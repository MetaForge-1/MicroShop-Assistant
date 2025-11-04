MicroShop Assistant — Quick Start (for your friend)
--------------------------------------------------

Hi — thanks for trying out MicroShop Assistant! This file explains how to get the project running locally.

Included files:
- app.py                  # Streamlit frontend
- microshop_backend.py    # Backend AI logic (Flan-T5 + Hindi translator)
- inventory.csv           # Sample inventory data
- requirements.txt        # Python dependencies
- README.txt              # This file

IMPORTANT NOTES
- Python 3.9+ is required.
- The first run will download Hugging Face models (~1 GB). After that, the app runs offline.
- Do NOT include a virtual environment folder in the zip; create one locally.

Quick manual setup (Windows / macOS / Linux)
--------------------------------------------

1) Open a terminal and change into the project folder (where you unzipped the project):
   - Windows (PowerShell):
     > cd C:\path\to\MicroShopAssistant
   - macOS / Linux:
     $ cd /path/to/MicroShopAssistant

2) Create a virtual environment:
   - Windows:
     > python -m venv venv
   - macOS / Linux:
     $ python3 -m venv venv

3) Activate the virtual environment:
   - Windows (PowerShell):
     > venv\Scripts\Activate.ps1
     (If you get "running scripts is disabled", run PowerShell as Administrator and execute:
       Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
       then re-run the Activate.ps1 command.)
   - Windows (Command Prompt):
     > venv\Scripts\activate
   - macOS / Linux:
     $ source venv/bin/activate

   After activation you should see (venv) at the start of your prompt.

4) Install dependencies:
   (make sure (venv) is active)
   > pip install -r requirements.txt

5) Run the Streamlit app:
   > streamlit run app.py

6) In the browser page that opens (usually http://localhost:8501) upload `inventory.csv` to try it.
   The first time you generate messages the app will download the Hugging Face models (Flan-T5 and the English→Hindi translator).

If you want the exact commands tailored to your OS and terminal (PowerShell, cmd, bash, zsh), copy & paste the AI prompt below into ChatGPT (or your assistant in your account). It will produce ready-to-run commands for your specific environment.

-------------------------
AI PROMPT (paste this into ChatGPT or another assistant)
-------------------------
I have a Python project folder with these files: `app.py`, `microshop_backend.py`, `inventory.csv`, and `requirements.txt`. I want step-by-step terminal commands to set up and run it locally on my machine.

Please:
1. Detect and ask me which OS I'm using (Windows / macOS / Linux).
2. Ask which shell I will use (PowerShell / Command Prompt / bash / zsh).
3. After I reply, provide exact commands (copy-paste ready) to:
   - change into the project directory (I will paste the full project path when asked),
   - create a Python virtual environment,
   - activate the virtual environment for my shell,
   - install dependencies with `pip install -r requirements.txt`,
   - run the Streamlit app with `streamlit run app.py`.
4. If I’m on Windows PowerShell, include a note and a command to set the execution policy if needed:
   `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
5. Also include a short troubleshooting checklist for common issues:
   - "python not found" (how to check PATH),
   - "permission error activating venv",
   - what to do if models fail to download (check internet, retry).
6. End with a short line telling me how to stop the Streamlit server (Ctrl+C in the terminal).

When you paste this prompt into ChatGPT, answer the assistant’s follow-up questions (OS, shell, and the folder path) and then run the exact commands it returns.

-------------------------
Short message you can send to your friend (optional copy-paste):
-------------------------
Hi — I zipped a small Python project called *MicroShopAssistant*. Unzip it, open a terminal in the project folder, paste the AI prompt (from README.txt) into ChatGPT, follow the commands it gives to create and activate a virtual environment, install dependencies, and run `streamlit run app.py`. The UI will open in your browser — upload `inventory.csv` to test. The first run downloads models (about 1 GB); after that it runs offline.

If you want, I can also provide a one-click Windows PowerShell script to automate venv creation + install. Let me know.

Enjoy! — Animesh
