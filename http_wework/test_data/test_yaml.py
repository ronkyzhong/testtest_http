import json

import yaml

params = {
    "token": "token",
    "tagname":"bbbb",
    "tagid": 11
}


def test_yaml():
    with open("tag.yaml", encoding='utf-8') as f:
        data = yaml.safe_load(f)['create_tag']
        print(data)
        print(type(data))

        data1 = json.dumps(data)
        print(data1)
        print(type(data1))
        for key, value in params.items():
            data1 = data1.replace('${'+key+'}', str(value))
        print(data1)
        print(type(data1))
        data = json.loads(data1)

        print(data)
        print(type(data))
