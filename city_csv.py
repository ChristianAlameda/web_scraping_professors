# pip install bs4
# pip install python

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests_html import HTMLSession
from selenium import webdriver

import html5lib
import urllib.request
import time
import requests
import csv
import pandas as pd
import lxml




def create_for_modesto():
    page_to_scrape = requests.get("http://people.mjc.edu/list.aspx")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    print(soup)
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
    
def create_for_merced():
    url_list = ["https://www.mccd.edu/directory/"]
    for i in range(2,52):
        url_list.append('https://www.mccd.edu/directory/page/'+str(i)+'/')
    url_list.append('https://www.mccd.edu/directory/page/52/#item_list')
    
    #NEED A USER AGENT
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    for url in url_list:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        page_to_scrape = requests.get(url, headers=headers)

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        name = soup.findAll("h2",attrs = {"class":"people_item_name"})
        
        title = soup.findAll("div", attrs = {"class":"people_item_title"})
        
        division = soup.findAll("div", attrs = {"class":"people_item_division"})
        
        phone_email_school = soup.findAll("span", attrs = {"class":"people_item_detail_info_label"})

        #phone = soup.findAll("span", attrs = {"class":"people_item_detail_info_label"})
        """
        0      \r\n\t\t\t\tRebecca J Abarca\r\n\t\t\t          Professor of Radiologic Technology  \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tAllied Health\...                 209-384-6535
        1  \r\n\t\t\t\tDeanna M Abbruzzetti\r\n\t\t\t  Administrative Assistant to Vice President  \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHuman Resource...      rebecca.abarca@mccd.edu
        2       \r\n\t\t\t\tMatthew D Adams\r\n\t\t\t                              Security Guard  \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSecurity & Saf...                Merced Campus
        """
        
        phone = []
        email = []
        college = []
        for i in range(3,len(phone_email_school),3):
            phone.append(phone_email_school[i-3])
            email.append(phone_email_school[i-2])
            college.append(phone_email_school[i-1])
        
        with open("MERCED.csv", "a", encoding='utf-8') as file:
        
            writer = csv.writer(file)
            writer.writerow(["NAME","TITLE","DIVISION","PHONE","EMAIL","COLLEGE"])
            
            for name,title,division,phone,email,college in zip(name,title,division,phone,email,college):
                writer.writerow([name.text, title.text, division.text, phone.text, email.text, college.text])
                
    file.close()
    df = pd.read_csv("MERCED.csv")
    print(df)
    
    
    
if __name__ == "__main__":
    create_for_merced()