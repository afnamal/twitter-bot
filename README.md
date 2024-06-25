 Fenerbahçe Twitter Bot

This project contains a Twitter bot that posts random tweets about Fenerbahçe at specific intervals. The bot uses the OpenAI GPT-3.5-turbo model to generate tweets on specific topics and automatically posts these tweets to your Twitter account.

## Features

- The bot is triggered by GitHub Actions every hour.
- It waits for a random period (0-15 minutes) before posting a tweet.
- Tweets are generated using randomly selected prompts based on predefined topics.
- Tweets are posted to Twitter using OpenAI API and Tweepy.

## Installation

### Requirements

- Python 3.x
- OpenAI API key
- Twitter API keys (Bearer Token, Consumer Key, Consumer Secret, Access Token, Access Token Secret)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/username/twitter-bot.git
   cd twitter-bot

    Install the required Python packages:

    bash

python -m pip install --upgrade pip
pip install -r requirements.txt

Define your API keys in a .env file:

plaintext

OPENAI_API_KEY=your_openai_api_key
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_CONSUMER_KEY=your_twitter_consumer_key
TWITTER_CONSUMER_SECRET=your_twitter_consumer_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

Run the bot:

bash

    python twitter_bot.py

Automatic Execution with GitHub Actions

    Push this project to GitHub.

    Go to Settings > Secrets and variables > Actions in your GitHub repository and add the following secrets:
        OPENAI_API_KEY
        TWITTER_BEARER_TOKEN
        TWITTER_CONSUMER_KEY
        TWITTER_CONSUMER_SECRET
        TWITTER_ACCESS_TOKEN
        TWITTER_ACCESS_TOKEN_SECRET

    Set the content of .github/workflows/twitter-bot.yml to the following:

    yaml

    name: Twitter Bot

    on:
      schedule:
        - cron: '0 * * * *' # Runs at the beginning of every hour
      push:
        branches:
          - master

    jobs:
      run-bot:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
          uses: actions/checkout@v2

        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: Run the bot with random delay
          run: |
            python twitter_bot.py
          env:
            OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
            TWITTER_BEARER_TOKEN: ${{ secrets.TWITTER_BEARER_TOKEN }}
            TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
            TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
            TWITTER_ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
            TWITTER_ACCESS_TOKEN_SECRET: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}

This configuration will trigger the bot at the beginning of every hour and post a tweet after waiting for a random period.
Technologies Used

    OpenAI
    Tweepy
    GitHub Actions

Twitter Account

This bot generates and posts tweets for the MourinhoKoc Twitter account.
License

This project is licensed under the MIT License. See the LICENSE file for more details.




This `README.md` file provides detailed information about your project, how to set it up, and how to run it. It also includes a link to the Twitter account where the bot posts tweets.
