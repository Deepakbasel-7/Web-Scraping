import requests
from bs4 import BeautifulSoup

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
            print("Match:", a_tag.text)


            # Finding the corresponding <div> tag with class 'text-gray' and print its text content
            div_sibling = a_tag.find_next_sibling('div', class_='text-gray')
            if div_sibling:
                print("Location:", div_sibling.text.strip())
            else:
                print("Location: Not found")


            # Finding the corresponding <div> tag with class 'cb-text-upcoming' and print its text content for date
            date_div = a_tag.find_next('a', class_='cb-text-upcoming')
            if date_div:
                print("Date:", date_div.text.strip())


            # Finding the corresponding <div> tag with class 'schedule-time' and print its text content for time
            time_div = a_tag.find_next('div', class_='cb-text-upcoming')
            if time_div:
                print("Time:", time_div.text.strip())


            print()  # Prints an empty line for better readability between matches


