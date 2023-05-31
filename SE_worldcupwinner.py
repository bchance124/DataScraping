from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch a new instance of Firefox browser
browser = webdriver.Firefox()

# Navigate to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_winning_players'
browser.get(url)

# Find the table of World Cup winning players and iterate over its rows
table = browser.find_element(By.CLASS_NAME, 'wikitable')
for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:
    # Extract the player's name and World Cup winning team
    cells = row.find_elements(By.TAG_NAME, 'th')
    name = cells[0].text.strip()
    team = cells[1].text.strip()

    # Print the player's name and winning team
    print(f'{name} - {team}')

# Close the browser window
browser.quit()