# AI-Powered Python Application for Natural Language E-Commerce and Flight Data Extraction

## Overview

This application processes natural-language user queries—such as product searches, flight price requests, or price comparisons across sites—and produces comprehensive Excel reports with all relevant data. It combines advanced AI for understanding user intent and the Model Context Protocol (MCP) for multi-site, browser-driven automation and data extraction.

---

## Key Features

- **Natural Language Query Processing**  
  Handles a wide range of query types, including product searches, flight price lookups, and multi-site price comparisons.

- **MCP Browser Automation**  
  Employs Playwright or Selenium with MCP for precise, scriptable browser control—covering navigation, form filling, and dynamic content interaction.

- **Multi-Site Scraping**  
  Extracts rich, structured data from Amazon, Flipkart, leading travel sites, and more.

- **Excel Report Generation**  
  Produces Excel files with dynamic sheets, filterable data tables, tailored summary analysis, and visually engaging charts for any supported query.

---

## Architecture

### 1. AI Query Interpretation

- Uses OpenAI, Anthropic, or local LLMs to parse each user query.
- Determines:
  - Query intent (product search, flight booking, price comparison)
  - Target websites (Amazon, Flipkart, travel portals)
  - Search parameters (item, price, location, dates, etc.)

### 2. Automated Browser Workflows

- Scriptable, human-like automation using MCP:
  - Navigation to relevant pages
  - Search form and filter interactions (typing, selecting, submitting)
  - Dynamic content handling (scrolling, AJAX, pagination)
  - Error handling (popups, CAPTCHAs, failures)

### 3. Data Extraction & Aggregation

- Structured scraping into Python objects:
  - **Product data:** Title, price, image, rating, reviews, features, direct link
  - **Flight data:** Airline, routes, dates, prices, booking links
  - **Multi-site:** Standardizes and merges similar fields across platforms

### 4. Excel Report Generation

- Uses `pandas`, `openpyxl`, and/or `xlsxwriter` to:
  - Create a worksheet for each query/site
  - Populate structured, filterable data tables
  - Generate analytics and charts (price distributions, comparisons)
  - Organize output by site, product, or flight route

---

## Workflow Examples

### A. Product Search (e.g., "Find me laptops under ₹50,000")

1. User enters query.
2. LLM parses for product search: `"laptop"`, price ≤ ₹50,000, sites: Amazon, Flipkart.
3. Browser automation steps:
    - Navigate to Amazon/Flipkart
    - Fill search bar, apply price filter, extract results
    - Repeat per site
4. Aggregation and normalization of listings.
5. Excel report:
    - Sheets: "Amazon", "Flipkart"
    - Columns: Title, Price, Rating, Reviews, Link, Features
    - Summary charts: Price range, top brands

---

### B. Flight Price Lookup (e.g., "What's the price of ticket from Bangalore to SF")

1. LLM identifies flight search: "Bangalore" to "SF," targets travel sites.
2. Browser automation:
    - Go to MakeMyTrip
    - Complete flight search (cities, dates)
    - Extract flight results
3. Data extraction: airline, timings, layovers, prices, booking options
4. Excel sheet with sortable/filterable results and price trend charts

---

### C. Multi-Site Price Comparison (e.g., "Compare AirPods prices on different sites")

1. LLM parses for comparison: Product = AirPods, sites = Amazon, Flipkart, Croma.
2. Perform and extract product search from each site.
3. Merge and normalize results.
4. Excel sheet(s) with product rows and price columns for each site, with a summary comparison chart.

---

## Technical Components

**Core Python Modules:**

- LLMs: `openai`, `anthropic`, or local `transformers`
- MCP Automation: `mcp-playwright`, `selenium-mcp`, or REST MCP
- Data Extraction: `BeautifulSoup`, `lxml`, `pandas`
- Excel Generation: `openpyxl`, `xlsxwriter`, `pandas`
- Visualization: `matplotlib`, `seaborn`

**Example MCP Commands:**

- `browser_navigate('https://www.amazon.in')`
- `browser_type('#searchBox', 'laptop')`
- `browser_click('.price-filter')`
- `browser_scroll('.results-list')`
- `browser_snapshot()`

---

## Error Handling

- Automatic dialog/alert closures
- CAPTCHA and site-block detection
- Retry and fallback logic for partial failures

---

## Example Directory Structure
project-root/

├── app/

│ ├── llm_interface.py

│ ├── mcp_client.py

│ ├── extractors/

│ │ ├── amazon.py

│ │ └── flipkart.py

│ ├── excel_report.py

│ ├── main.py

│ └── utils.py

├── requirements.txt

├── README.md

├── MCP_AUTOMATION.md

├── WORKFLOW_EXAMPLES.md

└── samples/

├── laptops_under_50K.xlsx

├── bangalore_to_sf_flights.xlsx

└── airpods_prices_comparison.xlsx



---

## Sample Output (Excel Reports)

- **Products:**  
  Columns: Name, Price, Rating, Review Count, Features, Shop, Product Link
- **Flights:**  
  Columns: Airline, Departure, Arrival, Duration, Stops, Price, Booking Link
- **Analytics:**  
  Price distribution, best-rated options, cross-site comparison charts

---

## Setup Requirements

- Python 3.8+
- Dependencies: `openai`, `anthropic`, `python-dotenv`, `beautifulsoup4`, `lxml`, `pandas`, `openpyxl`, `playwright`, etc. (see `requirements.txt`)
- LLM access: OpenAI or Anthropic API key, or working local model
- Full user/developer documentation:  
  - Setup, use: `README.md`  
  - Browser automation: `MCP_AUTOMATION.md`  
  - Sample workflows: `WORKFLOW_EXAMPLES.md`

---

## Performance and Extensibility

- Modular, extensible design—easy to add new sites and query types
- Advanced prompt and error handling for robust results
- Dynamic, instantly actionable Excel reports with analytics, filters, and sorting

---

This application provides a rapid, intelligent solution for extracting, analyzing, and reporting e-commerce and travel data, empowering users with rich Excel outputs for any supported natural-language query.

