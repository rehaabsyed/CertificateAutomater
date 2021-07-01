# code being tested
import math

def test_sqrt_0():
    assert math.sqrt(0) == 0.0

def test_sqrt_neg():
    try:
        num = math.sqrt(-1.0)
        assert False, "math.sqrt() did not fail when giving negative number"
    except Exception as err:
        assert isinstance(err, ValueError), "Exception not an AssertionError"

def test_sqrt_1():
    assert math.sqrt(1) == 1.0, "sqrt(1) must be exactly 1"

def test_sqrt_square_num():
    assert math.sqrt(9) == 3.0, "sqrt(9) must be exaclty 3"

def test_sqrt_smaller():
    assert 0.0 <= 0.5 <= math.sqrt(0.5), "sqrt(0.5) must be greater than 0.5"

def test_sqrt_larger():
    assert 1.0 <= math.sqrt(5) <= 5, "sqrt(5) must be less than 5"

def test_sqrt_dec():
    assert abs(math.sqrt(10) - 3.1623) < 0.0001, "sqrt(10) should be ~3.1623"

# This test will fail
def test_sqrt_fail():
    assert math.sqrt(4) == 4, "sqrt(4) must equal 4"