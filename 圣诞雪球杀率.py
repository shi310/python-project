import os
from util import odds, json, path, consol


def build_line_data(line: dict, expected: float):
    # 正常区间
    multiples = odds.probability(line['multiples'], expected)
    ratio = []

    i = 0
    for m in multiples:
        r = {}
        r['ratio'] = float(m)
        r['multiple'] = line['multiples'][i]
        ratio.append(r)
        i += 1

    line_data = {}
    line_data['line'] = line['line']
    line_data['ratio'] = ratio

    return line_data


def build_type_data(data: dict, data_type: str, expected: float):
    lines_data = []
    for line in data:
        # 正常区间
        line_data = build_line_data(line, expected)
        lines_data.append(line_data)

    if data_type == 'low':
        type_data = {}
        type_data['type'] = 0
        type_data['lines'] = lines_data
        return type_data

    if data_type == 'normal':
        type_data = {}
        type_data['type'] = 1
        type_data['lines'] = lines_data
        return type_data

    if data_type == 'high':
        type_data = {}
        type_data['type'] = 2
        type_data['lines'] = lines_data
        return type_data

    return type_data


def build_data(json: dict, expected: float):
    result = []

    for data in json:
        _data = json[data]
        type_data = build_type_data(_data, data, expected)
        result.append(type_data)

    return result


def init_data():
    return {
        'data': {
            'max': 0.09,
            'min': 0.07,
            'less': [],
            'normal': {},
            'greater': [],
        },
        'header': {
            'max':
            '最大杀率',
            'min':
            '最小杀率',
            'less':
            '补杀配置: break-杀率小于值, lines-杀率配置(type-难度(0-low， 1-noraml， 2-high)，line-行列(line-行列， ratio-概率配置(multiple-倍率，ratio-概率)))',
            'normal':
            '正常配置: break-不用管, lines-杀率配置(type-难度(0-low， 1-noraml， 2-high)，line-行列(line-行列， ratio-概率配置(multiple-倍率，ratio-概率)))',
            'greater':
            '放水配置: break-杀率大于值, lines-杀率配置(type-难度(0-low， 1-noraml， 2-high)，line-行列(line-行列， ratio-概率配置(multiple-倍率，ratio-概率)))',
        }
    }


def start():
    '''计算权重可以直接调用方法::

        odds.probability(list, 2)

    返回一个概率数组::

        [0。0000,0.5000,0.5000]
    '''
    result = init_data()
    json_dir_path = path.join('', 'json')
    json_file_path = path.join(json_dir_path, '圣诞雪球赔率.json')
    odds_json = json.read(json_file_path)
    json_data = odds_json['data']

    data = build_data(json_data, 0.93)
    normal = {}
    normal['lines'] = data

    less = []

    data = build_data(json_data, 0.91)
    data_break = {}
    data_break['break'] = 1
    data_break['lines'] = data
    less.append(data_break)

    data = build_data(json_data, 0.9)
    data_break = {}
    data_break['break'] = 0.75
    data_break['lines'] = data
    less.append(data_break)

    data = build_data(json_data, 0.89)
    data_break = {}
    data_break['break'] = 0.5
    data_break['lines'] = data
    less.append(data_break)

    data = build_data(json_data, 0.88)
    data_break = {}
    data_break['break'] = 0.25
    data_break['lines'] = data
    less.append(data_break)

    greater = []

    data = build_data(json_data, 1)
    data_break = {}
    data_break['break'] = 0
    data_break['lines'] = data
    greater.append(data_break)

    data = build_data(json_data, 1.1)
    data_break = {}
    data_break['break'] = 0.25
    data_break['lines'] = data
    greater.append(data_break)

    data = build_data(json_data, 1.2)
    data_break = {}
    data_break['break'] = 0.5
    data_break['lines'] = data
    greater.append(data_break)

    data = build_data(json_data, 1.3)
    data_break = {}
    data_break['break'] = 0.75
    data_break['lines'] = data
    greater.append(data_break)

    result['data']['normal'] = normal
    result['data']['less'] = less
    result['data']['greater'] = greater

    consol.succful(result)
    json_write_path = path.join(json_dir_path, '圣诞雪球杀率_new.json')
    json.save(json_write_path, result)


if __name__ == '__main__':
    start()
