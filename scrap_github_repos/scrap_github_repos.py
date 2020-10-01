import sys
from github import Github


def repository_names(user):
    repo_names = []
    for repo in user.get_repos():
        repo_names.append(repo)
    return repo_names


def repository_details(user):
    all_repo_details = []
    repo_names = repository_names(user)
    for repo in repo_names:
        repo_details = {}
        repo_details["Name"] = repo.full_name.split("/")[1]
        repo_details["Description"] = repo.description
        repo_details["Created on"] = repo.created_at
        repo_details["Programming language"] = repo.language
        repo_details["Forked"] = str(repo.forks) + " time(s)"
        all_repo_details.append(repo_details)
    return all_repo_details


if __name__ == "__main__":
    username = sys.argv[1]
    user = Github().get_user(username)
    github_repository_task = repository_details(user)
    for content in github_repository_task:
        for title, description in content.items():
            print(title, ":", description)
        print("\n" * 20)
