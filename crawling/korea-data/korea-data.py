import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    URL = 'https://kdx.kr/data/view/32007'

    soup = BeautifulSoup(urlopen(URL), 'html.parser')

    print(soup)

if __name__ == '__main__':
    main()