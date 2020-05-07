import requests
from bs4 import BeautifulSoup


def readOlxURL(URL):#czyta strone i wyswietla zrodlo


    headers = {
       "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.360'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    cats = soup.find(id = "topLink")

    return cats


def getNazwy(cats):#pobiera nazwy klas
    names = []

    try:
        nazwy = cats.find_all(class_="hidden")
    except:
        return names

    for item in nazwy:
        names.append((str(item).partition("<span>")[2].partition("<")[0]))


    return names

def getLinks(cats):#pobiera linki
    linki = []

    try:
        links = cats.find_all(class_="hidden")
    except:
        return linki

    for item in links:
        linki.append(str(item).partition('href="')[2].partition('">')[0])


    return linki

def addNamesAndLinks(names, links):#laczy tablice

    tab = [["" for x in range(2)] for y in range(len(names))]

    for row in range(len(names)):
        tab[row][0] = names[row]
        tab[row][1] = links[row]

    return tab

def fromStringToTable(URL):


    cats = readOlxURL(URL)
    links = getLinks(cats)
    names = getNazwy(cats)
    tab = addNamesAndLinks(names, links)

    temp = []

    if len(tab) != 0:
        for item in tab:
            temp = temp + fromStringToTable(item[1])
        tab = tab + temp

    return tab




#fromStringToTable("https://www.olx.pl/oferty/")
print(fromStringToTable("https://www.olx.pl/motoryzacja/samochody/"))