import requests 
import json
import webbrowser 
from bs4 import BeautifulSoup
def open_url(URL):
    webbrowser.open(URL)
    html = requests.get(URL) 
    soup = BeautifulSoup(html.content, 'html.parser')
    # print(soup.title)
    table = soup.find('table')  
    rows = table.find_all('tr')  

    data = []
    header = [th.text.strip() for th in rows[0].find_all('th')]

    for row in rows[1:]: 
        values = [td.text.strip() for td in row.find_all('td')]
        row_data = dict(zip(header, values))
        data.append(row_data)

    with open('output.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
print(open_url("https://www.insiderscreener.com/en/explore/au"))

