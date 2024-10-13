import pandas as pd
import re
from sys import argv
from datasets import load_dataset
from transformers import (
    pipeline, 
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    Trainer, 
    TrainingArguments
)

# Load sentiment analysis model
# sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment of a text
# result = sentiment_analyzer("I'm feeling fantastic today!")
# print(result)  # Output: [{'label': 'POSITIVE', 'score': 0.9998}]

def analyze_input(emotion_analyzer) -> None:
    """
    Keeps prompting the user for input and performs emotional analysis on each input.
    Prints the detected emotion and confidence score.
    """
    text = input("Enter text to analyze: ")
    while text:
        emotions = emotion_analyzer(text)
        print(f"Emotion: {emotions[0]['label']}, Confidence: {emotions[0]['score'] * 100:.1f}%")
        text = input("Enter text to analyze: ")

def tokenize_function(examples, tokenizer):
    """
    Tokenizes the input examples using the specified tokenizer.
    """
    return tokenizer(examples["text"], padding="max_length", truncation=True)

def train_model(model, tokenized_datasets, training_args, tokenizer) -> None:
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
    df = pd.read_csv(input_csv_file)
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
    training = df.sample(frac=training_percent / 100, random_state=42)
    
    # The validation data is the remainder of the dataset
    validation = df.drop(training.index)
    
    # Save the validation data to a new CSV file
    validation.to_csv(validation_file, index=False)
    training.to_csv(training_file, index=False)

def teach_emotion(training_file: str, validation_file: str, model_name: str, num_labels: int) -> None:
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
    train_model(model, tokenized_datasets, training_args, tokenizer)

def fix_data(data_file : str, new_file : str) -> None:

    # Define the regular expression
    pattern = re.compile(r'(\d+),[^,]+,suicide')

    # Read the input file and filter lines
    with open(data_file, 'r') as infile, open(new_file, 'w') as outfile:
        for line in infile:
            if pattern.search(line):
                outfile.write(line)


            
            
            
if __name__ == "__main__":
    data_file = "data/data.csv"
    dataset = "data/test.csv"
    training_file = "data/training.csv"
    validation_file = "data/validation.csv"

    data2 = "data/Suicide_Detection.csv"
    cleaned = "data/suicide_cleaned.csv"
    
    if argv[1] == "test":
        analyze_input(pipeline("text-classification", model="model", tokenizer="tokenizer"))
    
    if argv[1] == "fix":
        fix_data(data2, cleaned)
    
    else:
        add_label(data_file, dataset, 7)
        split_data(dataset, training_file, validation_file)
        teach_emotion(training_file, validation_file, "j-hartmann/emotion-english-distilroberta-base", 8)
