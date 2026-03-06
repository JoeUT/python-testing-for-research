import random
import pytest

@pytest.fixture
def estimate_pi():
    iterations = 1000000
    num_inside = 0
    for _ in range(iterations):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            num_inside += 1
    return 4 * num_inside / iterations

def test_pi_passes(snaptolshot, estimate_pi):
    # Passes due to loose tolerance.
    snaptolshot.assert_allclose(estimate_pi, rtol=1e-03, atol=0.0)

def test_pi_fails(snaptolshot, estimate_pi):
    # Fails due to tight tolerance.
    with pytest.raises(AssertionError):
        snaptolshot.assert_allclose(estimate_pi, rtol=1e-04, atol=0.0)