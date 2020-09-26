
import functools
import inspect


__version__ = "0.1.0"


def typeCheck(f):
    """Function type-checking decorator."""
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



