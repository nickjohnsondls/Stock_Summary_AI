from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_text(file_path):
    # Load the pre-trained model and tokenizer
    model_name = "t5-small"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Print the text to debug
    print("Read text:", text[:500])  # Print the first 500 characters for debugging

    # Tokenize and encode the text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary
    summary_ids = model.generate(inputs, num_beams=4, max_length=150, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Path to your .txt file
file_path = 'testing.txt'

# Summarize the text
summary = summarize_text(file_path)
print("Summary:", summary)
