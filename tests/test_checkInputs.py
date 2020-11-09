
import typewrap
import pytest


@typewrap.checkInputs
def add_retAnnotsMatch(a: int, b: int = 1) -> float:
    """Return type matches annotation"""
    return float(a + b)

@typewrap.checkInputs
def add_retAnnotsDontMatch(a: int, b: int = 1) -> float:
    """Return type DOESN'T match annotation"""
    return int(a + b)


def test_checkInputs():
    # Check wrapper with good inputs
    assert add_retAnnotsMatch(1,2)
    # Check wrapper with bad inputs
    with pytest.raises(typewrap.TypeCheckError):
        add_retAnnotsMatch(1,2.0)
    # Output inputs don't match but wrapper
    # shouldn't catch it
    assert add_retAnnotsDontMatch(1,2) == 3.0
