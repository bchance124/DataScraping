import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_winning_players'
response = requests.get(url)

# Use Beautiful Soup to parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table of World Cup winning players and iterate over its rows
table = soup.find('table', {'class': 'wikitable'})
for row in table.find_all('tr')[1:]:
    # Extract the player's name and World Cup winning team
    cells = row.find_all('th')
    name = cells[0].text.strip()
    team = cells[1].text.strip()

    # Print the player's name and winning team
    print(f'{name} - {team}')