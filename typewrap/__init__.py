
import functools
import inspect


__version__ = "0.2.2"


def typeCheck(f):
    """Function input type-checking decorator.
    
    Wraps a function with argument type annotations.
    When function is called, checks input and output
    value types against annotated types.
    """
    # Get the function signature
    sig = inspect.signature(f)
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Check the inputs
        bound = sig.bind(*args,**kwargs)
        for arg, val in bound.arguments.items():
            argtype = sig.parameters.get(arg).annotation
            if argtype is inspect._empty: continue
            if not isinstance(val,argtype):
                raise TypeError(f"[typeCheck] type({val!r}) !+ {argtype!r}")
        # Compute the result
        result = f(*args,**kwargs)
        # Check the output
        return_type = sig.return_annotation
        if return_type is not inspect._empty:
            if not isinstance(result,return_type):
                raise TypeError(f"[typeCheck] type({result!r}) !+ {return_type!r}")
        return result
    return inner

def checkInputs(f):
    """Function input type-checking decorator.
    
    Wraps a function with argument type annotations.
    When function is called, checks input arguments 
    against annotated types.

    Example:
    >>> @checkInputs
    >>> def add(a: int, b: int):
    ...    return a + b
    >>> add(1, 2)   # Works
    >>> add(1, 2.0) # Raises TypeError
    """
    # Get the function signature
    sig = inspect.signature(f)
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Check the inputs
        bound = sig.bind(*args,**kwargs)
        for arg, val in bound.arguments.items():
            argtype = sig.parameters.get(arg).annotation
            if argtype is inspect._empty: continue
            if not isinstance(val,argtype):
                raise TypeError(f"[typeCheck] type({val!r}) !+ {argtype!r}")
        # Return the result
        return f(*args,**kwargs)
    return inner



