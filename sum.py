from transformers import T5Tokenizer, T5ForConditionalGeneration
from app import extraction 

def summarize_text_list(text_list):
    # Load the pre-trained model and tokenizer
    model_name = "t5-small"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # Concatenate the list of strings into a single text
    text = ' '.join(text_list)

    # Print the text to debug
    # print("Read text:", text[:500])  # Print the first 500 characters for debugging

    # Tokenize and encode the text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary
    summary_ids = model.generate(inputs, num_beams=4, max_length=150, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Summarize the list of texts
# summary = summarize_text_list(extraction('https://www.biospace.com/news/money/'))
#print("Summary:", summary)
