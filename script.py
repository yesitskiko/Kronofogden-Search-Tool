import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

cookies = {}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://auktion.kronofogden.se',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://auktion.kronofogden.se/auk/w.objectlist?inC=KFM&inA=WEB',
    'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('inC', 'KFM'),
    ('inA', 'WEB'),
)

Results = []

inpt = input("Skriv fraser: ")
words = inpt.split(", ")
if len(words) == 0:
  words.insert(0, inpt)
for Index, Word in enumerate(words):
  data = {
    'inCategoryId': '',
    'inPageNo': '1',
    'inSearchCrit': '0',
    'inSiteLang': '',
    'inSelectedSort': '',
    'inSearchText': str(Word)
  }

  response = requests.post('https://auktion.kronofogden.se/auk/w.objectlist', headers=headers, params=params, cookies=cookies, data=data)
  if response.text.find('Tyvärr så gav din sökning på "{0}" inga träffar just nu!'.format(Word)) > -1:
    print(Word, "existerar inte i kronofogdens marknad.")
  else:
    soup = BeautifulSoup(response.content, 'html.parser')
    for Index, Item in enumerate(list(list(list(list(soup.children)[1].children)[1])[0])[11]):
      Item  = list(list(Item.children)[0])
      Items = list(Item[2])[0]
      if not(len(list(Items)) > 3): 
        Val = list(list(Items)[2])[0]
        TId = list(Val)[1].text
        Name = list(Val)[2]
        if Name == " ":
          Name = "{0}{1}".format(list(Val)[3].text, list(Val)[4])
        for _, Val2 in enumerate(list(Val)):
          if str(Val2).find("Utrop") > -1:
            Results.insert(0, [ Word, TId[0:-1], Name, list(Val2)[len(list(Val2)) - 1].text])
        continue
      for Idx, Val in enumerate(list(Items)[3]):
        TId = list(Val)[1].text
        Name = list(Val)[2]
        if Name == " ":
          Name = "{0}{1}".format(list(Val)[3].text, list(Val)[4])
        for _, Val2 in enumerate(list(Val)):
          if str(Val2).find("Utrop") > -1:
            Results.insert(0, [ Word, TId[0:-1], Name, list(Val2)[len(list(Val2)) - 1].text])

print(tabulate(Results, headers=["Sökord", "Id", "Namn", "Högsta Bud"], tablefmt='orgtbl'))
