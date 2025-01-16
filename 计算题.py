jihua = input('请输入计划每天修多少米：')
shiji = input('请输入实际每天修多少米：')

jisuan1:int= int(shiji) - int(jihua)
jisuan2:int = int(shiji) / jisuan1
jisuan3:int = int(jihua) * jisuan2



print(jisuan3 * 3 / int(shiji))