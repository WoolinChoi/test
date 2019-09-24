"""
    exfile3.py
    mypackage / eaxm / exmodule.py 안엔 sum() 호출
"""
import example.exmodule
print(example.exmodule.sum("3", 4))

from example import exmodule
print(exmodule.sum("3", 4))

from example.exmodule import sum
print(sum("3", 4))

