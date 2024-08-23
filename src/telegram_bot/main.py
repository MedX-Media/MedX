import requests
import json
import time

# Define the bot token and the channel chat ID for sending messages via Telegram
BOT_TOKEN = "<BOT_TOKEN>"
CHANNEL_CHAT_ID = "<CHANNEL_CHAT_ID>"

# URL to access the GitHub API for the specific repository's commits
REPO_URL_API = '<REPO_URL_API>'

# Personal GitHub token for authentication
GITHUB_TOKEN = '<GITHUB_TOKEN>'

def recive_last_commit_data(repo_url_api, github_token):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response = requests.get(repo_url_api, headers=headers)
    commits = response.json()

    if commits:
        return commits[0]  # Returning the latest commit
    else:
        return None  # If no commits are found, return None

def save_json_to_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def extract_important_info(commit_data):
    important_info = {
        "sha": commit_data.get("sha"),
        "author_name": commit_data["commit"]["author"].get("name"),
        "author_email": commit_data["commit"]["author"].get("email"),
        "message": commit_data["commit"].get("message"),
        "commit_url": commit_data.get("html_url")
    }
    return important_info

def format_message(info):
    message = (
        "🚀 *New Commit Detected*\n\n"
        "🔗 *SHA:* `{sha}`\n"
        "👤 *Author:* {author_name} ({author_email})\n"
        "📝 *Message:* {message}\n\n"
        "🔍 [View Commit]({commit_url})".format(**info)
    )
    return message

def send_tel(mess, bot_token, chat_id):
    data = {
        'UrlBox': f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mess}&parse_mode=Markdown',
        'ContentTypeBox': '',
        'ContentDataBox': '',
        'HeadersBox': '',
        'RefererBox': '',
        'AgentList': 'Internet Explorer',
        'AgentBox': '',
        'VersionsList': 'HTTP/1.1',
        'MethodList': 'GET',
    }
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response

# Main loop to continuously check for new commits
last_checked_sha = None

while True:
    # Fetch the last commit data from the GitHub repository
    last_commit_data = recive_last_commit_data(REPO_URL_API, GITHUB_TOKEN)

    if last_commit_data:
        # Check if the commit is new by comparing the SHA
        if last_commit_data['sha'] != last_checked_sha:
            last_checked_sha = last_commit_data['sha']

            # Save the commit data to a JSON file
            save_json_to_file(last_commit_data, 'data.json')
            print(f"New commit detected and data saved to 'data.json'")

            # Extract the important information from the last commit data & Format the extracted information into a message
            important_info = extract_important_info(last_commit_data)
            telegram_message = format_message(important_info)

            # Send the formatted message to the Telegram channel
            response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)
            print("Message sent to Telegram channel")
        else:
            print("No new commit detected.")

    # Wait for a specific amount of time before checking again (e.g., 60 seconds)
    time.sleep(60)

