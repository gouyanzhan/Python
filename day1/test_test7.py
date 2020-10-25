import pytest


def f():
    return 5
def test_f():
    n = f()
    assert n % 3 == 0 ,  "判断n是否能被3整除，当前n的值为：%s" % n


if __name__ == '__main__':
    pytest.main()
