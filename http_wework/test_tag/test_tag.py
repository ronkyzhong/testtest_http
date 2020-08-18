from http_wework.api.tag import Tag


class TestTag():
    def test_create_tag(self):
        assert "created" in Tag().create_tag("java", "111")['errmsg']

    def test_update_tag(self):
        assert "updated" in Tag().update_tag("testUI", 12)['errmsg']

    def test_select_tag(self):
        print(Tag().select_tag(12))
        assert "ok" in Tag().select_tag(12)['errmsg']

    def test_delete_tag(self):
        assert "deleted" in Tag().delete_tag(12)['errmsg']
