import openai
import os
from dotenv import load_dotenv

# Load .env file variables into environment
load_dotenv()

API_KEY = os.environ.get("PERPLEXITY_API_KEY")
print("PERPLEXITY_API_KEY:", API_KEY)   # Should show key (or first few chars for security)

client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.perplexity.ai"
)

def parse_query(user_query: str) -> dict:
    prompt = f"""
    Analyze the following user query and output JSON with:
    - intent: (product_search, flight_search, price_comparison)
    - keywords: [main search terms]
    - price_limit: (numeric, if mentioned)
    - from_city: (for flights)
    - to_city: (for flights)
    - target_sites: [e.g., amazon, flipkart, makemytrip, etc.]
    User query: "{user_query}"
    """
    response = client.chat.completions.create(
        model="sonar-small-online",
        messages=[{"role": "system", "content": prompt}]
    )
    import json
    content = response.choices[0].message.content
    try:
        json_str = content[content.find('{'):content.rfind('}')+1]
        info = json.loads(json_str)
    except Exception:
        info = {}
    return info
