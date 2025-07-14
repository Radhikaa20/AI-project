# backend/summarizer.py

import openai

openai.api_key = "your-openai-api-key"  # or use os.getenv("OPENAI_API_KEY")

def summarize_text(text, max_words=1000):
    if len(text.split()) > max_words:
        text = " ".join(text.split()[:max_words])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Please summarize the following:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']
