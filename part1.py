import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
headers = {
    'Origin': 'https://www.amazon.in',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')




product_names = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
urls = soup.find_all('a', class_='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
review_and_rating = soup.find_all('div', class_='a-row a-size-small')
prices = soup.find_all('div', class_='a-section a-spacing-none a-spacing-top-micro s-price-instructions-style')

# Open a CSV file for writing
with open('20_products.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    
    csvwriter = csv.writer(csvfile) # Create a CSV writer
    csvwriter.writerow(["URL", "Name", "Price", "Rating", "Review"]) # Write the header row

    for i in range(20):
        product_url = "https://amazon.in" + urls[i].attrs['href'] 
        product_price = prices[i].select_one('.a-price-whole').text
        product_name = product_names[i].text
        product_rating = review_and_rating[i].text[:3]
        product_review = review_and_rating[i].select_one('.s-underline-link-text').text
        
        csvwriter.writerow([product_url, product_name, product_price, product_rating, product_review])
    csvfile.close()    

print('Done. Data saved to 20_products.csv')
