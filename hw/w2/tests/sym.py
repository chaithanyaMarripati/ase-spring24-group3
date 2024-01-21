from src.SYM import SYM
def test():
    #testcase 0
    sym =SYM();
    assert sym.mid() == None
    assert sym.most == 0
    assert sym.m == 0
    assert sym.small() == 0
    

    #testcase 1
    sym1 = SYM("Hello")
    assert sym1.txt == "Hello"
    assert sym1.n == 0
    # '?' will not get added
    sym1.add("?")
    assert sym1.n == 0
    sym1.add("34")
    assert sym1.n == 1
    

test()
