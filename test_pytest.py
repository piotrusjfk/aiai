import main
import pytest

def test_v():
    assert main.V(120, 2) == 60

def test_suma():
    assert main.suma(2, 2) == 4