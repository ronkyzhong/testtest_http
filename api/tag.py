import requests
import yaml

from api.api import Api
from api.util import Util


class Tag(Api):
    def __init__(self):
        self.token = Util().get_token()
        self.params['token'] = self.token
        with open("../test_data/tag.yaml", encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def create_tag(self, tagname, tagid):
        """
        https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        """
        self.params['tagname'] = tagname
        self.params['tagid'] = tagid
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}", json=data)
        return self.send(self.data["create_tag"])
        # assert "created" == r.json()['errmsg']

    def update_tag(self, tagname, tagid):
        """
        https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        """
        self.params['tagname'] = tagname
        self.params['tagid'] = tagid
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
        #                   json=data)
        return self.send(self.data["update_tag"])
        # print(r.json())
        # assert "updated" == r.json()['errmsg']

    def select_tag(self, tagid):
        """
        https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        self.params['tagid'] = tagid
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        # print(r.json())
        # assert "UI" == r.json()['tagname']
        return self.send(self.data["select_tag"])

    def delete_tag(self, tagid):
        """
        https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        self.params['tagid'] = tagid
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}")
        # print(r.json())
        # assert "deleted" == r.json()['errmsg']
        return self.send(self.data["delete_tag"])
