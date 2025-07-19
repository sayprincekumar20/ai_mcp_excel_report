from bs4 import BeautifulSoup

def extract_flights(html):
    soup = BeautifulSoup(html, "html.parser")
    flights = []
    for flight in soup.select('.some-flight-card-selector'):
        airline = flight.select_one('.airlineName')
        times = flight.select_one('.flightTimes')
        price = flight.select_one('.flightPrice')
        if not airline or not times or not price:
            continue
        flights.append({
            'airline': airline.text.strip(),
            'times': times.text.strip(),
            'price': price.text.strip().replace('₹','').replace(',',''),
        })
    return flights
