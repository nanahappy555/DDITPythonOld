from astropy.io.fits.util import first
from Cython.Compiler.Naming import self_cname
class Xi:
    def __init__(self):
        self.money = 1000
    
    def steal(self,smoney):
        self.money += smoney
        
class Putin:
    def __init__(self):
        self.nuclear = 5000
    
    def alzheimer(self):
        self.nuclear -= 1

class Jungeun:
    def __init__(self):
        self.missile = 10000
        
    def ssorau(self):
        self.missile -= 100
        
class Sungwoo(Xi, Putin, Jungeun):
    """
    파이썬에서는 다중상속이 가능하다. 
    시진핑,푸틴,정은을 상속하는 클래스 성우를 작성하라
    """
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        Jungeun.__init__(self)
        self.knowledge = 100
    
    def study(self, first):
        self.knowledge += first
        

a = Sungwoo()
print(a.nuclear)
print(a.money)
print(a.missile)
print(a.knowledge)
