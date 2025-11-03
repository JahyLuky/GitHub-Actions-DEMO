from src.main import hello

def test_hello():
    assert hello("Paul") == "Hello, Paul!"

def test_hello_empty():
    assert hello("") == "Hello, !"

def test_hello_none():
    assert hello(None) == "Hello, None!"
