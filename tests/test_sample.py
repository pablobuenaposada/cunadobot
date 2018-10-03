def test_name():
    # Just asserts that this file exists
    assert __name__ == "test_sample"
    assert test_name.__name__ == "test_name"
