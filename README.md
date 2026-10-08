Textbook Agent
A simple AI textbook tutor built with Python, Google's Gemini API, and Gemini File Search. The agent uses a PDF textbook as its knowledge source so it can answer questions based on the textbook and identify where the information was found.
Features
- Answers questions about the textbook
- Uses the uploaded textbook as the primary source
- Provides concise answers
- Provides the textbook chapter and page where the information was found when available
- Runs directly from the VS Code terminal
- Uses Gemini File Search for retrieving relevant textbook content
Project Structure
TextbookAgent/
├── venv/
├── textbook.pdf
├── setup_textbook.py
├── ask_textbook.py
├── test_gemini.py
├── store_name.txt
└── README.md
File Descriptions
- textbook.pdf — The textbook used by the AI tutor.
- setup_textbook.py — Creates a Gemini File Search store and uploads the textbook. Run this when setting up a new textbook.
- ask_textbook.py — Main program used to ask questions about the textbook.
- test_gemini.py — Simple test used to verify that the Gemini API connection works.
- store_name.txt — Stores the name of the Gemini File Search store created during setup.
- venv/ — Python virtual environment containing the project's dependencies.
Requirements
- macOS, Windows, or Linux
- Python 3.13 or compatible Python version
- A Google Gemini API key
- The google-genai Python package
- A textbook in PDF format
Setup
1. Open the project in VS Code
Open the TextbookAgent folder in VS Code.
2. Open the terminal
In VS Code, select:
Terminal → New Terminal
3. Activate the virtual environment
On macOS/Linux:
cd ~/TextbookAgent
source venv/bin/activate
4. Set the Gemini API key
The project expects the API key to be stored in the GEMINI_API_KEY environment variable.
For macOS/Linux:
export GEMINI_API_KEY="YOUR_API_KEY"
Do not place your API key directly into the Python files or commit it to GitHub.
5. Install the Gemini package
If it has not already been installed:
pip install google-genai
Setting Up the Textbook
Make sure the textbook is named:
textbook.pdf
and is located in the main TextbookAgent folder.
Run:
python setup_textbook.py
This will:
1. Create a Gemini File Search store.
2. Upload textbook.pdf.
3. Wait for the textbook to finish processing.
4. Save the File Search store name to store_name.txt.
Important: You normally only need to run setup_textbook.py when setting up a new textbook. Running it again creates a new File Search store.
Running the Textbook Tutor
Activate the virtual environment:
cd ~/TextbookAgent
source venv/bin/activate
Then run:
python ask_textbook.py
You can then type questions directly into the terminal.
Example:
You: What is a query result set?
The AI will answer the question and provide a textbook location when available.
To exit the program:
quit
How It Works
The project uses Gemini's File Search functionality to search the uploaded textbook.
The general process is:
Student Question
       ↓
ask_textbook.py
       ↓
Gemini 3.8 Flash
       ↓
Gemini File Search
       ↓
Textbook PDF
       ↓
Relevant textbook information
       ↓
Answer + Chapter/Page
The AI is instructed to use the textbook as its source rather than relying on unrelated information.
Testing the Gemini Connection
To test whether the Gemini API is working:
python test_gemini.py
A successful test should return a short response from Gemini.
Troubleshooting
GEMINI_API_KEY error
If you see an error indicating that the API key is missing, set the environment variable again:
export GEMINI_API_KEY="YOUR_API_KEY"
Then run the program again.
Textbook cannot be found
Make sure the file is named exactly:
textbook.pdf
and is inside the TextbookAgent folder.
File Search store error
Check that store_name.txt exists:
ls
If the store has not been created yet, run:
python setup_textbook.py
API quota or rate-limit error
Check your Gemini API project and billing/quota settings. The error may indicate that the project has reached its available request limit.
Updating the Textbook
If you want to use a different textbook:
1. Replace textbook.pdf with the new textbook.
2. Run:
python setup_textbook.py
3. The new File Search store name will be saved to store_name.txt.
4. Run:
python ask_textbook.py
Important Security Note
Never share your Gemini API key publicly.
Do not commit your API key to GitHub or place it directly inside:
- ask_textbook.py
- setup_textbook.py
- test_gemini.py
Using the GEMINI_API_KEY environment variable keeps the key separate from the project code.
Current Model
The project currently uses:
gemini-3.8-flash
through Google's google-genai Python package.
