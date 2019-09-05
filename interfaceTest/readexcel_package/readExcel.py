import os
import interfaceTest.getpathInfo
from xlrd import open_workbook

# 当前测试路径
path = interfaceTest.getpathInfo.get_Path()

class readExcel():

    def get_xls(self, xls_name, sheet_name):
        # 定义一个list
        cls = []
        # join拼接获取需要遍历的excel路径
        xlsPath = os.path.join(path, "testFile", xls_name)
        # 打开excel
        file = open_workbook(xlsPath)
        # 获取excel的sheet
        sheet = file.sheet_by_name(sheet_name)
        # 获取sheet行数
        nrows = sheet.nrows
        # 遍历行数
        for i in range(nrows):
            # 跳过第一行
            if i == 0:
                continue
                # 将遍历的数据添加至cls
            cls.append(sheet.row_values(i))
        return cls

reds = readExcel()


