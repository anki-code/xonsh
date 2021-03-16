# -*- coding: utf-8 -*-
"""Testing for ``xonsh.shell.Shell``"""
import os

from xonsh.environ import Env
from xonsh.shell import Shell
from xonsh.history.json import JsonHistory
from xonsh.history.sqlite import SqliteHistory
from xonsh.history.dummy import DummyHistory


def test_shell_with_json_history(xonsh_builtins, xonsh_execer, tmpdir_factory):
    """
    Check that shell successfully load JSON history from file.
    """
    tempdir = str(tmpdir_factory.mktemp("history"))

    history_file = os.path.join(tempdir, 'history.json')
    h = JsonHistory(filename=history_file)
    h.append({"inp": "echo Hello world 1\n", "rtn": 0, "ts": [1615887820.7329783, 1615887820.7513437]})
    h.append({"inp": "echo Hello world 2\n", "rtn": 0, "ts": [1615887820.7329783, 1615887820.7513437]})
    h.flush()

    xonsh_builtins.__xonsh__.env = Env(
        XONSH_DATA_DIR=tempdir,
        XONSH_INTERACTIVE=True,
        XONSH_HISTORY_BACKEND='json',
        XONSH_HISTORY_FILE=history_file,
        # XONSH_DEBUG=1  # to show errors
    )

    Shell(xonsh_execer, shell_type='none')

    assert len([i for i in xonsh_builtins.__xonsh__.history.all_items()]) == 2


def test_shell_with_sqlite_history(xonsh_builtins, xonsh_execer, tmpdir_factory):
    """
    Check that shell successfully load SQLite history from file.
    """
    tempdir = str(tmpdir_factory.mktemp("history"))

    history_file = os.path.join(tempdir, 'history.db')
    h = SqliteHistory(filename=history_file)
    h.append({"inp": "echo Hello world 1\n", "rtn": 0, "ts": [1615887820.7329783, 1615887820.7513437]})
    h.append({"inp": "echo Hello world 2\n", "rtn": 0, "ts": [1615887820.7329783, 1615887820.7513437]})
    h.flush()

    xonsh_builtins.__xonsh__.env = Env(
        XONSH_DATA_DIR=tempdir,
        XONSH_INTERACTIVE=True,
        XONSH_HISTORY_BACKEND='sqlite',
        XONSH_HISTORY_FILE=history_file,
        # XONSH_DEBUG=1  # to show errors
    )

    Shell(xonsh_execer, shell_type='none')

    assert len([i for i in xonsh_builtins.__xonsh__.history.all_items()]) == 2


def test_shell_with_dummy_history_in_not_interactive(xonsh_builtins, xonsh_execer):
    """
    Check that shell use Dummy history in not interactive mode.
    """
    xonsh_builtins.__xonsh__.env = Env(XONSH_INTERACTIVE=False)
    xonsh_builtins.__xonsh__.history = None
    Shell(xonsh_execer, shell_type='none')
    assert isinstance(xonsh_builtins.__xonsh__.history, DummyHistory)
