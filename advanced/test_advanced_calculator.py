import pytest

from advanced_calculator import power, is_prime


def test_power():
    """Test for the power function"""
    assert power(2, 3) == 8
    assert power(3, 3) == 27

@pytest.mark.parametrize(
        "n, expected", 
        [
            pytest.param(1, False, id="1"),
            pytest.param(2, True, id="2"),
            pytest.param(-1, False, id="-1"),
            pytest.param(5, True, id="5"),
            pytest.param(27644437, True, id="27644437"),
            pytest.param(100000000, False, id="100000000"),
        ]
)
def test_is_prime(n, expected):
    """Test for the is_prime function"""
    assert is_prime(n) == expected
