import pandas as pd
import re
import torch
from sys import argv
from datasets import load_dataset
from transformers import (
    pipeline, 
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    Trainer, 
    TrainingArguments,
    BertForQuestionAnswering,
    BertTokenizer
)

def analyze_input(emotion_analyzer, text : str) -> str:
    """
    Keeps prompting the user for input and performs emotional analysis on each input.
    Prints the detected emotion and confidence score.
    """

    label2emotion = {
        '0': "sadness",
        '1': "joy",
        '2': "love",
        '3': "anger",
        '4': "fear",
        '5': "surprise",
        '6': "suicidal",
        '7': "sexual violence",
        '8': "physical violence",
        '9': "emotional violence",
        '10': "economic violence",
        '11': "harmful traditional practice"
    }

    emotions = emotion_analyzer(text)
    #Fix print statement
    emotion = emotions[0]['label'].split('_')[1]
    confidence = emotions[0]['score'] * 100
    result =  f"Emotion:{emotion},Confidence:{confidence:.1f}%"
    return f"Your journal entry indicates that you are feeling {label2emotion[emotion]} with a confidence of {confidence:.1f}%"
    

def tokenize_function(examples, tokenizer):
    """
    Tokenizes the input examples using the specified tokenizer.
    """
    return tokenizer(examples["text"], padding="max_length", truncation=True)

def train_model(model, tokenized_datasets, training_args, tokenizer, device) -> None:
    # Move model to the specified device
    model.to(device)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
    )

    # Fine-tune the model
    trainer.train()

    # Save the model
    model.save_pretrained("model")
    tokenizer.save_pretrained("tokenizer")

def add_label(input_csv_file: str, output_csv_file: str, label: str, column_name: str = "label") -> None:
    """
    Given a csv file, adds a column full of a specific value. The name of the new column is 'label' by default but can be specified.
    Creates a new csv file.
    """
    df = pd.read_csv(input_csv_file, encoding="latin1")
    df[column_name] = label
    df.dropna(inplace=True)
    df.to_csv(output_csv_file, index=False)

def split_data(original_data_file: str, training_file: str, validation_file: str, training_percent: int = 80) -> None:
    """
    Separates a dataset into training and validation sections. By default, 80% of the data will be used for training and 20% for validation.
    Creates a new csv file for the validation data.
    """
    df = pd.read_csv(original_data_file)
    
    # Sample the training data
    training = df.sample(frac=training_percent / 100)
    
    # The validation data is the remainder of the dataset
    validation = df.drop(training.index)
    
    # Save the validation data to a new CSV file
    validation.to_csv(validation_file, index=False)
    training.to_csv(training_file, index=False)

def teach_emotion(training_file: str, validation_file: str, model_name: str, num_labels: int, device: str) -> None:
    """
    Trains a model to detect emotions from text data.
    """
    dataset = load_dataset('csv', data_files={'train': training_file, 'validation': validation_file})

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the dataset
    tokenized_datasets = dataset.map(lambda examples: tokenize_function(examples, tokenizer), batched=True)
    tokenized_datasets.set_format("torch", columns=["input_ids", "attention_mask", "label"])

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels, ignore_mismatched_sizes=True)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Train the model with device specification
    train_model(model, tokenized_datasets, training_args, tokenizer, device)

def fix_data(data_file : str, new_file : str) -> None:
    # Define the regular expression
    pattern = re.compile(r'(\d+),[^,]+,suicide')

    # Read the input file and filter lines
    with open(data_file, 'r') as infile, open(new_file, 'w') as outfile:
        for line in infile:
            if pattern.search(line):
                outfile.write(line)

def combine_files(files : list[str], combined_file_path : str, rows_to_keep : int=None) -> None:
    # Combine all csv files into one
    dfs = [pd.read_csv(file, index_col=False).dropna() for file in files]
    combined_df = pd.concat(dfs, ignore_index=True)

    combined_df["label"] = combined_df["label"].astype(int)

    combined_df = combined_df.sample(frac=1).reset_index(drop=True)

    if rows_to_keep is not None:
        combined_df = combined_df.head(rows_to_keep)

    combined_df.to_csv(combined_file_path, index=False)

def delete_lines_with_non_digit_substring(input_file, output_file):
    # Define the regex pattern: match a comma followed by one or more non-digit characters
    pattern = r",[^\d]+"

    # Open the input file and read all lines
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Filter out lines that match the pattern
    filtered_lines = [line for line in lines if not re.search(pattern, line)]

    # Write the remaining lines to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(filtered_lines)

def delete_first_column(input_csv_file : str, output_csv_file : str):
    df = pd.read_csv(input_csv_file)
    df.drop(df.columns[0], axis=1, inplace=True)
    df.to_csv(output_csv_file, index=False)

def answer_question(qa_pipeline, question, text):
    result = qa_pipeline({
        'question': question,
        'context': text
    })
    return result['answer']

            
if __name__ == "__main__":
    data_file = "data/data.csv"
    training_file = "data/training.csv"
    validation_file = "data/validation.csv"

    data2 = "data/Suicide_Detection.csv"
    cleaned = "data/suicide_cleaned.csv"
    
    device = "cuda:0"  # Set the device here
    
    if len(argv) >= 2 and argv[1] == "test":
        #analyze_input(pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base"))
        analyze_input(pipeline("text-classification", model="model", tokenizer="tokenizer"), """
I am feeling depressed
I want to kill myself
I want to kill myself
I want to end it all
I hate myself
Make it stop
IM SO FUCKING ANGRY
""")

    elif len(argv) >= 2 and argv[1] == "fix":
        delete_lines_with_non_digit_substring("data/suicide_cleaned.csv", "data/suicide_cleaned2.csv")
    
    elif len(argv) >= 2 and argv[1] == "ask":
        # Initialize the question-answering pipeline once
        qa_pipeline = pipeline("question-answering", model="meta-llama/Llama-3.1-8B")

        text = "He told me he would kill me"
        question = "Has he threatened to kill me?"

        # Call the answer_question function
        answer = answer_question(qa_pipeline, question, text)
        print(answer)
    
    else:
        files_to_process = ["data/test.csv", "data/suicide_cleaned.csv", "data/big_data.csv", "data/violence_cleaned.csv"]
        for index, file in enumerate(files_to_process):
            df = pd.read_csv(file, encoding="latin1")
            if "label" not in df.columns:
                add_label(file, file.split(".")[0] + "_labeled.csv", 6)
                files_to_process[index] = file.split(".")[0] + "_labeled.csv"
        combine_files(files_to_process, "data/full_dataset.csv", 20000)
        split_data("data/full_dataset.csv", "data/full_training.csv", "data/full_validation.csv")
        teach_emotion("data/full_training.csv", "data/full_validation.csv", "j-hartmann/emotion-english-distilroberta-base", 12, device)
