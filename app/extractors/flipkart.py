from bs4 import BeautifulSoup

def extract_flipkart_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for item in soup.select('div._2kHMtA'):
        title = item.select_one('div._4rR01T')
        price = item.select_one('div._30jeq3')
        link = item.select_one('a')
        rating = item.select_one('div._3LWZlK')
        if not title or not price or not link:
            continue
        products.append({
            'title': title.text.strip(),
            'price': price.text.strip().replace('₹','').replace(',',''),
            'rating': rating.text if rating else '',
            'link': 'https://www.flipkart.com'+link['href']
        })
    return products
