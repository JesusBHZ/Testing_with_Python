from mayor import Mayor as m

class TestMayor:
    def test_mayor1(self):
        assert m.mayor(self,2,1) == 2
    def test_mayor2(self):
        assert m.mayor(self,1,2) == 2

    def test_mayor3(self):
        assert m.mayor(self,2,2) == None

    def test_mayor4(self):
        assert m.mayor(self,1,-1) == 1  

    def test_mayor5(self):
        assert m.mayor(self,1,-1) == 1  

    def test_mayor6(self):
        assert m.mayor(self,-1,-1) == None  

    def test_mayor7(self):
        assert m.mayor(self,-1,-2) == -1

    def test_mayor8(self):
        assert type(m.mayor(self,-2,-1)) == int
        
    def test_mayor9(self):
        assert type(m.mayor(self,"q",1)) == str
        
    def test_mayor10(self):
        assert type(m.mayor(self,-2,"t")) == str
        
    def test_mayor11(self):
        assert type(m.mayor(self,2.1,2)) == float

    def test_mayor12(self):
        assert type(m.mayor(self,2,1.2)) == int
        
    def test_mayor13(self):
        assert type(m.mayor(self,2.2,"2")) == str

    def test_mayor14(self):
        assert type(m.mayor(self,"1",1)) == str
    
    
""" py -m pytest -v test """