import os
import interfaceTest.getpathInfo
import time

date = time.strftime('%Y%m%d%H%M%S')
path = interfaceTest.getpathInfo.get_Path()
config_path = os.path.join(path,
                           'result\\report-' + date + '.html')
print(config_path)

from interfaceTest.readexcel_package import readExcel

url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
methods = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][3]
print(url)
print(parameter)
print(methods)
config_path1 = "D:\Program Files\PyrequestCode\interfaceTest\\result\\report-20190710180114.html"
print(config_path1)