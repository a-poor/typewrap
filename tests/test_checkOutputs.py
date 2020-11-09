
import typewrap
import pytest


@typewrap.checkOutputs
def add_retAnnotsMatch(a: int, b: int = 1) -> float:
    """Return type matches annotation"""
    return float(a + b)

@typewrap.checkOutputs
def add_retAnnotsDontMatch(a: int, b: int = 1) -> float:
    """Return type DOESN'T match annotation"""
    return int(a + b)


def test_checkOutputs():
    # Input args don't match but
    # wrapper isn't looking for it
    assert add_retAnnotsMatch(1,2.0)
    # Input and output args match
    # supplied annotations
    assert add_retAnnotsMatch(1,2) == 3.0

    with pytest.raises(typewrap.TypeCheckError):
        # ret annotation: `float` | actual ret: `int`
        add_retAnnotsDontMatch(1,2)
