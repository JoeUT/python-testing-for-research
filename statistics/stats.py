import random
import numpy as np

def get_indexes_to_sample(total_participants: int, sample_size: int):
    """Get the indexes to sample from the total participants"""
    return random.sample(range(total_participants), sample_size)

def get_sampled_participants(participants: list, indexes: list):
    """Get the sampled participants from the total participants using the indexes"""
    sampled_participants = []
    for i in indexes:
        sampled_participants.append(participants[i])
    return sampled_participants

def filter_by_age(participants: list, min_age: int, max_age: int):
    """Remove participants that are outside the age range"""
    filtered_participants = []
    for participant in participants:
        if participant["age"] >= min_age and participant["age"] <= max_age:
            filtered_participants.append(participant)
    return filtered_participants

def filter_by_height(participants: list, min_height: int, max_height: int):
    """Remove participants that are outside the height range"""
    filtered_participants = []
    for participant in participants:
        if participant["height"] >= min_height and participant["height"] <= max_height:
            filtered_participants.append(participant)
    return filtered_participants

def randomly_sample_and_filter_participants(
        participants: list,
        sample_size: int,
        min_age: int,
        max_age: int,
        min_height: int,
        max_height: int
):
    """Participants is a list of dicts, containing the age and height of each participant
    participants = [
        {"age": 25, "height": 180},
        {"age": 30, "height": 170},
        {"age": 35, "height": 160},
    ]
    """

    # Get the indexes to sample
    indexes = get_indexes_to_sample(len(participants), sample_size)

    # Get the sampled participants
    sampled_participants = get_sampled_participants(participants, indexes)

    # Remove participants that are outside the age range
    sampled_participants_age_filtered = filter_by_age(sampled_participants, min_age, max_age)

    # Remove participants that are outside the height range
    sampled_participants_height_filtered = filter_by_height(sampled_participants_age_filtered, min_height, max_height)

    return sampled_participants_height_filtered

def calculate_cumulative_sum(array: np.ndarray) -> np.ndarray:
    """Calculate the cumulative sum of a numpy array"""
    
    result = np.zeros(array.shape)
    result[0] = array[0]
    for i in range(1, len(array)):
        result[i] = result[i-1] + array[i]

    return result
