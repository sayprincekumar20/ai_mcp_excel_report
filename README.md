# AI-Powered E-Commerce & Flight Data Excel Automation

This Python application lets you process natural language queries (e.g., `"Find me laptops under ₹50,000"`) and automatically generates Excel reports with data extracted from Amazon, Flipkart, and travel sites—driven by AI with Perplexity LLM and browser automation.

---

## Features

- 🚀 **Conversational AI for query interpretation**
- 🧑‍💻 **Browser automation** with Playwright for robust scraping
- 📦 **Multi-site extraction** (Amazon, Flipkart, Flights)
- 📊 **Excel report generation**—filterable, multi-sheet, ready for analysis

---

## Quickstart Guide

### Requirements

- Python 3.8 or newer
- [Perplexity AI API Key](https://www.perplexity.ai/api/keys)
- Google Chrome or Chromium Browser
- Windows, macOS, or Linux

### Installation

1. **Clone the repo (or copy files):**

    ```
    git clone <your-repo-url>
    cd <project-folder>
    ```

2. **Set up Python environment:**

    ```
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Set your Perplexity API key in `.env` file:**

    In your project root, create a file called `.env` with this line (no spaces, no quotes):

    ```
    PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

4. **Install Playwright browser drivers:**

    ```
    python -m playwright install
    ```

---

## Usage

