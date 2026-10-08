from google import genai
import os

# Connect to Gemini
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# Load the File Search store
with open("store_name.txt", "r") as f:
    store_name = f.read().strip()

print("Textbook loaded.")
print("Ask a question about your textbook.")
print("Type 'quit' to exit.\n")


while True:

    question = input("You: ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    print("\nSearching textbook...\n")

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=f"""
You are a college-level textbook tutor.

Answer the student's question using the provided textbook.

Instructions:
- Use the textbook as your primary source.
- Give a clear, accurate explanation.
- Do not invent information.
- If the textbook contains relevant information, use it.
- When textbook citations are available, preserve them.

Student question:
{question}
""",
        tools=[
            {
                "type": "file_search",
                "file_search_store_names": [store_name]
            }
        ]
    )

    # Display the answer
    print("AI:")
    print(response.output_text)

    # Look for textbook citations
    citations = []

    for step in response.steps:

        if step.type == "model_output":

            for content in step.content:

                if content.type == "text" and content.annotations:

                    for annotation in content.annotations:

                        if annotation.type == "file_citation":

                            citation = {
                                "file": getattr(
                                    annotation, "file_name", None
                                ),
                                "page": getattr(
                                    annotation, "page_number", None
                                ),
                                "source": getattr(
                                    annotation, "source", None
                                )
                            }

                            citations.append(citation)

    # Display citations if Gemini returned them
    if citations:

        print("\nSources:")

        for citation in citations:

            file_name = citation["file"]
            page = citation["page"]

            if page:
                print(f"- {file_name}, page {page}")
            else:
                print(f"- {file_name}")

    else:

        print("\nSources:")
        print("- No citation information was returned for this response.")

    print()