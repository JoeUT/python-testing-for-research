SNAPSHOT_DATA = 615370469611.9492

def very_complex_processing(data):
    # Simulate a complex processing task
    result = 0
    for i in range(1000000):
        result += (i * data) % 1234567
    return result

def test_something():
    input_data = 42.1238421

    processed_data = very_complex_processing(input_data)

    print(processed_data)
    assert processed_data == SNAPSHOT_DATA  # Expected output based on the calculation above