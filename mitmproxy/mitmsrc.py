from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "https://book.douban.com/" in flow.request.pretty_url:
        with open("tmp2.json", encoding='utf-8') as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                "Hello World" + f.read(),  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )