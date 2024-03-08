from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_mustBeChance():
        expected = 14
        actual = Yatzy.chance(1,1,3,3,6)
        assert expected == actual  

def test_mustBeYatzy():
        expected = 50
        actual = Yatzy.yatzy([1,1,1,1,1])
        assert expected == actual   
def mustBeYatzyFail():
        expected = 0
        actual = Yatzy.yatzy([1,1,1,1,5])
        assert expected == actual 

def test_mustBeOnes():
        expected = 5
        actual = Yatzy.ones(1,1,1,1,1)
        assert expected == actual

def test_mustBeTwos():
        expected = 10
        actual = Yatzy.twos(2,2,2,2,2)
        assert expected == actual
def test_mustBeThrees():
        expected = 15
        actual = Yatzy.threes(3,3,3,3,3)
        assert expected == actual
def test_mustBeFours():
        expected = 8
        actual = Yatzy.fours(2,2,2,2,0)
        assert expected == actual
def test_mustBeCrazyChangeImpar():
        expected = 10
        actual = Yatzy.crazyChange(1,1,1,1,1)
        assert expected == actual
def test_mustBeCrazyChangePar():
        expected = 30
        actual = Yatzy.crazyChange(2,2,2,2,2)
        assert expected == actual