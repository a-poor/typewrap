
import typewrap
import pytest

def add(a: int, b: int = 1) -> float:
    return float(a + b)

@typewrap.checkInputs
def add_checkInputs(a: int, b: int = 1) -> float:
    return float(a + b)

@typewrap.checkInputs
def add_checkOutputs(a: int, b: int = 1) -> float:
    return int(a + b)


def test_add():
    assert add(1,2.0) == 3.0
    assert add("3",".0") == 3.0

    assert add_checkInputs(1,2)
    with pytest.raises(TypeError):
        add_checkInputs(1,2.0)
    
    assert add_checkOutputs(1,2) == 3.0




