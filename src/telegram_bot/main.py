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


def recive_last_data(api_url, github_token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()

    if data:
        return data[0]  # Returning the latest data (commit or issue)
    else:
        return None  # If no data is found, return None


def save_json_to_file(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def extract_commit_info(commit_data):
    important_info = {
        "sha": commit_data.get("sha"),
        "author_name": commit_data["commit"]["author"].get("name"),
        "author_email": commit_data["commit"]["author"].get("email"),
        "message": commit_data["commit"].get("message"),
        "commit_url": commit_data.get("html_url"),
    }
    return important_info


def extract_issue_info(issue_data):
    important_info = {
        "issue_number": issue_data.get("number"),
        "title": issue_data.get("title"),
        "user_login": issue_data["user"].get("login"),
        "state": issue_data.get("state"),
        "labels": [label.get("name") for label in issue_data.get("labels", [])],
        "created_at": issue_data.get("created_at"),
        "updated_at": issue_data.get("updated_at"),
        "issue_url": issue_data.get("html_url"),
        "body": issue_data.get("body", ""),
    }
    return important_info


def escape_markdown(text):
    escape_chars = r"\*_`\[\]()~>#+-=|{}.!"
    return re.sub(r"([%s])" % re.escape(escape_chars), r"\\\1", text)


def format_commit_message(info):
    info["message"] = escape_markdown(info["message"])
    message = (
        "🚀 *New Commit Detected*\n\n"
        "🔗 *SHA:* `{sha}`\n"
        "👤 *Author:* {author_name} ({author_email})\n"
        "📝 *Commit Message:* {message}\n\n"
        "🔍 [View Commit]({commit_url})".format(**info)
    )
    return message


def format_issue_message(info):
    info["body"] = escape_markdown(info["body"])
    labels = ", ".join([escape_markdown(label) for label in info["labels"]])
    message = (
        f"🐞 *New Issue Detected* - "
        f"🔢 *Issue Number:* `{info['issue_number']}`\n\n"
        f"📝 *Title:* {info['title']}\n"
        f"👤 *User:* {info['user_login']}\n"
        f"🏷️ *Labels:* {labels}\n\n"
        f"📅 *Created At:* {info['created_at']}\n"
        f"🔄 *Updated At:* {info['updated_at']}\n\n"
        f"🔗 [View Issue]({info['issue_url']})\n\n"
    )
    return message


def send_tel(mess, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mess,
        "parse_mode": "Markdown",  # Use 'MarkdownV2' if necessary and ensure proper escaping
    }
    response = requests.post(url, data=data)
    return response


# Main loop to continuously check for new issues and commits
last_checked_sha = None
last_checked_issue_number = None

while True:
    # Check for new commits
    last_commit_data = recive_last_data(REPO_URL_API, GITHUB_TOKEN)
    if last_commit_data and last_commit_data["sha"] != last_checked_sha:
        last_checked_sha = last_commit_data["sha"]
        save_json_to_file(last_commit_data, "commit_data.json")
        print(f"New commit detected and data saved to 'commit_data.json'")
        commit_info = extract_commit_info(last_commit_data)
        telegram_message = format_commit_message(commit_info)
        response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)
        if response.status_code == 200:
            print("Commit message sent to Telegram channel")
        else:
            print(f"Failed to send commit message: {response.status_code}")

    # Check for new issues
    last_issue_data = recive_last_data(REPO_URL_ISSUES, GITHUB_TOKEN)
    if last_issue_data and last_issue_data["number"] != last_checked_issue_number:
        last_checked_issue_number = last_issue_data["number"]
        save_json_to_file(last_issue_data, "issue_data.json")
        print(f"New issue detected and data saved to 'issue_data.json'")
        issue_info = extract_issue_info(last_issue_data)
        telegram_message = format_issue_message(issue_info)
        response = send_tel(telegram_message, BOT_TOKEN, CHANNEL_CHAT_ID)
        if response.status_code == 200:
            print("Issue message sent to Telegram channel")
        else:
            print(f"Failed to send issue message: {response.status_code}")

    # Wait for a specific amount of time before checking again (e.g., 60 seconds)
    time.sleep(60)
