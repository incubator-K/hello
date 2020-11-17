# 制作变量名的Json文件
import re


def createJson(eqName):
    """
    编写某个设备的Json文件
    :param eqName:设备的名字
    :return:
    """
    with open("Names", "r", encoding="UTF-8") as r, open("EQProperties.json", "w", encoding="UTF-8") as w:
        w.write("\"%s\":{\n" % eqName)
        datas = r.readlines()
        for data in datas:
            data = data.replace("\t", " ").replace("\n", "")
            nameAndValue = data.split(" ")
            name = ""
            value = ""
            for item in nameAndValue:
                res = re.match("[a-zA-Z0-9_#]{1,}", item)
                if is_Chinese(item):
                    name = item
                    pass
                elif res:
                    value = res.group()
                pass
            w.write("\"{}\": \"{}\",\n".format(name, value))
            pass
        w.write("}\n")
        pass
    pass


def is_Chinese(word):
    """
    判断字符是否为中文
    :param word:
    :return:
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


createJson("Feeder")
