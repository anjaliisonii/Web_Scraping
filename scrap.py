import requests 
import webbrowser 
from bs4 import BeautifulSoup
def open_url(URL):
    webbrowser.open(URL)
    html = requests.get(URL) 
    soup = BeautifulSoup(html.content, 'html.parser')
    # print(soup.title)
    table = soup.select_one("div.table-responsive-md table")
    if table:
            headers = [th.text.strip() for th in table.select("thead th")]
            rows = []
            for row in table.select("tbody tr"):
                cells = [td.text.strip() for td in row.find_all(["td", "th"])]
                rows.append(cells)
            # print(headers,rows)
    df=[]
    for i in headers:
            df.append(i)
    df2={}
    i=0
    for col in rows:
            i=0
            df2={}
            while i<len(df):
                    for j in col:
                            df2[df[i]]=j
                            i+=1

            print(df2)

print(open_url("https://www.insiderscreener.com/en/explore/au"))

