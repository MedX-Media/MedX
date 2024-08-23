# Medx Project

## Overview

Medx is a simple Python script designed to monitor a GitHub repository for new commits and automatically send a formatted message with the commit details to a specified Telegram channel. The script continuously checks for new commits, saves the latest commit data to a JSON file, and sends the relevant commit information to Telegram when a new commit is detected.

## Features

- Fetches the latest commit from a specified GitHub repository.
- Extracts and formats important commit details.
- Sends a notification with commit information to a Telegram channel.
- Continuously monitors the repository for new commits.

## Prerequisites

- Python 3.x
- `requests` library: Install via pip if not already installed.
  ```bash
  pip install requests
  ```

## Setup

### 1. Clone the repository (if not done already):
  ```bash
  	git clone https://github.com/MedX-Media/MedX
	cd Medx/src/telegram_bot
  ```
  
### 2. Configuration:
	Replace `<BOT_TOKEN>` with your Telegram bot's token.
	Replace `<CHANNEL_CHAT_ID>` with your Telegram channel's chat ID.
	Replace `<REPO_URL_API>` with the GitHub API URL for the repository's commits (e.g., `https://api.github.com/repos/username/repository/commits`).
	Replace <GITHUB_TOKEN> with your personal GitHub token.

### 3. Run the script:
  ```bash
	python main.py
  ```
  
## Code Explanation

`recive_last_commit_data(repo_url_api, github_token)`

- Fetches the latest commit data from the GitHub API.
- Returns the latest commit data or None if no commits are found.

`save_json_to_file(data, filename)`

- Saves the given data to a specified JSON file.

`extract_important_info(commit_data)`

- Extracts important details from the commit data such as SHA, author name, email, commit message, and commit URL.

`format_message(info)`

- Formats the extracted commit details into a Telegram message format.

`send_tel(mess, bot_token, chat_id)`

- Sends the formatted commit message to the specified Telegram channel.

### Main Loop

- The script runs in an infinite loop, checking the GitHub repository for new commits every 60 seconds.
- If a new commit is detected, it is saved to a JSON file, and a notification is sent to the Telegram channel.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](https://github.com/MedX-Media/MedX/blob/main/LICENSE) file for details.
