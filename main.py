import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# total 220

req = requests.get("https://trends.builtwith.com/analytics/country/Cambodia").content.decode("utf-8")

soup = BeautifulSoup(req,"html.parser")

table = soup.find(lambda tag: tag.name =='table')
heads = table.findAll(lambda tag:tag.name == 'thead')
tbody = table.find(lambda tag: tag.name == 'tbody')
rows = tbody.findAll(lambda tag:tag.name == 'tr')


headers = heads[0]
child_links = []
technologies= []

# store child link
for row in rows:
    a = 'https:'+ row.findAll(lambda tg: tg.name == 'a')[-1]['href']
    child_links.append(a)

# store technology
for idx,row in enumerate(rows):
        for col in row:
            if col.text.strip() == '': continue
            text =col.text.strip()
            technologies.append(text)
            break
        


# create csv for parent info

with open('./result/main.csv','w') as file:
    for head in headers:
        file.write(head.text.strip())

    file.write(' child_link\n')

with open('./result/main.csv','a') as file:
    for idx,row in enumerate(rows):
        for col in row:
            if col.text.strip() == '': continue
            text =col.text.strip() +' | '
            file.write(text)
        file.write(child_links[idx])
        file.write('\n\r')




# get information from child detail
# I created child folder for store all child detail within child link
# file format for child detail: technology-details-> Google Analytics-details.csv


for idx,link in enumerate(child_links):
    req2 = requests.get(link).content.decode("utf-8")
    soup2 = BeautifulSoup(req2,"html.parser")

    table2 = soup2.find(lambda tag: tag.name =='table')
    heads2 = table2.findAll(lambda tag:tag.name == 'thead')[0]
    tbody2 = table2.find(lambda tag: tag.name == 'tbody')
    rows2 = tbody2.findAll(lambda tag:tag.name == 'tr')
    
    
    data =[]
    for row in rows2:
        if not headers:
            # Extract table headers
            headers = [cell.get_text(strip=True) for cell in row.find_all('th')]
        else:
            # Extract table data rows
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            data.append(row_data)
    filename = f'result/details/{technologies[idx]}-details.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([th.text.strip() for th in heads2])  # Write headers to the CSV file
        writer.writerows(data)  # Write data rows to the CSV file