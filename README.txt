QUIKANSWER - GROQ Q&A CHATBOT
=============================

ABOUT
-----
QuikAnswer is a Streamlit chat app that answers questions with a Groq-hosted
language model. It can use Google Serper search for current information and
keeps conversation memory while the app is running.

PROJECT FILE
------------
apps/Qna_chatBot_with_groq.py

TOOLS AND SERVICES
------------------
- Python 3.10 or newer
- Streamlit for the web interface
- LangChain and LangGraph for the agent and in-memory checkpointing
- Groq API, using the openai/gpt-oss-20b model
- Google Serper API for web search
- python-dotenv to load local API keys from a .env file

SET UP (WINDOWS POWERSHELL)
---------------------------
Run these commands from the project root folder:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

If the Python launcher "py" is unavailable, use "python" instead:

    python -m venv .venv

API KEYS
--------
Create a file named .env in the project root and add your own API keys:

    GROQ_API_KEY=your_groq_api_key
    SERPER_API_KEY=your_serper_api_key

Obtain keys from Groq and Serper. Do not commit or share the .env file.
The repository .gitignore excludes it.

RUN THE APP
-----------
With the virtual environment activated, run from the project root:

    python -m streamlit run .\apps\Qna_chatBot_with_groq.py

Streamlit will print a local URL (usually http://localhost:8501) and open the
app in your browser.

TROUBLESHOOTING
---------------
- If a package is missing, activate the virtual environment and rerun:
      python -m pip install -r requirements.txt
- If the app reports missing credentials, check that .env is in the project
  root and contains both GROQ_API_KEY and SERPER_API_KEY.
- If PowerShell blocks virtual-environment activation, open a new terminal
  and run the virtual environment's Python directly:
      .\.venv\Scripts\python.exe -m pip install -r requirements.txt
      .\.venv\Scripts\python.exe -m streamlit run .\apps\Qna_chatBot_with_groq.py
