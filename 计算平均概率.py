import random

times = 10000000
g = 0.125

t = 1
i = 1
p = 0
p_list = []

while t <= times:
    if random.random() <= g * i:
        is_pass = True
        p_list.append({"time": t, "p_times": i, "is_pass": is_pass})
        p += 1
        i = 1

    else:
        is_pass = False
        p_list.append({"time": t, "p_times": i, "is_pass": is_pass})
        i += 1

    t += 1

p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
p_6 = 0
p_7 = 0
p_8 = 0
p_max = 0

for pp in p_list:
    if pp["p_times"] > p_max:
        p_max = pp["p_times"]
    if pp["is_pass"] == True and pp["p_times"] == 1:
        p_1 += 1
    if pp["is_pass"] == True and pp["p_times"] == 2:
        p_2 += 1
    if pp["is_pass"] == True and pp["p_times"] == 3:
        p_3 += 1
    if pp["is_pass"] == True and pp["p_times"] == 4:
        p_4 += 1
    if pp["is_pass"] == True and pp["p_times"] == 5:
        p_5 += 1
    if pp["is_pass"] == True and pp["p_times"] == 6:
        p_6 += 1
    if pp["is_pass"] == True and pp["p_times"] == 7:
        p_7 += 1
    if pp["is_pass"] == True and pp["p_times"] == 8:
        p_8 += 1
print('1把过的局数 ', p_1)
print('2把过的局数 ', p_2)
print('3把过的局数 ', p_3)
print('4把过的局数 ', p_4)
print('5把过的局数 ', p_5)
print('6把过的局数 ', p_6)
print('7把过的局数 ', p_7)
print('8把过的局数 ', p_8)

print(p_1 + p_2 + p_3 + p_4 + p_5 + p_6 + p_7 + p_8, p, len(p_list), p_max)
print(p / times)
