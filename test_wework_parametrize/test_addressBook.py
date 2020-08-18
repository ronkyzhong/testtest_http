import random
import re

import pytest
import requests


def test_create_data():
    data = [("lufei"+str(i), "路飞", "138%08d"%i) for i in range(20)]
    print(data)
    return data


class TestWework:
    # @pytest.fixture(scope="session")
    # def test_get_token(token):
    #     params = {
    #         "corpid": "ww9e3bdf504c0dc816",
    #         "corpsecret": "vNkqt55N56eNIHVY8GZd7cOeoxU1bdvP06PlUkhPHFY"
    #     }
    #     r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
    #     token = r.json()['access_token']
    #     return token

    def get_token(self):
        """
        获取 access_token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        params = {
            "corpid": "ww9e3bdf504c0dc816",
            "corpsecret": "vNkqt55N56eNIHVY8GZd7cOeoxU1bdvP06PlUkhPHFY"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        # print(r.json())
        return r.json()['access_token']

    def test_create_member(self, userid, name, mobile, department=None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = [1]
        json = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}", json=json)
        return r.json()

    def test_get_member(self, userid):
        """
        获取成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        params = {
            "access_token": self.get_token(),
            "userid": userid
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        return r.json()

    def test_update_member_info(self, userid, name, mobile):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        params = {
            "access_token": self.get_token()
        }
        json = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update", params=params, json=json)
        return r.json()

    def test_delete_member(self, userid):
        """
        删除成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        params = {
            "access_token": self.get_token(),
            "userid": userid
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(r.json())
        return r.json()

    @pytest.mark.parametrize("userid,name,mobile", test_create_data())
    def test_wework(self, userid, name, mobile):
        try:
            assert "created" in self.test_create_member(userid, name, mobile)["errmsg"]
        except AssertionError as e:
            print(e)
            if "mobile existed" in e.__str__():
                err_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete_member(err_userid)
                assert "created" in self.test_create_member(userid, name, mobile)["errmsg"]
        assert userid in self.test_get_member(userid)["userid"]
        assert "updated" in self.test_update_member_info(userid, "海贼王路飞", mobile)["errmsg"]
        assert "deleted" in self.test_delete_member(userid)["errmsg"]
