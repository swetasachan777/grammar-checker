import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
import pandas as pd

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path).dropna()
    dataset = Dataset.from_pandas(df[['Incorrect Sentence', 'Correct Sentence']])
    return dataset.train_test_split(test_size=0.2)  # ✅ Splitting into train (80%) and eval (20%)

# Load Pretrained Model
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Tokenization
# Tokenization Function (Fixed)
def tokenize_data(batch):
    inputs = ["fix grammar: " + text for text in batch["Incorrect Sentence"]]  # ✅ Process as a list
    targets = [text for text in batch["Correct Sentence"]]

    tokenized_inputs = tokenizer(inputs, truncation=True, padding="max_length", max_length=128)
    tokenized_targets = tokenizer(targets, truncation=True, padding="max_length", max_length=128)

    return {
        "input_ids": tokenized_inputs["input_ids"],
        "attention_mask": tokenized_inputs["attention_mask"],  # ✅ Added attention mask
        "labels": tokenized_targets["input_ids"]
    }

# Load and process dataset
dataset_dict = load_data("grammar_correction.csv")  # ✅ Now dataset has train and eval sets
train_dataset = dataset_dict["train"].map(tokenize_data, batched=True)
eval_dataset = dataset_dict["test"].map(tokenize_data, batched=True)

# Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    evaluation_strategy="epoch",  # ✅ Evaluation enabled
    save_strategy="epoch",
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=10,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,  # ✅ Added train dataset
    eval_dataset=eval_dataset,  # ✅ Added eval dataset
)

# Train Model
trainer.train()

# Save Model
model.save_pretrained("grammar_corrector_model")
tokenizer.save_pretrained("grammar_corrector_model")
