import messagesInfo as mi

files = mi.getAllFiles("Test1")

if files:
    combined = mi.combineFiles(files)
