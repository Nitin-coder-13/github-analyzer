from github import Github
import os
from dotenv import load_dotenv

load_dotenv()


class GitHubService:
    def __init__(self):
        # add token later, for now it works without one (but has rate limits)
        github_token = os.getenv("GITHUB_TOKEN")
        if github_token:
            self.client = Github(github_token)
        else:
            self.client = Github()  # Use without authentication

    def get_repo_info(self, repo_url: str):
        """
        Extract owner and repo name from URL and fetch basic info
        """
        try:
            # Parse the URL to get owner/repo
            parts = repo_url.rstrip('/').split('/')
            owner = parts[-2]
            repo_name = parts[-1]

            # Fetch repository
            repo = self.client.get_repo(f"{owner}/{repo_name}")

            return {
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "language": repo.language,
                "created_at": str(repo.created_at),
                "updated_at": str(repo.updated_at)
            }
        except Exception as e:
            return {"error": str(e)}