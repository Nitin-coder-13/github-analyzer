from fastapi import APIRouter
from pydantic import BaseModel
from app.services.github_service import GitHubService

router = APIRouter()
github_service = GitHubService()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/analyze")
def analyze_repository(request: RepoRequest):
    """
    Analyze a GitHub repository
    """
    repo_info = github_service.get_repo_info(request.repo_url)
    return {
        "status": "success",
        "data": repo_info
    }