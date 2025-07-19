from app.llm_interface import parse_query
from app.mcp_client import MCPClient
from app.extractors.amazon import extract_amazon_products
from app.extractors.flipkart import extract_flipkart_products
from app.extractors.flights import extract_flights
from app.excel_report import save_to_excel
from app.utils import filter_by_price

def run(user_query):
    # Step 1: LLM processing
    params = parse_query(user_query)
    intent = params.get('intent')
    sheets_data = {}

    if intent == 'product_search' or intent == 'price_comparison':
        # For each site
        if 'amazon' in params.get('target_sites', []):
            mcp = MCPClient()
            mcp.navigate("https://www.amazon.in/")
            mcp.type("#twotabsearchtextbox", ' '.join(params['keywords']))
            mcp.click(".nav-search-submit")
            mcp.scroll()
            html = mcp.get_html()
            products = extract_amazon_products(html)
            products = filter_by_price(products, params.get('price_limit'))
            sheets_data['Amazon'] = products
            mcp.close()
        
        if 'flipkart' in params.get('target_sites', []):
            mcp = MCPClient()
            mcp.navigate("https://www.flipkart.com/")
            mcp.type("input[name='q']", ' '.join(params['keywords']))
            mcp.click("button[type='submit']")
            mcp.scroll()
            html = mcp.get_html()
            products = extract_flipkart_products(html)
            products = filter_by_price(products, params.get('price_limit'))
            sheets_data['Flipkart'] = products
            mcp.close()
    
    elif intent == 'flight_search':
        mcp = MCPClient()
        mcp.navigate('https://www.makemytrip.com/flights/')
        # Add further detailed automation for date/cities as per MCP, selectors and sequence
        # Fill source, destination, pick date, submit
        mcp.type("input#fromCity", params['from_city'])
        mcp.type("input#toCity", params['to_city'])
        mcp.click("button.search-btn")
        mcp.scroll()
        html = mcp.get_html()
        flights = extract_flights(html)
        sheets_data['Flights'] = flights
        mcp.close()

    # Step 5: Generate Excel Report
    excel_name = 'report.xlsx'
    save_to_excel(sheets_data, excel_name)
    print(f"Report saved to {excel_name}")

if __name__ == "__main__":
    user_q = input("Enter your query: ")
    run(user_q)
