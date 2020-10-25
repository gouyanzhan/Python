# 异常断言

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as exceptionInfo:
        100 / 0
    #断言异常类型

    assert exceptionInfo.type == ZeroDivisionError

    #断言异常的值

    assert "division by zero" in str(exceptionInfo.value)