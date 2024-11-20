import main
def test_add():
    assert main.add(2,3)==5
    assert main.add(-1,1)==0
def test_subtract():
    assert main.subtract(5,3)==2
    assert main.subtract(0,1)==-1   
