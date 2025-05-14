import importlib
import sys

from . import typing_help
from . import timeit


# needed if running in a continuously running IPython kernel
importlib.reload(typing_help)
importlib.reload(timeit)

from .timeit import *

if "numpy" in sys.modules:
    """
    from .numpy_dependent_subfolder import some_module
    # needed if running in a continuously running IPython kernel
    importlib.reload(some_module)
    from .numpy_dependent_subfolder.some_module import some_func, some_var
    """
    pass
    
