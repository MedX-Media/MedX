# GitHub to Telegram Notification Bot

This Python script monitors a specified GitHub repository for new commits and issues and sends notifications to a designated Telegram channel. It uses the GitHub API to retrieve the latest data and the Telegram Bot API to send formatted messages to the channel.

## Features

- **Commit Monitoring**: The script checks for the latest commit in the repository, extracts relevant details, and sends a formatted notification to the Telegram channel.
- **Issue Monitoring**: The script checks for new issues, extracts important details, and sends a formatted notification to the Telegram channel.
- **Continuous Monitoring**: The script runs in a loop, checking for new data at regular intervals (e.g., every 60 seconds).

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- GitHub Personal Access Token with access to the repository you want to monitor.
- Telegram Bot Token and Channel Chat ID to send notifications.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo-url
    ```

2. **Install Required Packages**: Make sure you have the necessary Python packages installed. You can install them using:
    ```bash
    pip install requests
    ```

3. **Update Configuration**: Replace the following placeholders in the script with your actual tokens and IDs:
    - `BOT_TOKEN`: Your Telegram bot token.
    - `CHANNEL_CHAT_ID`: The chat ID of your Telegram channel.
    - `GITHUB_TOKEN`: Your GitHub personal access token.
    - `REPO_URL_API`: The API URL for commits in your GitHub repository.
    - `REPO_URL_ISSUES`: The API URL for issues in your GitHub repository.

4. **Run the Script**:
    ```bash
    python script_name.py
    ```

## Script Overview

- **Functions**:
    - `recive_last_data(api_url, github_token)`: Fetches the latest data (commit or issue) from the GitHub API.
    - `save_json_to_file(data, filename)`: Saves JSON data to a file.
    - `extract_commit_info(commit_data)`: Extracts important details from commit data.
    - `extract_issue_info(issue_data)`: Extracts important details from issue data.
    - `escape_markdown(text)`: Escapes special characters for proper formatting in Telegram.
    - `format_commit_message(info)`: Formats commit details into a message suitable for Telegram.
    - `format_issue_message(info)`: Formats issue details into a message suitable for Telegram.
    - `send_tel(mess, bot_token, chat_id)`: Sends the formatted message to the specified Telegram channel.

- **Main Loop**: The script runs an infinite loop, checking for new commits and issues every 60 seconds. If new data is detected, it is processed and sent to the Telegram channel.

## Usage Notes

- **Markdown Formatting**: The script uses Telegram's Markdown formatting. If you encounter issues with special characters, ensure they are properly escaped using the `escape_markdown` function.
- **Timing**: You can adjust the `time.sleep(60)` duration to change how often the script checks for updates.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bug fixes.

## Disclaimer

Ensure that your GitHub token and Telegram bot token are kept secure. Avoid sharing them publicly to prevent unauthorized access.

