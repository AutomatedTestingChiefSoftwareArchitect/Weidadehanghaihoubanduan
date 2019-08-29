import os
import interfaceTest.getpathInfo
from xlrd import open_workbook


path = interfaceTest.getpathInfo.get_Path()


class readExcel():

    def get_xls(self, xls_name, sheet_name):
        cls = []
        xlsPath = os.path.join(path, "testFile", xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows

        for i in range(nrows):
            if i == 0:
                continue
            cls.append(sheet.row_values(i))
        return cls


reds = readExcel()


