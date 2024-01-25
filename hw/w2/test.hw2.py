from src.NUM import NUM
from src.ROW import ROW
from src.SYM import SYM


def sym_test():
    #testcase 0
    sym =SYM()
    assert sym.mid() == None
    assert sym.most == 0
    assert sym.m == 0
    assert sym.small() == 0

    sym = SYM()
    vals = [2,3,5,5,5,5,6]
    for val in vals:
        sym.add(val)
    assert sym.mid() == 5
    assert sym.mode == 5

    #testcase 1
    sym1 = SYM("Hello")
    assert sym1.txt == "Hello"
    assert sym1.n == 0
    # '?' will not get added
    sym1.add("?")
    assert sym1.n == 0
    sym1.add("34")
    assert sym1.n == 1
    

def row_test():
    row = ROW(None)
    assert row.cells == None
     

def num_test():
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

    #testcase 4, checking mid for different values
    num2 = NUM()
    initSum =0 
    values = [5,5,5,5]
    for val in values:
        num2.add(val)
        initSum+=val
    expectedMean= initSum/len(values)

    assert expectedMean == num2.mid()
    

    #testcase 5, checking low for the stream
    num2 = NUM()
    values = [1,2,-2,89]
    for val in values:
        num2.add(val)
    
    assert -2 == num2.lo




sym_test()
row_test()
num_test()