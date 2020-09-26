
import typewrap
import pytest

def add(a: int, b: int = 1) -> float:
    return float(a + b)

@typewrap.typeCheck
def xadd(a: int, b: int = 1) -> float:
    return float(a + b)

def test_add():
    assert add(1,2.0) == 3.0
    with pytest.raises(TypeError):
        xadd(1,2.0)





