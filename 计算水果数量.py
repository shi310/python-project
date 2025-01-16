from decimal import Decimal
from collections import Counter

fruits = [
    {
        "name":
        "蓝莓",
        "info": [
            {
                "numbers": 15,
                "pei": 3,
            },
            {
                "numbers": 12,
                "pei": 1,
            },
            {
                "numbers": 10,
                "pei": 0.8,
            },
            {
                "numbers": 9,
                "pei": 0.6,
            },
            {
                "numbers": 8,
                "pei": 0.4,
            },
            {
                "numbers": 7,
                "pei": 0.3,
            },
            {
                "numbers": 6,
                "pei": 0.2,
            },
            {
                "numbers": 5,
                "pei": 0.1,
            },
        ]
    },
    {
        "name":
        "草莓",
        "info": [
            {
                "numbers": 15,
                "pei": 3,
            },
            {
                "numbers": 12,
                "pei": 1,
            },
            {
                "numbers": 10,
                "pei": 0.8,
            },
            {
                "numbers": 9,
                "pei": 0.6,
            },
            {
                "numbers": 8,
                "pei": 0.4,
            },
            {
                "numbers": 7,
                "pei": 0.3,
            },
            {
                "numbers": 6,
                "pei": 0.2,
            },
            {
                "numbers": 5,
                "pei": 0.1,
            },
        ]
    },
    {
        "name":
        "牛油果",
        "info": [
            {
                "numbers": 15,
                "pei": 10,
            },
            {
                "numbers": 12,
                "pei": 3,
            },
            {
                "numbers": 10,
                "pei": 1,
            },
            {
                "numbers": 9,
                "pei": 0.8,
            },
            {
                "numbers": 8,
                "pei": 0.6,
            },
            {
                "numbers": 7,
                "pei": 0.4,
            },
            {
                "numbers": 6,
                "pei": 0.3,
            },
            {
                "numbers": 5,
                "pei": 0.2,
            },
        ]
    },
    {
        "name":
        "山竹",
        "info": [
            {
                "numbers": 15,
                "pei": 10,
            },
            {
                "numbers": 12,
                "pei": 3,
            },
            {
                "numbers": 10,
                "pei": 1,
            },
            {
                "numbers": 9,
                "pei": 0.8,
            },
            {
                "numbers": 8,
                "pei": 0.6,
            },
            {
                "numbers": 7,
                "pei": 0.4,
            },
            {
                "numbers": 6,
                "pei": 0.3,
            },
            {
                "numbers": 5,
                "pei": 0.2,
            },
        ]
    },
    {
        "name":
        "杨桃",
        "info": [
            {
                "numbers": 15,
                "pei": 75,
            },
            {
                "numbers": 12,
                "pei": 5,
            },
            {
                "numbers": 10,
                "pei": 3,
            },
            {
                "numbers": 9,
                "pei": 2.8,
            },
            {
                "numbers": 8,
                "pei": 1.5,
            },
            {
                "numbers": 7,
                "pei": 1,
            },
            {
                "numbers": 6,
                "pei": 0.7,
            },
            {
                "numbers": 5,
                "pei": 0.5,
            },
        ]
    },
    {
        "name":
        "红毛丹",
        "info": [
            {
                "numbers": 15,
                "pei": 150,
            },
            {
                "numbers": 12,
                "pei": 10,
            },
            {
                "numbers": 10,
                "pei": 5,
            },
            {
                "numbers": 9,
                "pei": 3,
            },
            {
                "numbers": 8,
                "pei": 2,
            },
            {
                "numbers": 7,
                "pei": 1,
            },
            {
                "numbers": 6,
                "pei": 0.8,
            },
            {
                "numbers": 5,
                "pei": 0.6,
            },
        ]
    },
    {
        "name":
        "枇杷",
        "info": [
            {
                "numbers": 15,
                "pei": 300,
            },
            {
                "numbers": 12,
                "pei": 25,
            },
            {
                "numbers": 10,
                "pei": 10,
            },
            {
                "numbers": 9,
                "pei": 4,
            },
            {
                "numbers": 8,
                "pei": 3,
            },
            {
                "numbers": 7,
                "pei": 2,
            },
            {
                "numbers": 6,
                "pei": 1,
            },
            {
                "numbers": 5,
                "pei": 0.8,
            },
        ]
    },
    {
        "name":
        "火龙果",
        "info": [
            {
                "numbers": 15,
                "pei": 750,
            },
            {
                "numbers": 12,
                "pei": 50,
            },
            {
                "numbers": 10,
                "pei": 20,
            },
            {
                "numbers": 9,
                "pei": 8,
            },
            {
                "numbers": 8,
                "pei": 5,
            },
            {
                "numbers": 7,
                "pei": 3,
            },
            {
                "numbers": 6,
                "pei": 2,
            },
            {
                "numbers": 5,
                "pei": 1,
            },
        ]
    },
]


