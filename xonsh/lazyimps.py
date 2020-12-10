"""Lazy imports that may apply across the xonsh package."""
import os
import importlib

# from xonsh.platform import ON_WINDOWS, ON_DARWIN
# from xonsh.lazyasd import LazyObject, lazyobject


# pygments = LazyObject(
#     lambda: importlib.import_module("pygments"), globals(), "pygments"
# )

import pygments

# pyghooks = LazyObject(
#     lambda: importlib.import_module("xonsh.pyghooks"), globals(), "pyghooks"
# )

# import xonsh.pyghooks as pyghooks

# @lazyobject
# def pty():
#     if ON_WINDOWS:
#         return
#     else:
#         return importlib.import_module("pty")

import pty

# @lazyobject
# def termios():
#     if ON_WINDOWS:
#         return
#     else:
#         return importlib.import_module("termios")

import termios

# @lazyobject
# def fcntl():
#     if ON_WINDOWS:
#         return
#     else:
#         return importlib.import_module("fcntl")

import fcntl

# @lazyobject
# def tty():
#     if ON_WINDOWS:
#         return
#     else:
#         return importlib.import_module("tty")

import tty

# @lazyobject
# def _winapi():
#     if ON_WINDOWS:
#         import _winapi as m
#     else:
#         m = None
#     return m

_winapi = None

# @lazyobject
# def msvcrt():
#     if ON_WINDOWS:
#         import msvcrt as m
#     else:
#         m = None
#     return m
#

msvcrt = None
#
# @lazyobject
# def winutils():
#     if ON_WINDOWS:
#         import xonsh.winutils as m
#     else:
#         m = None
#     return m
#

winutils = None
#
# @lazyobject
# def macutils():
#     if ON_DARWIN:
#         import xonsh.macutils as m
#     else:
#         m = None
#     return m

macutils = None

# @lazyobject
# def terminal256():
#     return importlib.import_module("pygments.formatters.terminal256")

import pygments.formatters.terminal256 as terminal256

# @lazyobject
# def html():
#     return importlib.import_module("pygments.formatters.html")

import pygments.formatters.html as html

# @lazyobject
# def os_listxattr():
#     def dummy_listxattr(*args, **kwargs):
#         return []
#
#     return getattr(os, "listxattr", dummy_listxattr)

from os import listxattr as os_listxattr