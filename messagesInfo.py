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