# 浮点数精度处理
def change(number):
    return Decimal(number).quantize(Decimal("0.01"))


# 两个数组是否相同
def isSameList(list_1: list[dict], list_2: list[dict]):
    if len(list_1) != len(list_2):
        return False

    same_sum = 0

    for m in list_1:
        for n in list_2:
            if m == n:
                same_sum += 1

    if same_sum == len(list_1):
        return True

    return False


# 是否触发大乐透
isBonus = False

# 目标倍率
taget = change(240)
taget_min = change(200)
taget_max = change(300)


# 拿到符合要求的水果列表
def get_pass_fruit(
    taget: Decimal,
    taget_min: Decimal,
    taget_max: Decimal,
    frutis: list[dict],
    is_range: bool = False,
):
    # 通过的组合列表
    pass_fruit: list[list] = []

    # 每一种水果都需要尝试，一个一个来
    for fruit in frutis:

        # 每个水果的每一个赔率都需要试试有没有组合
        # 例如一个水果有 8 种赔率
        for info in fruit["info"]:

            # 如果水果的赔率比目标大，就不用和其他水果组合了
            # 这里包含了范围和非范围两种情况
            if (not is_range and change(info["pei"])
                    > taget) or (is_range and change(info["pei"]) > taget_max):

                continue

            # 下面的情况就是水果的赔率比目标赔率小，需要和其他水果进行组合
            # 也是我们重点需要计算的地方
            # 非双倍的数据
            pass_info = {"name": fruit["name"]}
            pass_info["info"] = info
            pass_info["isDouble"] = False

            # 双倍的数据
            # 默认存一个单倍和一个双倍
            pass_info_double = {"name": fruit["name"]}
            pass_info_double["info"] = info
            pass_info_double["isDouble"] = True

            # 如果水果的赔率刚好等于目标，也不用和其他水果组合了，这也是合理的单组合
            # 或者是赔率刚好等于目标范围的最大值
            if (not is_range and change(info["pei"]) == taget) or (
                    is_range and change(info["pei"]) == taget_max):
                pass_fruit.append([pass_info])
                continue

            # 如果水果的赔率刚好处于目标范围内，这也是合理的单组合
            if is_range and change(info["pei"]) < taget_max and change(
                    info["pei"]) >= taget_min:
                pass_fruit.append([pass_info])

            # 如果水果的赔率*2刚好等于目标或等于范围的最大值，
            if (not is_range and change(info["pei"] * 2) == taget) or (
                    is_range and change(info["pei"] * 2) == taget_max):
                pass_fruit.append([pass_info_double])

            # 如果水果的赔率*2刚好在区间内
            if is_range and change(info["pei"] * 2) < taget_max and change(
                    info["pei"] * 2) >= taget_min:
                pass_fruit.append([pass_info_double])

            # 通过的组合列表
            pass_list: list[list] = []
            # 这是赔率相加的和值
            # 和 pass_list 是一一对应的
            result: list[list] = []

            # 开始循环和其他水果进行匹配
            # 我们要一个一个的来匹配
            # 首先从第一个水果的第一个赔率和所有水果的所有赔率进行匹配
            for fruit_2 in fruits:
                # 同一种水果就跳过
                if fruit["name"] == fruit_2["name"]:
                    continue

                # 第一次和非第一次的处理不同
                # is_first = True

                for info_2 in fruit_2['info']:
                    # 如果水果的赔率比目标大，就不用和其他水果组合了
                    if (not is_range and change(info["pei"]) > taget) or (
                            is_range and change(info["pei"]) > taget_max):

                        continue

                    # 下面的情况就是水果的赔率比目标赔率小，需要和其他水果进行组合
                    # 也是我们重点需要计算的地方
                    # 非双倍的数据
                    pass_info_2 = {"name": fruit_2["name"]}
                    pass_info_2["info"] = info_2
                    pass_info_2["isDouble"] = False

                    # 双倍的数据
                    # 默认存一个单倍和一个双倍
                    pass_info_2_double = {"name": fruit_2["name"]}
                    pass_info_2_double["info"] = info_2
                    pass_info_2_double["isDouble"] = True

                    # else:
                    # 开始往数组里添加值
                    # 这个时候添加的是各种组合不考虑是否符合要求
                    for i in range(len(result)):
                        result_temp = change(result[i])
                        pass_list_temp = pass_list[i].copy()

                        result_sum = result_temp + change(info_2["pei"])

                        # 同样的水果的不同赔率不能出现在一个组合里
                        is_have_name = False

                        for p in pass_list_temp:
                            if p["name"] == pass_info_2["name"] or p[
                                    "name"] == pass_info_2_double["name"]:
                                is_have_name = True
                                continue

                        if is_have_name:
                            continue

                        if (not is_range and result_sum <= taget) or (
                                is_range and result_sum <= taget_max):
                            result[i] = result_sum
                            pass_list[i].append(pass_info_2)

                        result_sum = result_temp + change(info_2["pei"] * 2)
                        if (not is_range and result_sum <= taget) or (
                                is_range and result_sum <= taget_max):
                            result.append(result_sum)
                            pass_list_temp.append(pass_info_2_double)
                            pass_list.append(pass_list_temp)

                    # if is_first:
                    result_sum = change(info["pei"]) + change(info_2["pei"])

                    if (not is_range and result_sum <= taget) or (
                            is_range and result_sum <= taget_max):
                        result.append(result_sum)
                        pass_info_list = [pass_info, pass_info_2]
                        pass_list.append(pass_info_list)

                    ##########################

                    result_sum = change(info["pei"] * 2) + change(
                        info_2["pei"])

                    if (not is_range and result_sum <= taget) or (
                            is_range and result_sum <= taget_max):
                        result.append(result_sum)
                        pass_info_list = [pass_info_double, pass_info_2]
                        pass_list.append(pass_info_list)

                    ##########################

                    result_sum = change(info["pei"]) + change(
                        info_2["pei"] * 2)
                    if (not is_range and result_sum <= taget) or (
                            is_range and result_sum <= taget_max):
                        result.append(result_sum)
                        pass_info_list = [pass_info, pass_info_2_double]
                        pass_list.append(pass_info_list)

                    ##########################

                    result_sum = change(info["pei"] * 2) + change(
                        info_2["pei"] * 2)
                    if (not is_range and result_sum <= taget) or (
                            is_range and result_sum <= taget_max):
                        result.append(result_sum)
                        pass_info_list = [
                            pass_info_double,
                            pass_info_2_double,
                        ]
                        pass_list.append(pass_info_list)

                    ##########################

                # is_first = False
                # print(pass_list)

                for i in range(len(result)):
                    is_not_have = True
                    for p in pass_fruit:
                        if isSameList(pass_list[i].copy(), p.copy()):
                            is_not_have = False
                            break

                    if not is_range:
                        # 能直接找到目标杀率的方案
                        is_taget = change(result[i]) == taget
                        if is_taget and is_not_have:
                            pass_fruit.append(pass_list[i].copy())
                    else:
                        is_in_range = change(
                            result[i]) <= taget_max and change(
                                result[i]) >= taget_min
                        if is_in_range and is_not_have:
                            pass_fruit.append(pass_list[i].copy())

    return pass_fruit


pass_fruit = get_pass_fruit(taget, taget_min, taget_max, fruits, False)

# 如果找不到组合
# 改为用区间尝试
if pass_fruit == []:
    print('没有找到任何符合要求的组合')
    pass_fruit = get_pass_fruit(taget, taget_min, taget_max, fruits, True)

# 如果还是没有组合那就是配置实在有问题

print('符合要求的组合数量', len(pass_fruit))
for p in pass_fruit:
    result = 0
    for f in p:
        if f["isDouble"] == True:
            result += f["info"]["pei"] * 2
        else:
            result += f["info"]["pei"]
    print(change(result), p)

# 大乐透的思路，将大乐透的的区间分成三份
# 第一份：60%
# 第二份：30%
# 第三份：10%
# 例如：随机到了 100 - 200 这个区间
# 第一步的区间为 60-120
# 第二步的区间为 30-60
# 第三步的区间为 10-20
# 这样的话，每一步都能通过get_pass_fruit方法拿到符合要求的组合，在多个组合中随机一个即可
# 拿到了水果的组合就可以生成地图给客户端了

# 方法还能继续拓展，例如通过区间算出来的组合怎么取值
# 1、可以随机一个
# 2、可以取和taget最接近的
