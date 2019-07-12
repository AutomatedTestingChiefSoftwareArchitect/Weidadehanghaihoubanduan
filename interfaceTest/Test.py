import requests
from interfaceTest.readexcel_package import readExcel


url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
results = requests.get(url, parameter)
if results.status_code == 200:
    print(url, parameter)
    print(results.json())
else:
    print("cuowula")