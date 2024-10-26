from um import count

def test_response():
    assert count("Um um") == 2
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("um, thanks, um...") == 2
    assert count(" ") == 0
