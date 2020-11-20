import random
import TimeListTest


class VarValue:
    def __init__(self, varName):
        self.varName = varName
        if "报警" in varName or "状态" in varName:
            if random.randint(1, 10) == 3:
                self.varValue = "True"
            else:
                self.varValue = "False"
            pass
        else:
            self.varValue = random.randint(5, 600) / 10
        pass

    pass


def insertStrCurretCreste(projectName, eqName, i):
    with open("ChineseNames.txt", "r", encoding="utf-8") as r, open("Insert.txt", "a", encoding="utf-8") as w:
        names = r.readlines()
        for VarName in names:
            myVarName = VarName.replace("\n", "")
            myVarValue = VarValue(myVarName)
            insertStr = "INSERT INTO [dbo].[VarableHistory]  ([Id] ,[ProjectName],[EQName],[VarName],[VarValue]" \
                        ",[SaveTime]) " \
                        "VALUES({},'{}','{}','{}','{}','{}');\n".format(i, projectName, eqName, myVarName,
                                                                        myVarValue.varValue,
                                                                        TimeListTest.getRadomTime())
            i += 1
            w.write(insertStr)
            pass
        pass
    return i
    pass


a = insertStrCurretCreste("上海", "喂料机1", 141)
b = insertStrCurretCreste("西安", "喂料机1", a)
c = insertStrCurretCreste("上海", "喂料机2", b)
d = insertStrCurretCreste("西安", "喂料机2", c)
