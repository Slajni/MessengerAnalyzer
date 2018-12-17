from bs4 import BeautifulSoup
import glob
import pandas as pd
from operator import itemgetter
from datetime import datetime as dt

def getAllFiles(path=""):
    files = glob.glob(path + "*html")
    if files == []:
        files = glob.glob(path + "/*html")
        if files == []:
            return False
    return files


def combineFiles(list, outfileName="result.html"):
    with open(outfileName, 'w') as outfile:
        for fname in list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    return outfile


def getUsers(soup):
    seen_users = set()

    def users(tag):
        username = tag.get('title')
        if username and ('box_r' in tag.get('class', '') or 'box_l' in tag.get('class', '')):
            seen_users.add(username)
            return True

    soup.find_all(users)
    return seen_users


def getMessageData(file):
    data = []
    soup = BeautifulSoup(file, 'html.parser')
    for name in getUsers(soup):
        for div in soup.find_all("div",{"title":name}):
            data.append([name,dt.strptime(div["time"],"%m/%d/%Y %I:%M:%S %p"),div.find('span').text])

    data = sorted(data, key=itemgetter(1))
    for item in data:
        item[1] = item[1].strftime("%d/%m/%Y")

    return data