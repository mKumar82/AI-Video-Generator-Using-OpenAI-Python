from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = api_key

# Initialize the OpenAI client
client = OpenAI()

# Set the model to use
model_engine = "gpt-3.5-turbo-0125"

# Set the prompt to generate text for
text = input("What topic you want to write about: ")
prompt = text

print("The AI BOT is trying now to generate a new text for you...")

# Generate text using the GPT-3 model
completion = client.chat.completions.create(
    model=model_engine,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print the generated text
generated_text = completion.choices[0].message.content
print(generated_text)

# Save the text in a file
with open("generated_text.txt", "w") as file:
    file.write(generated_text)

print("The Text Has Been Generated Successfully!")
