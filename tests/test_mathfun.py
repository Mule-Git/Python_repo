import mathfun.myfun
from mathfun.my_fun_p import comp
import pytest
from unittest import mock



@mock.patch('mathfun.my_fun_p.pow')
def test_comp(mock_pow):
    mock_pow.return_value = 3
    result = comp(0,4)
    assert result == '4 is postive'
    mock_pow.assert_called_once()






@pytest.mark.xfail
def test_int_adding():
    result = mathfun.myfun.adding(2, 4)

    assert result == 6

def test_str_adding():
    result = mathfun.myfun.adding("mule","wol")
    assert type(result) is str
    assert result == "mulewol"

def test_float_adding():
    result = mathfun.myfun.adding(2.2, 4.2)

    assert result == 6.4


