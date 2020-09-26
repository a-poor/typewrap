
import functools
from inspect import signature


def typeCheck(f):

    annots = f.__annotations__

    annots = {
        k: v for k, v in 
        f.__annotations__.items()
        if isinstance(v, type)
    }
    inTypes = {
        k:v for k,v in annots.items()
        if k != "return"
    }
    checkOutput = "return" in annots
    outType = annots.get("return")
    
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Check the inputs
        # ...
        # Compute the result
        result = f(*args,**kwargs)
        # Check the output
        if output is not None:
            assert (
                isinstance(result,outType) or 
                result == outType
                ), f"return value typeCheck error: {result!r} != {outType!r}"
        return result
    return inner


def add1(a,b):
    return float(a + b)

def add2(a: int,b: int = 1):
    return float(a + b)

def add3(a: int,b: int = 1) -> float:
    return float(a + b)

@typeCheck
def xadd1(a,b):
    return float(a + b)

@typeCheck
def xadd2(a: int,b: int = 1):
    return float(a + b)

@typeCheck
def xadd3(a: int,b: int = 1) -> float:
    return float(a + b)
