import csv
import requests
from bs4 import BeautifulSoup


url = 'https://www.google.com/'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
html = requests.get(url, headers={'User-Agent': ua}).text


def scrap():

    tree = BeautifulSoup(html, 'html.parser')  # parse HTML

    with open('results.csv', 'w', newline='') as csv_f:

        '''
        Write our columns.

        Example: fieldnames = ['id', 'title', 'price', 'phone']
        '''
        fieldnames = []
        csv_w = csv.DictWriter(csv_f, fieldnames=fieldnames, delimiter=',')
        csv_w.writeheader()

        '''
        Scraping logic goes here. Use csv_w.writerow() to write to csv.

        Example:
        csv_w.writerow({'id': str(i),
                        'title': title,
                        'price': price,
                        'phone': phone})
        '''


if __name__ == '__main__':
    scrap()
