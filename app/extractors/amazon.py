from bs4 import BeautifulSoup

def extract_amazon_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for item in soup.select('.sg-col-4-of-12, .s-result-item'):
        # Simplified extraction logic
        title = item.select_one('h2 span')
        price = item.select_one('.a-price .a-offscreen')
        link = item.select_one('h2 a')
        rating = item.select_one('.a-icon-alt')
        if not title or not price or not link:
            continue
        products.append({
            'title': title.text.strip(),
            'price': price.text.strip().replace('₹','').replace(',',''),
            'rating': rating.text if rating else '',
            'link': 'https://www.amazon.in'+link['href']
        })
    return products
