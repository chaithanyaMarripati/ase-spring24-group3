import src.ROW as ROW

def testcase():
    row = ROW.ROW(None)
    assert row.cells == None
    assert row.k == 1

testcase()