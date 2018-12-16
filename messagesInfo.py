from bs4 import BeautifulSoup
import glob


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


def getUsers(file):
    seen_users = set()

    def users(tag):
        username = tag.get('title')
        if username and 'message' in tag.get('class', ''):
            seen_users.add(username)
            return True

    soup = BeautifulSoup(file, 'html.parser')
    soup.find_all(users)
    return seen_users
