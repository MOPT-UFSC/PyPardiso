# coding: utf-8
from importlib.metadata import version, PackageNotFoundError

from .pardiso_wrapper import PyPardisoSolver, Matrix_type


try:
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ['PyPardisoSolver', 'Matrix_type']
