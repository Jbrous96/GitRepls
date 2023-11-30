
from flask import Flask, request, jsonify
from github import Github, GithubException

app = Flask(__name__)

token = "your_github_token"
github = Github('INSERT_TOKEN_HERE')

@app.route('/commit', methods=['POST'])

# def commit_to_github(repo_name, file_name, file_data, commit_message, branch='main'):
#     user = github.get_user()
#     repo = user.get_repo(repo_name)

def commit_to_github():
    data = request.json
    repo_name = data['repo_name']
    file_name = data['file_name']
    file_data = data['file_data']
    commit_message = data['commit_message']
    branch = data('branch', 'main')

    try:
        user = github.get_user()
        repo = user.get_repo(repo_name)
        contents = repo.get_contents(file_name, ref=branch)
        repo.update_file(contents.path, commit_message, file_data, contents.sha, branch=branch)
    except GithubException:
        repo.create_file(file_name, commit_message, file_data, branch=branch)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':app.run(debug=True, port=5000)

# commit_to_github(
#     'TEST1',
#     'example.txt',
#     'File content here',
#     'Update example.txt'
# )
