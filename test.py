# pip install bs4
# pip install python

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def test():
    page_to_scrape = requests.get("http://quotes.toscrape.com")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    
    quotes = soup.findAll("span", attrs = {"class":"text"})
    authors = soup.findAll("small", attrs = {"class":"author"})
    
    with open("write_quotes_authors.csv", "w", encoding='utf-8') as file:
    
        writer = csv.writer(file)
        writer.writerow(["QUOTES","AUTHORS"])
        
        for quote, author in zip(quotes,authors):
            
            for i,j in enumerate(quote):
                if j == "" or j == "":
                    quote[i] = ''
            
            writer.writerow([quote.text, author.text])
        file.close()
        df = pd.read_csv("write_quotes_authors.csv")
        print(df.head(10))
    
if __name__ == "__main__":
    test()