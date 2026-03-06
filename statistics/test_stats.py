import random
import numpy as np
import pytest

import stats

@pytest.fixture
def participants():
    participants = [
        {"age": 25, "height": 180},
        {"age": 30, "height": 170},
        {"age": 35, "height": 160},
    ]
    return participants

def test_get_indexes_to_sample():
    total_participants = 10
    sample_size = 5
    random.seed(0)  # Set seed for reproducibility

    indexes = stats.get_indexes_to_sample(total_participants, sample_size)

    assert len(indexes) == sample_size
    assert all(index < total_participants for index in indexes)
    assert indexes == [6, 9, 0, 2, 4]  # Expected output with seed 0

def test_sampled_participants(participants):
    indexes = [0, 2]

    sampled_participants = stats.get_sampled_participants(participants, indexes)

    assert len(sampled_participants) == len(indexes)
    assert sampled_participants == [
        {"age": 25, "height": 180},
        {"age": 35, "height": 160},
    ]


def test_filter_by_age(participants):
    min_age = 26
    max_age = 34

    filtered_participants = stats.filter_by_age(participants, min_age, max_age)

    assert len(filtered_participants) == 1
    assert filtered_participants == [
        {"age": 30, "height": 170},
    ]

def test_filter_by_height(participants):
    min_height = 165
    max_height = 175

    filtered_participants = stats.filter_by_height(participants, min_height, max_height)

    assert len(filtered_participants) == 1
    assert filtered_participants == [
        {"age": 30, "height": 170},
    ]

def test_randomly_sample_and_filter_participants(participants):
    sample_size = 2
    min_age = 26
    max_age = 34
    min_height = 165
    max_height = 175

    random.seed(0)  # Set seed for reproducibility

    filtered_participants = stats.randomly_sample_and_filter_participants(
        participants,
        sample_size,
        min_age,
        max_age,
        min_height,
        max_height
    )

    assert len(filtered_participants) == 1
    assert filtered_participants == [
        {"age": 30, "height": 170},
    ]

def test_calculate_cumulative_sum():
    array_ints = np.array([1, 2, 3, 4])
    cumulative_sum_ints = stats.calculate_cumulative_sum(array_ints)

    assert len(cumulative_sum_ints) == len(array_ints)
    np.testing.assert_array_equal(cumulative_sum_ints, np.array([1, 3, 6, 10]))

    array_floats = np.array([1.5872352, 2.29875823, 3.8623852])
    cumulative_sum_floats = stats.calculate_cumulative_sum(array_floats)

    assert len(cumulative_sum_floats) == len(array_floats)
    np.testing.assert_allclose(cumulative_sum_floats, np.array([1.5872352, 3.88599343, 7.74837863]))