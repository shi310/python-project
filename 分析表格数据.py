import os
import pandas as pd

order_path = os.path.join('', 'order.csv')
bet_meta_path = os.path.join('', 'bet_meta.csv')

# 开始读取表格信息
# 读取的是单个表格文件的所有 sheet
titanic = pd.read_csv(order_path)

print(titanic.loc['30002'])

# exit()

# for sheet_name, sheet_data in df.items():
#     print(sheet_name, sheet_data)

#     # 格式化表格文件
#     sheet_rows = sheet_data.to_dict()
#     print(sheet_rows)

#     row_index = 0

#     # 读取每一行的信息
#     for row_data in sheet_rows:

#         print(row_data.values())
#         # row_index += 1
