def normalize_price(price_str):
    try:
        # Remove non-numeric, parse int
        return int(''.join(filter(str.isdigit, price_str)))
    except:
        return None

def filter_by_price(products, limit):
    if limit is None:
        return products
    return [p for p in products if normalize_price(p['price']) <= limit]
