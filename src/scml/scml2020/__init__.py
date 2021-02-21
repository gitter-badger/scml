"""Implements the SCML 2020 world design.

The detailed description of this world simulation can be found here_.

.. _here: http://www.yasserm.com/scml/scml2020.pdf

"""

from .common import *
from .factory import *
from .awi import *
from .world import *
from .agent import *
from .components import *
from .agents import *
from . import utils
from .utils import *

__all__ = (
    common.__all__
    + agents.__all__
    + world.__all__
    + components.__all__
    + factory.__all__
    + awi.__all__
    + agent.__all__
    + ["utils"]
)
