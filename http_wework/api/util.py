import requests


class Util:
    def get_token(self):
        """
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        params = {
            "corpid": "ww9e3bdf504c0dc816",
            "corpsecret": "vNkqt55N56eNIHVY8GZd7aUKqhUVzjcIOzZXVHOL4Bk"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        return r.json()['access_token']