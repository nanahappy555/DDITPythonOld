import time
class Cat:
    def __init__(self):
        print("constructor")
    
    def cry(self):
        print("crying")
    
    def __del__(self):
        print("destroyer")
    
    # java의 toString
    def __str__(self):
        return "babo"

c = Cat()
c.cry()
time.sleep(4) # 4초 지연. 단위 sec
print(c)