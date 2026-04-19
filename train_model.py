import pandas as pd
import re
import json
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

def clean_text(text):
    text = str(text)
    text = text.replace("{product_purchased}", "")
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()


def main():

    # ---------------- LOAD DATA ----------------
    df = pd.read_csv("customer_support_tickets.csv")
    df = df[['Ticket Description', 'Ticket Type']]

    # ---------------- CLEAN DATA ----------------
    df['Ticket Description'] = df['Ticket Description'].apply(clean_text)
    df = df[df['Ticket Description'].str.strip() != ""]

    print("Original Data Size:", len(df))

    # ---------------- STRATIFIED SAMPLING ----------------
    df_sample, _ = train_test_split(
        df,
        train_size=3000,                     # 🔥 change size here if needed
        stratify=df['Ticket Type'],          # 🔥 maintain class distribution
        random_state=42
    )

    df = df_sample
    print("Sampled Data Size:", len(df))
    print("Class Distribution:\n", df['Ticket Type'].value_counts())

    # ---------------- LABEL ENCODING ----------------
    df['label'] = df['Ticket Type'].astype('category').cat.codes

    label_map = dict(enumerate(df['Ticket Type'].astype('category').cat.categories))
    with open("label_map.json", "w") as f:
        json.dump(label_map, f)

    print("Label Mapping:", label_map)

    # ---------------- SPLIT ----------------
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    train_dataset = Dataset.from_pandas(train_df)
    test_dataset = Dataset.from_pandas(test_df)

    # ---------------- TOKENIZER ----------------
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

    def tokenize(example):
        return tokenizer(
            example['Ticket Description'],
            truncation=True,
            padding='max_length',         # 🔥 dynamic padding
            max_length=64         # 🔥 reduced for speed
        )

    train_dataset = train_dataset.map(tokenize, batched=True)
    test_dataset = test_dataset.map(tokenize, batched=True)

    # Remove unused columns
    cols_to_remove = ['Ticket Description', 'Ticket Type']
    if '__index_level_0__' in train_dataset.column_names:
        cols_to_remove.append('__index_level_0__')

    train_dataset = train_dataset.remove_columns(cols_to_remove)
    test_dataset = test_dataset.remove_columns(cols_to_remove)

    # ---------------- MODEL ----------------
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=df['label'].nunique()
    )

    # ---------------- METRICS ----------------
    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = logits.argmax(axis=1)
        return {"accuracy": accuracy_score(labels, preds)}

    # ---------------- TRAINING ----------------
    training_args = TrainingArguments(
        output_dir="./results",
        per_device_train_batch_size=8,    # 🔥 faster
        per_device_eval_batch_size=8,
        num_train_epochs=1,               # 🔥 reduced
        dataloader_num_workers=0
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        compute_metrics=compute_metrics
    )

    # ---------------- TRAIN ----------------
    trainer.train()

    # ---------------- EVALUATE ----------------
    metrics = trainer.evaluate()
    print("Final Evaluation:", metrics)

    # ---------------- SAVE ----------------
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")


if __name__ == "__main__":
    main()