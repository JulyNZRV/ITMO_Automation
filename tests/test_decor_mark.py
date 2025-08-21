import pytest


@pytest.mark.smoke
def test_decor_mark1():
    assert True

@pytest.mark.regress
def test_decor_mark2():
    assert True

@pytest.mark.regress
def test_decor_mark3():
    assert True

@pytest.mark.regress
def test_decor_mark4():
    assert True

