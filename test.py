from openpyxl import load_workbook
from collections import OrderedDict
import json

wb = load_workbook(filename="dummy.xlsx", read_only=True)
# print (dir(wb))
# print (wb.get_sheet_names())

ws = wb['JANUARY (WARD)']
# print (dir(ws))

x = ws.get_squared_range(min_col=1, min_row=2, max_col=1, max_row=53)
# print (x)

date_list = []
for row in x:
	for cell in row:
		test_dict = {'date of admissiom': str(cell.value)}
		date_list.append(test_dict)

j = json.dumps(date_list)

with open('date_data.json', 'w') as f:
	f.write(j)

# for row in x:
# 	for cell in row:
# 		print (cell.value)

# for row in ws.rows:
#     for cell in row:
#         print(cell.value)
