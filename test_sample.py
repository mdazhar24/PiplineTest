import pytest
import pdb
import pytest_xray

@pytest.mark.xray(test_key="T3-1", test_exec_key="T3-1")
def test_my_function():
assert True == False

@pytest.mark.xray(test_key="T3-2", test_exec_key="T3-2")
def test_my_function1():
assert True == True

@pytest.mark.xray(test_key="T3-3", test_exec_key="T3-3")
def test_my_function2():
assert True == False
