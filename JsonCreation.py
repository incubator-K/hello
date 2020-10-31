# 制作变量名的Json文件
def createJson(eqName):
    """
    编写某个设备的Json文件
    :param eqName:设备的名字
    :return:
    """
    with open("Names","r",encoding="UTF-8") as r,open("EQProperties.json","w",encoding="UTF-8") as w:
        w.write("{\n")
        w.write("\"{}\":{".format(eqName))
        datas = r.readlines()
        for data in datas:

            pass
        w.write("}")
        w.write("}\n")
        pass
    pass