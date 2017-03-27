import urllib2
import pandas as pd
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib2.urlopen(wiki)

soup = BeautifulSoup(page,"lxml")
soup.table
#print(soup.prettify())
#for link in soup.find_all('a'):
    #print link.get('href')
right_table = soup.find('table', class_='wikitable sortable plainrowheaders')
#print right_table

a = []
b = []
c = []
d = []
e = []
f = []
g = []

for row in right_table.find_all("tr"):
    #print type(row)
    cells = row.find_all('td')
    states = row.find_all('th')

    if len(cells) == 6:
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))
        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True))
        e.append(cells[3].find(text=True))
        f.append(cells[4].find(text=True))
        g.append(cells[5].find(text=True))

df = pd.DataFrame(a,columns=['Number'])
df['State/UT'] = b
df['Admin_Capital'] = c
df['Legislative_Capital'] = d
df['Judiciary_capital'] = e
df['Year_Capital'] = f
df['Former_Capital'] = g

print df

        
