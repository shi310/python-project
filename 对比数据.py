from util import path,consol
import pandas




zhang_bian_ji_lu_path = path.join('表格','2月13号记录.xlsx')
zhu_dan_ji_lu_path = path.join('表格','注单记录.xlsx')

zhang_bian_ji_lu_table = pandas.read_excel(zhang_bian_ji_lu_path,sheet_name=None)
zhu_dan_ji_lu_table = pandas.read_excel(zhu_dan_ji_lu_path,sheet_name=None)

zhang_bian_ji_lu = []
zhu_dan_ji_lu = []

zhang_bian_ji_lu_same = []





for sheet_name, sheet_data in zhang_bian_ji_lu_table.items():
        # 格式化表格文件
        sheet_rows = sheet_data.to_dict(orient='records')


        # 读取每一行的信息
        for row_data in sheet_rows:
            
            if sheet_name == '账变记录-投注':
                zhang_bian_ji_lu.append(row_data)



for sheet_name, sheet_data in zhu_dan_ji_lu_table.items():
        # 格式化表格文件
        sheet_rows = sheet_data.to_dict(orient='records')

        # 读取每一行的信息
        for row_data in sheet_rows:
            zhu_dan_ji_lu.append(row_data)


# for zhang_bian in zhang_bian_ji_lu:
#       count = 0
#       for zhu_dan in zhang_bian_ji_lu:
            
            
#             is_same_id = zhang_bian['会员ID'] == zhu_dan['会员ID']
#             is_same_time = zhang_bian['创建时间'] == zhu_dan['创建时间']
#             is_same_money = zhang_bian['金额'] == zhu_dan['金额']
#             is_same_bi = zhang_bian['币种'] == zhu_dan['币种']


#             is_sanme = is_same_id and is_same_time and is_same_money

#             if is_sanme:
#                   count += 1

#             if count > 1:
#                   info = '%s 有重复 => %d 个' % (zhang_bian, count)


count = 0
for zhang_bian in zhang_bian_ji_lu:
      for zhu_dan in zhu_dan_ji_lu:
            
            
            is_same_id = zhang_bian['会员ID'] == zhu_dan['会员ID']
            is_same_time = zhang_bian['创建时间'] == zhu_dan['下注时间']
            is_same_money = 0-zhang_bian['金额'] == zhu_dan['投注金额']
            is_same_bi = zhang_bian['币种'] == zhu_dan['币种']


            is_sanme = is_same_id and is_same_time and is_same_money

            if  is_sanme:
                  zhang_bian_ji_lu_same.append(zhang_bian)
                  continue
            
consol.error(len(zhang_bian_ji_lu))
consol.error(len(zhang_bian_ji_lu_same))


            
for zhang_bian in zhang_bian_ji_lu:
      for same in zhang_bian_ji_lu_same:
            if zhang_bian == same:
                  zhang_bian_ji_lu.remove(same)
                  continue

consol.error(len(zhang_bian_ji_lu))

                
    






