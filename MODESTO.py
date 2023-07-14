# pip install bs4
# pip install python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
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
    
    
def test1():
    with requests.Session() as session:
        page_number = 1
        url = "http://people.mjc.edu"
        while True:
            print("Processing page: #{page_number}; url: {url}".format(page_number=page_number, url=url))
            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            #VARIABLES WE ARE COLLECTING: (NAME, TITLE, EMAIL, SCHOOL) // SCHOOL == Modesto Junior College
            name = soup.findAll("a", attrs = {"class":"lnkName"})
            title = soup.findAll("span", attrs = {"class":"lblTitle"})
            email = soup.findAll("a", attrs = {"class":"lnkEmail"})
            
            #ADDING TO THE MODESTO FILE EVERYTIME WE GO TO THE NEXT PAGE
            with open("MODESTO.csv", "w", encoding='utf-8') as file:
            
                writer = csv.writer(file)
                writer.writerow(["NAME","TITLE","EMAIL","SCHOOL"])
                
                school = 'Modesto Junior College'
                for name,title,email in zip(name,title,email):
                    writer.writerow([name.text, title.text, email.text, school])
                    
                file.close()
                df = pd.read_csv("MODESTO.csv")
                print(df)
            
            # CHECK IF THERE IS A NEXT BUTTON, IF SO CONTINUE IF NOT BREAK THE LOOP
            #href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$lnkNext','')"
            #id="ctl00_ContentPlaceHolder1_lnkNext"
            next_link = soup.findAll("a", attrs = {"id":"next", "href":"javascript:__doPostBack('ctl00$ContentPlaceHolder1$lnkNext','')"})
            print(next_link)# RETURNS NONE
            if next_link is None:
                break
            
            #urllib.parse.urljoin(base, url, allow_fragments=True)
            #javascript:__doPostBack('ctl00$ContentPlaceHolder1$lnkNext','')
            url = urljoin(url, next_link["href"])
            page_number += 1

    print("Done.")
    
    
if __name__ == "__main__":
    test1()