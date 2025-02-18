from utils import consol
from decimal import Decimal 

def probability(p_list: list, expected: float = 1.0):
    '''
    - p_list : 赔率数组（必传）
    - ex
    '''

    # 倍数小于期望值的数组单独存放
    w_low_sum = 0.0

    # 赔率的分量
    w_list = []

    # 比期望高的倍率的数量
    p_high_number = 0

    # 同期望相同倍率的数量
    p_same_umber = 0

    # 比期望小的倍率的数量
    p_low_umber = 0

    # 分量的总和
    w_sum = 0

    # 得到的概率结果
    r_list = []

    # 分析赔率 和 期望的关系
    # 提前处理大于期望的倍率：记录个数
    # 提前处理小于期望的倍率：单独统计他们的和
    for p in p_list:
        if p > expected:
            p_high_number += 1

        elif p < expected:
            if p > 0:
                w_p = expected / p
            else:
                w_p = expected
            w_low_sum += w_p
            p_low_umber += 1
        else:
            p_same_umber += 1

    # 这里有几个特殊情况：
    # 1、期望比最大赔率还大
    if p_high_number == 0 and p_same_umber == 0:
        consol.error('期望值太高了，无法达到...')
        exit()

    # 1、期望比最大赔率还大
    if p_low_umber == 0 and p_same_umber == 0:
        consol.error('期望值太低了，无法达到...')
        exit()

    # 期望是 0 的特殊处理
    if expected == 0 and p_same_umber == 0:
        consol.error('没有 0 的赔率，期望无法达到...')
        exit()

    # 处理赔率的比重
    for p in p_list:
        if p > expected:
            # 赔率大于期望值的时候有一个特殊情况
            # 那就是需要检查是否所有赔率都是大于期望的
            if p_low_umber == 0 or expected == 0:
                w = 0
            else:
                w = expected / (p - expected)

            w = Decimal(w).quantize(Decimal("0.0001"))
            w_list.append(w)

        elif p < expected:
            # 赔率大于期望值的时候有一个特殊情况
            # 那就是需要检查是否所有赔率都是大于期望的
            if p_high_number == 0 or expected == 0:
                w = 0
            else:
                if p > 0:
                    w_p = (expected / p) / w_low_sum
                else:
                    w_p = expected / w_low_sum

                w = expected / ((expected - p) / (p_high_number * w_p))

            w = Decimal(w).quantize(Decimal("0.0001"))
            w_list.append(w)

        else:
            if p_low_umber == 0 or p_high_number == 0 or expected == 0:
                w = 1 / p_same_umber
            else:
                w = p * expected

            w = Decimal(w).quantize(Decimal("0.0001"))
            w_list.append(w)

    # 计算比重的总和
    for w in w_list:
        w_sum += w

    # 计算每个比重的权重也就是需要的概率
    for w in w_list:
        r = w / w_sum
        r = Decimal(r).quantize(Decimal("0.0001"))
        r_list.append(r)

    # 计算总概率
    i = 0  # 下标
    r_sum = 0  # 概率结果总和
    string_p = '%-8s' % '原始赔率:'
    string_w = '%-8s' % '赔率重量:'
    string_r = '%-8s' % '概率结果:'
    string_q = '%-8s' % '期望结果:'
    for p in p_list:
        # 输出文本：原始概率
        string_p += '%-8s' % p

        # 计算概率总和
        r_sum += r_list[i]

        i += 1

    for w in w_list:
        # 输出文本：原始概率
        string_w += '%-8s' % w

    # 计算最大的概率
    r_max = 0
    for r in r_list:
        if r > r_max:
            r_max = r

    # 统计最大概率的数量
    r_max_unmber = 0
    for r in r_list:
        if r == r_max:
            r_max_unmber += 1

    # 修正概率值
    i = 0
    for r in r_list:
        if r == r_max:
            if r_sum > 1:
                r_new = r - (r_sum - 1)
                r_new = w = Decimal(r_new).quantize(Decimal("0.0001"))
                r_list[i] = r_new
                break

            if r_sum < 1:
                r_new = r + (1 - r_sum)
                r_new = w = Decimal(r_new).quantize(Decimal("0.0001"))
                r_list[i] = r_new
                break
        i += 1

    # 输出倍率
    # 输出概率
    # 输出期望
    r_sum_new = 0  # 概率结果总和
    q_sum = 0  # 期望结果总和
    i = 0  # 下标
    for p in p_list:
        # 输出文本：概率结果
        string_r += '%-8s' % r_list[i]
        r_sum_new += r_list[i]

        _q = Decimal(p).quantize(Decimal("0.0001")) * r_list[i]
        _q = Decimal(_q).quantize(Decimal("0.0001"))
        string_q += '%-8s' % _q
        q_sum += _q

        i += 1

    consol.succful(string_p)
    consol.succful(string_w)
    consol.succful(string_r)
    consol.succful(string_q)

    consol.succful('概率总和: %s' % r_sum_new)
    consol.succful('期望总和: %s' % q_sum)

    print()

    return r_list
