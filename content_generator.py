import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(topic, tone="professional", words=300):
    prompt = f"Write a {words}-word article about {topic} in a {tone} tone."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful content generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Example usage
topic = input("Enter your topic: ")
print("\nGenerated Content:\n")
print(generate_content(topic))