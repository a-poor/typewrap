# Type-Wrap

_created by Austin Poor_

Super tiny python package for function typechecking.


## Installation

Install with pip

```bash
$ pip install typewrap
```

## Usage

There's only one function in the package, `typeCheck`,  a decorator function that checks the function input and outputs against the function annotations.

Example:

```python
from typewrap import typeCheck

def add_noChecks(a: int, b: int) -> int:
    """Has annotations but doesn't
    check argument types."""
    return a + b

@typeCheck
def add_checkInputs(a: int, b: int) -> int:
    return a + b

@typeCheck
def add_checkOutputs(a: int, b: int) -> int:
    return float(a+b)

# Unwrapped function with 
# uninforced type annotations
add_noChecks(1,2.0) # No errors


# Wrapped function with bad
# input arguments
add_checkInputs(1,2.0) # Raises TypeError


# Wrapped function with
# bad output type
add_checkOutputs(1,2) # Raises TypeError
```







