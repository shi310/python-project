import json


def read(path: str):

    with open(path) as file:
        data = json.loads(file.read().strip())
    file.close()

    return data


def save(path: str, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False)
