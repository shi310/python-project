from util import odds, json, path, consol


def init_data():
    return {
        "data": {
            "max": 0.09,
            "min": 0.07
        },
        "header": {
            "max":
            "最大杀率",
            "min":
            "最小杀率",
            "normal":
            "正常配置,lv1.min-第一关得分倍率最小值,lv1.max-第一关得分倍率最大值,lv1.ratio-概率,lv2.min-第二关得分倍率最小值,lv2.max-第二关得分倍率最大值,lv2.ratio-概率,lv3.min-第三关得分倍率最小值,lv3.max-第三关得分倍率最大值,lv3.ratio-概率,lv4.min-第四关得分倍率最小值,lv4.max-第四关得分倍率最大值,lv4.ratio-概率",
            "less_than":
            "补杀配置,ratio-前杀率小于目标杀率最小值的比率,lv1.min-第一关得分倍率最小值,lv1.max-第一关得分倍率最大值,lv1.ratio-概率,lv2.min-第二关得分倍率最小值,lv2.max-第二关得分倍率最大值,lv2.ratio-概率,lv3.min-第三关得分倍率最小值,lv3.max-第三关得分倍率最大值,lv3.ratio-概率,lv4.min-第四关得分倍率最小值,lv4.max-第四关得分倍率最大值,lv4.ratio-概率",
            "greater_than":
            "放水设置,ratio-当前杀率大于目标杀率最大值的比列,lv1.min-第一关得分倍率最小值,lv1.max-第一关得分倍率最大值,lv1.ratio-概率,lv2.min-第二关得分倍率最小值,lv2.max-第二关得分倍率最大值,lv2.ratio-概率,lv3.min-第三关得分倍率最小值,lv3.max-第三关得分倍率最大值,lv3.ratio-概率,lv4.min-第四关得分倍率最小值,lv4.max-第四关得分倍率最大值,lv4.ratio-概率"
        }
    }


def start():
    '''计算权重可以直接调用方法::

        odds.probability(list, 2)

    返回一个概率数组::

        [0。0000,0.5000,0.5000]
    '''

    result = init_data()


if __name__ == '__main__':
    start()
