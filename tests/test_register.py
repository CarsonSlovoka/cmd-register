# pytest test_register.py -v
# pytest test_register.py::test_new_register -v

import unittest

# gcm python
# 於該目錄新增 `xxx.pth` 文件，並將此專案路徑給它即可讓python曉得
from cmd_register import new_register

cmd_funcs = []
cmd_register = new_register(cmd_funcs)

tool_funcs = []
tool_register = new_register(
    tool_funcs,
    lambda f: print(f"run tool: {f.__name__}"), # 可以設定before_func，使單獨運行函數時會先執行此動作
)

@cmd_register
def say(msg: str):
    print(msg)

@cmd_register
def bar():
    print("bar")

@tool_register
def ocr():
    print("ocr ...")


def test_new_register(capfd):
    print(len(cmd_funcs))
    say("hello")
    captured = capfd.readouterr()
    assert captured.out == \
"""2
hello
"""


def test_new_register2(capfd):
    print(len(tool_funcs))
    ocr()
    captured = capfd.readouterr()
    assert captured.out == \
"""1
run tool: ocr
ocr ...
"""
