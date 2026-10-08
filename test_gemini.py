from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

print("Sending test request...")

response = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say hello in one short sentence."
)

print("Gemini responded:")
print(response.output_text)