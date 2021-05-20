import requests
from os import makedirs
from os.path import join
from bs4 import BeautifulSoup

URL_ENDPOINT = 'https://www.whitehouse.gov/briefing-room/page/%s/'
MAX_PAGE_NUM = 100
INDEX_PAGES_DIR = 'index-pages'
makedirs(INDEX_PAGES_DIR, exist_ok=True)

for pagenum in range(1, MAX_PAGE_NUM):
    resp = requests.get(
        'https://www.whitehouse.gov/briefing-room/page/%s/' % pagenum)
    print("Downloaded", resp.url)

    fname = join(INDEX_PAGES_DIR, '{}.html'.format(pagenum))
    print("Saving to", fname)
    with open(fname, "w") as wf:
        wf.write(resp.text)
