import json
import re
import time

import requests

# Define the bot token and the channel chat ID for sending messages via Telegram
BOT_TOKEN = "<BOT_TOKEN>"
CHANNEL_CHAT_ID = "-1002215464363"

# URL to access the GitHub API for the specific repository's commits and issues
REPO_URL_API = "https://api.github.com/repos/MedX-Media/MedX/commits"
REPO_URL_ISSUES = "https://api.github.com/repos/MedX-Media/MedX/issues"

# Personal GitHub token for authentication
GITHUB_TOKEN = "<GITHUB_TOKEN>"


# Function to receive the latest data (commits or issues) from the GitHub API
def recive_last_data(api_url, github_token):
    headers = {
        'Accept': 'application/vnd.github+json',  # Required GitHub API version
        'Authorization': f'Bearer {github_token}',  # Bearer token for auth
        'X-GitHub-Api-Version': '2022-11-28',
    }
    # Fetch data from the API
    response = requests.get(api_url, headers=headers)
    data = response.json()

    if data:
        return data[0]  # Returning the latest data (commit or issue)
    else:
        return None  # If no data is found, return None


# Save the data to a local JSON file
def save_json_to_file(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


# Extract essential information from the commit data
def extract_commit_info(commit_data):
    important_info = {
        "sha": commit_data.get("sha"),  # Commit SHA
        "author_name": commit_data["commit"]["author"].get("name"),  # Commit author
        "author_email": commit_data["commit"]["author"].get("email"),  # Author email
        "message": commit_data["commit"].get("message"),  # Commit message
        "commit_url": commit_data.get("html_url")  # URL to the commit on GitHub
    }
    return important_info


# Extract important information from the issue data
def extract_issue_info(issue_data):
    important_info = {
        "issue_number": issue_data.get("number"),  # Issue number
        "title": issue_data.get("title"),  # Issue title
        "user_login": issue_data["user"].get("login"),  # User who opened the issue
        "state": issue_data.get("state"),  # Issue state (open/closed)
        "labels": [label.get("name") for label in issue_data.get("labels", [])],  # Issue labels
        "created_at": issue_data.get("created_at"),  # Creation timestamp
        "updated_at": issue_data.get("updated_at"),  # Last update timestamp
        "issue_url": issue_data.get("html_url"),  # URL to the issue on GitHub
        "body": issue_data.get("body", "")  # Body of the issue (description)
    }
    return important_info


# Escape Markdown special characters to ensure proper formatting
def escape_markdown(text):
    escape_chars = r'\*_`\[\]()~>#+-=|{}.!'  # Characters to be escaped in Markdown
    return re.sub(r'([%s])' % re.escape(escape_chars), r'\\\1', text)

# Format the commit message to be sent to Telegram
def format_commit_message(info):
    info['message'] = escape_markdown(info['message'])  # Escape special characters in the commit message
    message = ("🚀 *New Commit Detected*\n\n"
               "🔗 *SHA:* `{sha}`\n"
               "👤 *Author:* {author_name} ({author_email})\n"
               "📝 *Commit Message:* {message}\n\n"
               "🔍 [View Commit]({commit_url})".format(**info))  # Message content using Markdown
    return message


# Format the issue message to be sent to Telegram
def format_issue_message(info):
    info['body'] = escape_markdown(info['body'])  # Escape special characters in the issue body
    labels = ", ".join([escape_markdown(label) for label in info["labels"]])  # Format labels
    message = (f"🐞 *New Issue Detected* - "
               f"🔢 *Issue Number:* `{info['issue_number']}`\n\n"
               f"📝 *Title:* {info['title']}\n"
               f"👤 *User:* {info['user_login']}\n"
               f"🏷️ *Labels:* {labels}\n\n"
               f"📅 *Created At:* {info['created_at']}\n"
               f"🔄 *Updated At:* {info['updated_at']}\n\n"
               f"🔗 [View Issue]({info['issue_url']})\n\n")  # Message content using Markdown
    return message


# Function to send messages to a Telegram channel via a bot
def send_tel(mess, bot_token, chat_id):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'  # Telegram API URL
    data = {
        'chat_id': chat_id,
        'text': mess,  # Message content
        'parse_mode': 'Markdown'  # Use Markdown formatting
    }
    response = requests.post(url, data=data)  # Send POST request to Telegram API
    return response


# Main loop to continuously check for new issues and commits
last_checked_sha = None  # To track the last checked commit SHA
last_checked_issue_number = None  # To track the last checked issue number

while True:
    # Check for new commits
    last_commit_data = recive_last_data(REPO_URL_API, GITHUB_TOKEN)
    if last_commit_data and last_commit_data['sha'] != last_checked_sha:
        last_checked_sha = last_commit_data['sha']  # Update the last checked SHA
        save_json_to_file(last_commit_data, 'commit_data.json')  # Save commit data to a JSON file
        print(f"New commit detected and data saved to 'commit_data.json'")
        commit_info = extract_commit_info(last_commit_data)  # Extract commit details
        telegram_message = format_commit_message(commit_info)  # Format the commit message
        response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)  # Send the commit message to Telegram
        if response.status_code == 200:
            print("Commit message sent to Telegram channel")
        else:
            print(f"Failed to send commit message: {response.status_code}")

    # Check for new issues
    last_issue_data = recive_last_data(REPO_URL_ISSUES, GITHUB_TOKEN)
    if last_issue_data and last_issue_data['number'] != last_checked_issue_number:
        last_checked_issue_number = last_issue_data['number']  # Update the last checked issue number
        save_json_to_file(last_issue_data, 'issue_data.json')  # Save issue data to a JSON file
        print(f"New issue detected and data saved to 'issue_data.json'")
        issue_info = extract_issue_info(last_issue_data)  # Extract issue details
        telegram_message = format_issue_message(issue_info)  # Format the issue message
        response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)  # Send the issue message to Telegram
        if response.status_code == 200:
            print("Issue message sent to Telegram channel")
        else:
            print(f"Failed to send issue message: {response.status_code}")

    # Wait for a specific amount of time before checking again (e.g., 60 seconds)
    time.sleep(60)  # Pause for 60 seconds between checks