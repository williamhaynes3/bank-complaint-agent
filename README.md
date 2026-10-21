bank-complaint-agent
Bank complaint teams get a steady flow of customer complaints, many of them the same kind the CFPB publishes in its public complaint database. Sorting them by type and deciding what to do next takes time. This project is my attempt to build a small AI agent that helps with that first pass: read a complaint, label it, and suggest a next step. I'm building it in public, one week at a time, to learn hands-on AI development.

What it does today
Week 1 is one script, hello_llm.py. It sends a single sample complaint ("You charged me a $35 overdraft fee twice.") to Anthropic's Claude model and prints back a classification and a suggested next step.

It does not read the CFPB data yet. The sample complaint is written into the script.

How to run it
You need Python 3 and an Anthropic API key.

Clone the repo and move into it:
git clone https://github.com/williamhaynes3/bank-complaint-agent.git
cd bank-complaint-agent

Make a virtual environment and turn it on:
python3 -m venv .venv
source .venv/bin/activate

Install the two packages the script uses (there is no requirements file yet):
pip install anthropic python-dotenv

Make a file called .env in the project folder with your key:
ANTHROPIC_API_KEY=your-key-here

Run it:
python hello_llm.py

.env and any .csv files are in .gitignore, so your key and data stay on your machine.

Getting the complaint data
The data comes from the CFPB Consumer Complaint Database at https://www.consumerfinance.gov/data-research/consumer-complaints/. Filter the product to "Checking or savings account," pick a date range, and download the CSV into the project folder. The current code does not use it yet. It's there for the next step.

Roadmap (planned, not built yet)
Load the CFPB CSV into DuckDB so it can be queried with SQL
Run real complaints through the model to classify them and write short summaries a bank complaint team could use
Status
Week 1 of a learning project. Early and small on purpose.

Author
Will Haynes
