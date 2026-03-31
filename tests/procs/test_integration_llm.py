"""Integration tests that run xonsh in a subprocess.

These tests spawn a real xonsh process so that signals, process groups,
and job control behave exactly as they would for a user.
"""

import os
import signal
import subprocess
import sys
import textwrap

import pytest

from xonsh.pytest.tools import skip_if_on_windows

SIGINT_PIPELINE_CASES = {
    "two_stage": (
        "!(sleep 100 | echo 42).out",
        "42",
    ),
    "three_stage": (
        textwrap.dedent("""\
            try:
                r = !(echo 42 | sleep 100 | echo 43)
                r.out
            except:
                pass
            print(repr(r.out))
        """),
        "43",
    ),
    "callable_alias_last": (
        textwrap.dedent("""\
            aliases['my42'] = lambda: "42\\n"
            try:
                r = !(sleep 100 | my42)
                r.out
            except:
                pass
            print(repr(r.out))
        """),
        "42",
    ),
    "callable_alias_first": pytest.param(
        textwrap.dedent("""\
            aliases['mysleep'] = lambda: __import__('time').sleep(100)
            try:
                r = !(mysleep | echo 42)
                r.out
            except:
                pass
            print(repr(r.out))
        """),
        "42",
        marks=pytest.mark.xfail(
            reason="callable alias blocking in non-main thread "
            "cannot be interrupted by SIGINT"
        ),
    ),
}


@skip_if_on_windows
@pytest.mark.parametrize(
    "code, expected",
    SIGINT_PIPELINE_CASES.values(),
    ids=SIGINT_PIPELINE_CASES.keys(),
)
def test_sigint_pipeline_preserves_output(code, expected):
    """SIGINT during a pipeline should not lose already-produced output."""
    proc = subprocess.Popen(
        [sys.executable, "-m", "xonsh", "--no-rc", "--no-env", "-c", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
    )
    try:
        proc.wait(timeout=1)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGINT)

    stdout, stderr = proc.communicate(timeout=10)
    output = stdout.decode() + stderr.decode()
    assert expected in output, f"expected {expected!r} in output, got:\n{output}"
