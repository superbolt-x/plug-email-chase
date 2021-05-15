import pytest


def test_convert(capsys):
    """Correct my_name argument prints"""
    print("Test")
    captured = capsys.readouterr()
    assert "Test" in captured.out
