import requests
from bs4 import BeautifulSoup
import csv

def main_process():
        URL = "http://www.values.com/inspirational-quotes"
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html5lib')

        quotes = []  # a list to store quotes

        table = soup.find('div', attrs={'id': 'portfolio'})

        for row in table.findAll('div', attrs={'class': 'portfolio-image'}):
            quote = {}
            quote['theme'] = str(row.text)
            quote['url'] = str(row.a['href'])
            quote['img'] = str(row.img['src'])
            # quote['lines'] = row.h6.text
            # quote['author'] = row.p.text
            print('process..........')
            quotes.append(quote)

        filename = 'inspirational_quotes.csv'
        with open(filename, 'w') as f:
            #w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
            w = csv.DictWriter(f, ['theme', 'url', 'img'])
            try:
                w.writeheader()
            except Exception as es:
                print(str(es))
            for quote in quotes:
                try:
                    w.writerow(quote)
                except Exception as e:
                    print(str(e))

if __name__ == '__main__':
    main_process()



