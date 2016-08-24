"""Event tests"""
import pytest
from xonsh.events import EventManager

@pytest.fixture
def events():
    return EventManager()

def test_event_calling(events):
    called = False

    @events.on_test
    def _(spam):
        nonlocal called
        called = spam

    events.on_test.fire("eggs")

    assert called == "eggs"

def test_event_returns(events):
    called = 0

    @events.on_test
    def on_test():
        nonlocal called
        called += 1
        return 1

    @events.on_test
    def second():
        nonlocal called
        called += 1
        return 2

    vals = events.on_test.fire()

    assert called == 2
    assert set(vals) == {1, 2}

def test_validator(events):
    called = None

    @events.on_test
    def first(n):
        nonlocal called
        called += 1
        return False

    @first.validator
    def v(n):
        return n == 'spam'

    @events.on_test
    def second(n):
        nonlocal called
        called += 1
        return False

    called = 0
    events.on_test.fire('egg')
    assert called == 1

    called = 0
    events.on_test.fire('spam')
    assert called == 2


def test_eventdoc(events):
    docstring = "Test event"
    events.doc('on_test', docstring)

    import inspect
    assert inspect.getdoc(events.on_test) == docstring
