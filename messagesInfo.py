from bs4 import BeautifulSoup
import glob


def getAllFiles(path=""):
    files = glob.glob(path+"*html")
    if files == []:
        files = glob.glob(path+"/*html")
        if files == []:
            return False
    return files

