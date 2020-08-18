import json
import requests


class Api:
    params = {}

    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", str(value))
        data = json.loads(raw_data)

        print(data)
        return requests.request(**data).json()