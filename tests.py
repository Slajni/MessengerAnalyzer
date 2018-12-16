import messagesInfo as mi

files = mi.getAllFiles("Test1")

if files:
    combined = mi.combineFiles(files)

file = open("Test1/testing1.html")

print(mi.getUsers(file))