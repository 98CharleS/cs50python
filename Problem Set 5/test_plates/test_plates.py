from plates import is_valid

def test_is_valid():
    assert is_valid("K2") == False
    assert is_valid("22") == False
    assert is_valid("2K") == False
    assert is_valid("00EZ") == False
    assert is_valid("10EZ") == False
    assert is_valid("EZ00") == False
    assert is_valid("EZPZ") == True
    assert is_valid("EZ.PZ") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("NRVOUS") == True
    assert is_valid("NRVOUSABCABC") == False
