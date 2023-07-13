# pip install bs4
# pip install python

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def test():
    page_to_scrape = requests.get("http://people.mjc.edu")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    
    name = soup.findAll("a", attrs = {"class":"lnkName"})
    
    title = soup.findAll("span", attrs = {"class":"lblTitle"})
    
    email = soup.findAll("a", attrs = {"class":"lnkEmail"})
    
    with open("MODESTO.csv", "w", encoding='utf-8') as file:
    
        writer = csv.writer(file)
        writer.writerow(["NAME","TITLE","EMAIL"])
        
        for name,title,email in zip(name,title,email):
            writer.writerow([name.text, title.text, email.text])
            
        file.close()
        df = pd.read_csv("MODESTO.csv")
        print(df)
    
    
    
    
    
if __name__ == "__main__":
    test()