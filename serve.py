#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分镜工坊(开源版)本地服务 — 可选。

纯标准库，零依赖。两个作用：
1. 本地托管静态页面（http://127.0.0.1:8799）
2. /api_proxy CORS 兜底：个别 API 服务不允许浏览器直连时，由本进程代转

不想跑它也行：直接双击 index.html 也能用（多数国内 API 允许浏览器直连）。
"""
import json
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = int(os.environ.get("PORT", 8799))
HERE = os.path.dirname(os.path.abspath(__file__))


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def do_POST(self):
        if self.path != "/api_proxy":
            self.send_error(404)
            return
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            url = body["url"]
            if not url.startswith(("http://", "https://")):
                raise ValueError("bad url")
            req = urllib.request.Request(
                url,
                data=json.dumps(body["payload"]).encode("utf-8"),
                headers={"Content-Type": "application/json",
                         "Authorization": body.get("auth", "")},
            )
            with urllib.request.urlopen(req, timeout=300) as r:
                data = r.read()
            self.send_response(200)
        except Exception as e:
            data = json.dumps({"error": str(e)}).encode("utf-8")
            self.send_response(502)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"分镜工坊(开源版) → http://127.0.0.1:{PORT}")
    HTTPServer(("127.0.0.1", PORT), H).serve_forever()
