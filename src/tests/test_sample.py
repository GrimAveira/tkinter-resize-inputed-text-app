import pytest
from src.main import MyApp

def entry_handler(value):
    if int (value)<0:
        raise ValueError()

def test_answer():
    with pytest.raises(ValueError):
        entry_handler(-1)