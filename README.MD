# 🔍 GitHub Repository Analyzer

A powerful REST API built with FastAPI that analyzes GitHub repositories and provides detailed insights into commit patterns, contributor activity, and code changes over time.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### 1. Repository Metadata Analysis
- Fetch comprehensive repository information
- Get star count, fork count, and primary language
- View creation and last update timestamps

### 2. Commit Pattern Analysis
- Identify peak commit hours (with IST timezone support)
- Analyze commit distribution across 24-hour periods
- Discover top 10 contributors by commit count
- Understand team productivity patterns

### 3. Code Churn Analysis
- Track lines added and deleted over time
- Calculate net codebase growth
- View average changes per commit
- Timeline of recent commits with change statistics

## 🚀 Why This Project?

This project demonstrates:
- **Real API Integration**: Works with live GitHub data via REST API
- **Data Processing**: Analyzes and aggregates commit data efficiently
- **Algorithm Application**: Uses hash maps for O(1) lookups, sorting for rankings
- **Professional Practices**: Git workflow, branching strategy, pull requests
- **Problem Solving**: Timezone conversion, error handling, data validation

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI (async Python web framework)
- **API Integration**: PyGithub (GitHub REST API wrapper)
- **Language**: Python 3.13
- **Environment Management**: python-dotenv
- **API Documentation**: Automatic Swagger UI via FastAPI

## 📋 Prerequisites

- Python 3.13+
- Git
- GitHub account (optional: for higher API rate limits with token)

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Nitin-coder-13/github-analyzer.git
cd github-analyzer
```

2. **Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment (Optional)**
```bash
# Create .env file for GitHub token (increases API rate limit)
echo "GITHUB_TOKEN=your_github_token_here" > .env
```

5. **Run the server**
```bash
uvicorn app.main:app --reload
```

6. **Access the API**
- API Base URL: `http://127.0.0.1:8000`
- Interactive Docs: `http://127.0.0.1:8000/docs`

## 📖 API Endpoints

### 1. Analyze Repository Metadata
**Endpoint**: `POST /api/analyze`

**Request Body**:
```json
{
  "repo_url": "https://github.com/torvalds/linux"
}
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "name": "linux",
    "full_name": "torvalds/linux",
    "description": "Linux kernel source tree",
    "stars": 180000,
    "forks": 53000,
    "language": "C",
    "created_at": "2011-09-04 22:48:12",
    "updated_at": "2024-12-11 10:30:45"
  }
}
```

### 2. Analyze Commit Patterns
**Endpoint**: `POST /api/analyze/commits`

**Request Body**:
```json
{
  "repo_url": "https://github.com/fastapi/fastapi"
}
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "total_commits_analyzed": 100,
    "peak_commit_hour": {
      "hour": 14,
      "commits": 15
    },
    "commit_distribution_by_hour": {
      "10": 5,
      "11": 8,
      "14": 15,
      "16": 12
    },
    "top_contributors": [
      {"name": "Sebastián Ramírez", "commits": 45},
      {"name": "John Doe", "commits": 20}
    ]
  }
}
```

### 3. Analyze Code Churn
**Endpoint**: `POST /api/analyze/churn`

**Request Body**:
```json
{
  "repo_url": "https://github.com/microsoft/vscode"
}
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "commits_analyzed": 50,
    "total_additions": 15420,
    "total_deletions": 8230,
    "net_change": 7190,
    "avg_additions_per_commit": 308.4,
    "avg_deletions_per_commit": 164.6,
    "churn_timeline": [
      {
        "date": "2024-12-11",
        "time": "15:30",
        "additions": 245,
        "deletions": 120,
        "total_changes": 365,
        "message": "Add new feature for syntax highlighting"
      }
    ]
  }
}
```

## 🏗️ Project Structure
```
github-analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── analyzer.py         # API route handlers
│   ├── services/
│   │   ├── __init__.py
│   │   └── github_service.py   # GitHub API integration logic
│   ├── models/                 # (Future: database models)
│   ├── core/                   # (Future: config & settings)
│   └── utils/                  # (Future: helper functions)
├── .env                        # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧠 Technical Highlights

### Algorithm & Data Structure Usage

1. **Hash Maps (Dictionaries)**
   - Used for counting commits per hour: O(1) insert and lookup
   - Contributor commit counting: O(1) operations
   - Efficient for aggregating large datasets

2. **Sorting Algorithm**
   - Top contributors ranking: O(n log n) using Python's Timsort
   - Could be optimized to O(n log k) with min-heap for top K elements

3. **Time Complexity Analysis**
   - Commit analysis: O(n) where n = number of commits
   - Contributor ranking: O(n log n) for sorting
   - Overall API response: O(n log n) dominated by sorting

### Real-World Problem Solving

**Timezone Conversion Challenge:**
- GitHub stores all timestamps in UTC
- Implemented timezone conversion (UTC → IST) for accurate local times
- Used Python's datetime and timedelta for conversion

**API Rate Limiting Awareness:**
- GitHub API has rate limits (60 requests/hour without token)
- Designed to analyze limited commits (50-100) per request
- Future: Add caching layer to reduce API calls

## 🎯 Future Enhancements

- [ ] **Caching Layer**: Redis integration to cache analysis results
- [ ] **Database Storage**: PostgreSQL to store historical analysis
- [ ] **Heap Optimization**: Min-heap for efficient top-K contributor queries
- [ ] **Branch Analysis**: Visualize branch/merge patterns using graph algorithms
- [ ] **Deployment**: AWS EC2/Lambda deployment with CI/CD pipeline
- [ ] **Authentication**: User accounts to track analysis history
- [ ] **Webhooks**: Real-time updates when repos change

## 🧪 Testing

Currently manual testing via Swagger UI. Future additions:
- Unit tests with pytest
- Mock GitHub API responses
- Integration tests for endpoints
- Load testing for scalability

## 📝 Development Workflow

This project follows professional Git practices:
- Feature branches for new development
- Pull requests with detailed descriptions
- Clean commit history
- Code reviews before merging

Example workflow:
```bash
git checkout -b feature/new-analysis
# ... make changes ...
git add .
git commit -m "Add new analysis feature"
git push -u origin feature/new-analysis
# Create PR on GitHub → Review → Merge
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write clear commit messages
5. Create a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Nitin Pandey**
- GitHub: [@Nitin-coder-13](https://github.com/Nitin-coder-13)
- Learning Journey: AI/ML Engineer Roadmap - Stage 1 Project

## 🙏 Acknowledgments

- Built as part of the AI/ML Engineer learning roadmap
- Inspired by the need to understand repository health and team dynamics
- Thanks to the FastAPI and PyGithub communities

---

⭐ If you find this project helpful, please consider giving it a star!