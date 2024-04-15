import requests
from bs4 import BeautifulSoup
import sqlite3


#Connect the database
conn= sqlite3.connect('ipl_matches.db')
cursor= conn.cursor()


#Creating the table
cursor.execute('''CREATE TABLE IF NOT EXISTS matches
               (match VARCHAR, location TEXT, date VARCHAR)''')
conn.commit()


# Getting the HTML
url = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches"
response = requests.get(url)
if response:
    print("Connection Successful!")
    print()
else:
    print("Connection Lost!")

htmlContent = response.text


# Parsing the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')



# Getting the Header
h1_tag = soup.find('h1')
if h1_tag:
    print(h1_tag.text)
    print()
  
else:
    print('Nothing to show!')
    print()
 


# Finding all <a> tags with class 'text-hvr-underline' and print their text content
anchors = soup.find_all('a', class_='text-hvr-underline')
if not anchors:
    print("No anchor tags found with class 'text-hvr-underline'!!")
else:
    for a_tag in anchors[:-2]:
        if 'text-hvr-underline' in a_tag.get('class', []):
            match = a_tag.text
            location_div = a_tag.find_next_sibling('div', class_='text-gray')
            if location_div:
                location = location_div.text.strip()
            else:
                location = "Not found"
            date_div = a_tag.find_next('a', class_='cb-text-upcoming')
            if date_div:
                date = date_div.text.strip()
            else:
                date = "Not found"



# Inserting the scraped data
            cursor.execute("INSERT INTO matches (match, location, date) VALUES (?, ?, ?)",
                           (match, location, date))
            print("Inserted:", match, location, date)
            print()


#Commit changes and close

conn.commit()
conn.close()






