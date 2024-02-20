from NUM import NUM
from SYM import SYM
from statistics import mode

def testNUMmid():
    num = NUM()
    toBeAdded = [2, 3, 4, 5, 6]
    for nums in toBeAdded:
        num.add(nums)

    finalMean = 0

    for val in toBeAdded:
        finalMean += val
    finalMean /= len(toBeAdded)
    assert num.mid() == finalMean


def testLow():
    num = NUM()
    toBeAdded = [1, 2, 3, 4, 99]
    for val in toBeAdded:
        num.add(val)
    assert num.lo == min(toBeAdded)


def testWithEmpty():
    sym = SYM()
    res = sym.div()
    assert res == 0


def testWithManyvalues():
    sym = SYM()
    sym.add("1")
    sym.add("2")
    sym.add("3")
    res = sym.div()
    assert res > 0

def test_sym_mid():
    sym = SYM()
    vals = [1,1,1,1,1,1,1,199,99,9,99,99,9,99]
    for val in vals:
        sym.add(val)
    mid = mode(vals)
    assert sym.mid() == mid

    sym = SYM()
    vals = [22,2,2]
    for val in vals:
        sym.add(val)
    mid = mode(vals)
    assert sym.mid() == mid

testNUMmid()
testLow()
testWithEmpty()
testWithManyvalues()
