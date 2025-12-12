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

    def get_commit_analysis(self, repo_url: str, max_commits: int = 100):
        """
        Analyze commit patterns and get top contributors
        """
        try:
            parts = repo_url.rstrip('/').split('/')
            owner = parts[-2]
            repo_name = parts[-1]

            repo = self.client.get_repo(f"{owner}/{repo_name}")
            commits = repo.get_commits()[:max_commits]  # Get last 100 commits

            # Data structures for analysis
            commit_hours = {}  # Hour -> count
            contributors = {}  # Author -> commit count

            for commit in commits:
                # Extract commit hour (0-23)
                # Extract commit hour (0-23) and convert to IST
                if commit.commit.author.date:
                    # Convert UTC to IST (UTC + 5:30)
                    from datetime import timedelta
                    ist_time = commit.commit.author.date + timedelta(hours=5, minutes=30)
                    hour = ist_time.hour
                    commit_hours[hour] = commit_hours.get(hour, 0) + 1
                # Count commits per contributor
                author = commit.commit.author.name
                contributors[author] = contributors.get(author, 0) + 1

            # Find peak commit hour
            peak_hour = max(commit_hours.items(), key=lambda x: x[1]) if commit_hours else (0, 0)

            # Get top 10 contributors using heap concept (sorted by commit count)
            top_contributors = sorted(contributors.items(), key=lambda x: x[1], reverse=True)[:10]

            return {
                "total_commits_analyzed": max_commits,
                "peak_commit_hour": {
                    "hour": peak_hour[0],
                    "commits": peak_hour[1]
                },
                "commit_distribution_by_hour": commit_hours,
                "top_contributors": [
                    {"name": name, "commits": count}
                    for name, count in top_contributors
                ]
            }

        except Exception as e:
            return {"error": str(e)}

    def get_code_churn(self, repo_url: str, max_commits: int = 50):
        """
        Analyze code churn - lines added and deleted over time
        """
        try:
            from datetime import timedelta

            parts = repo_url.rstrip('/').split('/')
            owner = parts[-2]
            repo_name = parts[-1]

            repo = self.client.get_repo(f"{owner}/{repo_name}")
            commits = list(repo.get_commits()[:max_commits])

            churn_data = []
            total_additions = 0
            total_deletions = 0

            for commit in commits:
                # Convert to IST
                ist_time = commit.commit.author.date + timedelta(hours=5, minutes=30)

                churn_data.append({
                    "date": ist_time.strftime("%Y-%m-%d"),
                    "time": ist_time.strftime("%H:%M"),
                    "additions": commit.stats.additions,
                    "deletions": commit.stats.deletions,
                    "total_changes": commit.stats.total,
                    "message": commit.commit.message.split('\n')[0][:50]  # First line, truncated
                })

                total_additions += commit.stats.additions
                total_deletions += commit.stats.deletions

            # Calculate average churn per commit
            avg_additions = total_additions / len(commits) if commits else 0
            avg_deletions = total_deletions / len(commits) if commits else 0

            return {
                "commits_analyzed": len(commits),
                "total_additions": total_additions,
                "total_deletions": total_deletions,
                "net_change": total_additions - total_deletions,
                "avg_additions_per_commit": round(avg_additions, 2),
                "avg_deletions_per_commit": round(avg_deletions, 2),
                "churn_timeline": churn_data[:10]  # Return last 10 for brevity
            }

        except Exception as e:
            return {"error": str(e)}