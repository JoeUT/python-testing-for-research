from math import fabs, isclose
import random
import pytest

from estimate_pi import estimate_pi

@pytest.fixture
def est_pi():
    random.seed(0)
    iterations = 10000
    pi_estimate = estimate_pi(iterations)
    return pi_estimate

def test_estimate_pi(est_pi, snaptolshot):
    random.seed(0)
    iterations = 1000000

    pi_estimate = estimate_pi(iterations)

    expected = 3.141592654
    rtol = 5e-3
    atol = 1e-2

    assert fabs((pi_estimate - expected) / expected) < rtol
    assert fabs(pi_estimate - expected) < atol
    assert isclose(pi_estimate, expected, rel_tol=rtol, abs_tol=atol)

def test_estimate_pi_low_tolerance(est_pi, snaptolshot):
    rtol = 1e-7
    atol = 0.0

    with pytest.raises(AssertionError):
        snaptolshot.assert_allclose(est_pi, rtol=rtol, atol=atol)

def test_estimate_pi_high_tolerance(est_pi, snaptolshot):
    rtol = 1e-3
    atol = 0.0

    snaptolshot.assert_allclose(est_pi, rtol=rtol, atol=atol)
