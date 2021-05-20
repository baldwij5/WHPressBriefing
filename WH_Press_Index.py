from os.path import join
from bs4 import BeautifulSoup
import re
import pandas as pd
import glob

INDEX_PAGES_DIR = 'index-pages'

# get the text
# some_filename = join(INDEX_PAGES_DIR, '0.html')
# with open(some_filename, 'r') as rf:
#     txt = rf.read()
# parse the HTML

# create function to extract date


def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)


title = []
date = []
url = []

# soup = BeautifulSoup(txt, 'lxml')
# extract the URLs

for fname in glob.iglob(r'index-pages\*.html'):
    print(fname)
    with open(fname, 'r') as rf:
        txt = rf.read()
    # parse the HTML
    soup = BeautifulSoup(txt, 'lxml')
    for h in soup.find_all('h2'):
        a = h.find('a')
        if a is None:
            continue
    # print(a)
    # print(a.contents)
    # print(a.contents[0])
    # print(a.attrs['href'])
    # print(a.attrs['class'])
    # print(row.find_all('a')[0].contents)
    # print(extract_date(a.attrs['href']))
        for i in extract_date(a.attrs['href']):
            year = i[0]
            month = i[1]
            day = i[2]
            date_of = month + '/' + day + '/' + year
            print(date_of)
            date.append(date_of)
        url.append(a.attrs['href'])
        title.append(a.contents[0].strip())

print(url)
print(title)
print(date)

data = {'Title': title, 'Date': date, 'url': url}
df = pd.DataFrame(data)
print(df)

df.to_csv(r'Desktop\\test.csv')
