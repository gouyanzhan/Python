import pytest


def add(x):
    return x + 6
def test_result():
    assert add(6) == 11

if __name__ == '__main__':
    pytest.main()

