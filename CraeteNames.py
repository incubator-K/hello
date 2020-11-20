def CreateName():
    with open("RealNames.txt", "r", encoding="utf-8") as r, open("ChineseNames.txt", "w", encoding="utf-8") as w:
        strNames = r.readlines()
        for strName in strNames:
            names = strName.split("\t")
            name = names[0] + "\n"
            w.write(name)
        pass
    pass


CreateName()
