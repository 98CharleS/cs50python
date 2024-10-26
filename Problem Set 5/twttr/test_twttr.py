import twttr

def test_shorten():
    assert twttr.shorten("test") == "tst"
    assert twttr.shorten("Test") == "Tst"
    assert twttr.shorten("12test") == "12tst"
    assert twttr.shorten("12, test") == "12, tst"
    assert twttr.shorten("Atest") == "tst"
