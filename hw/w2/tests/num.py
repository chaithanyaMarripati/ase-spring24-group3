from src.NUM import NUM
def test():
    # testcase 0
    num = NUM()
    assert num.n == 0
    num.add("?")
    assert num.n == 0

    #testcase 1, checking div function
    assert num.div() == 0
    num.n = 2
    num.m2 = 4
    assert num.div() == 2

    #testcase 2, checking norm function
    assert num.norm("?") == "?"

    #testcase 3, checking mid function
    assert num.mid() == 0

test()
