from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://rentberry.com/de/apartments/s/cologne-germany?page=11&sort=relevance"
page = requests.get(url)

pasta = BeautifulSoup(page.content, 'html.parser')
lists = pasta.find_all('div', class_="apt-card-wrapper")

with open('housing.csv', 'w', encoding = 'utf8', newline ='') as f:
    thewriter = writer(f)
    header = ['Title', 'Address', 'Price', 'Area', 'Bathrooms', 'Bedrooms']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('div', class_= "apt-name").text
        address = list.find('div', class_= "apt-address").text
        price = list.find('span', class_= "price").text
        area = list.find('span', class_= "space").text.replace('\xa0', ' m²')
        bathrooms = list.find('span', class_= "bathrooms").text.replace('\xa0', ' ')
        bedrooms = list.find('span', class_= "bedrooms").text.replace('\xa0', ' ')
        
        info = [title, address, price, area, bathrooms, bedrooms]
        thewriter.writerow(info)

