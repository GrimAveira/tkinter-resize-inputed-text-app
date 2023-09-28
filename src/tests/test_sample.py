import pytest
from app import MyApp

class MockEventKeyCode:
    def __init__(self, keycode):
        self.keycode=keycode

@pytest.fixture(scope="module")
def app():
    app = MyApp()
    yield app

def test_entry_handler(app):
    with pytest.raises(ValueError):
        app.entry_handler(-1)
def test_font_increase(app):
    fontSize=app._fontSize
    app.resize_font_size(MockEventKeyCode(37))
    assert app._fontSize==fontSize/2
def test_font_decrease(app):
    fontSize=app._fontSize
    app.resize_font_size(MockEventKeyCode(39))
    assert app._fontSize==fontSize*2