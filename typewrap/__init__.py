
import functools
from inspect import signature, _empty


__version__ = "0.0.1"


def typeCheck(f):
    """Function type-checking decorator."""
    # Get the function signature
    sig = signature(f)
    @functools.wraps(f)
    def inner(*args,**kwargs):
        # Check the inputs
        bound = sig.bind(*args,**kwargs)
        for arg, val in bound.arguments.items():
             argtype = sig.parameters.get(arg).annotation
             if argtype is _empty: continue
             if not isinstance(val,argtype):
                TypeError(f"typeCheck: type({val!r}) !+ {argtype!r}")
        # Compute the result
        result = f(*args,**kwargs)
        # Check the output
        return_type = sig.return_annotation
        if return_type is not _empty:
            if not isinstance(result,return_type):
                raise TypeError(f"typeCheck: type({result!r}) !+ {return_type!r}")
        return result
    return inner



