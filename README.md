# 📰 Article To Tweet

A Streamlit-powered web app that summarizes articles from URLs and converts the summary into social media-friendly content (e.g., tweets) using an AI language model.

## Features

- URL-based article summarization: Input a URL, and the app fetches the article, cleans it, and provides a summary.
- Social media post generation: Summaries are under 250 characters and formatted to be used as social media posts.
- AI-powered: Uses an AI language model to generate summaries and tweets.

## Tech Stack

- Streamlit
- LangChain
- dotenv
- Python

## Installation

### Prerequisites

- Python 3.7+
- API Key for the language model (LangChain)

## How to Use

Input a valid article URL into the text input field.
Click "Submit" to scrape and summarize the article.
View the summary formatted as a social media post in markdown.
