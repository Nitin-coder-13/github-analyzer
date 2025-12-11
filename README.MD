# GitHub Repository Analyzer

A FastAPI-based tool to analyze GitHub repositories with detailed insights on commits, contributors, and code patterns.

## Features (Planned)
- Repository metadata analysis
- Commit pattern detection
- Top contributor identification
- Code churn analysis
- REST API with caching

## Tech Stack
- **Backend:** FastAPI, Python 3.13
- **API Integration:** PyGithub
- **Caching:** Redis
- **Database:** PostgreSQL
- **Deployment:** AWS EC2

## Project Status
🚧 Currently in development - Stage 1 (Project Setup)

## Setup Instructions
1. Clone the repository
2. Create virtual environment: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run server: `uvicorn app.main:app --reload`

## Author
Nitin Pandey - [GitHub](https://github.com/Nitin-coder-13)
