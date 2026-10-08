from google import genai
import os
import time

# Connect to Gemini
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

print("Creating File Search store...")

# Create the File Search store
store = client.file_search_stores.create(
    config={
        "display_name": "My Textbook"
    }
)

print("File Search store created:")
print(store.name)

print("\nUploading textbook...")

# Upload the textbook to the File Search store
operation = client.file_search_stores.upload_to_file_search_store(
    file="textbook.pdf",
    file_search_store_name=store.name,
    config={
        "display_name": "Textbook PDF"
    }
)

print("Textbook uploaded.")
print("Waiting for textbook processing...")

# Wait until Gemini finishes processing the PDF
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)
    print(".", end="", flush=True)

print("\n\nTextbook processing complete!")

# Display the File Search store name
print("File Search store:", store.name)

# Save the store name so ask_textbook.py can use it
with open("store_name.txt", "w") as f:
    f.write(store.name)

print("\nStore name saved to store_name.txt")
print("Setup complete!")