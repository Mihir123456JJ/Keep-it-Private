class privacy:
    __Var1=1234
    def __Var2(self):
        print("THis function is in private class")
    def hello(self):
        print("Private varibal is:",privacy.__Var1)  
pin=privacy()
pin.hello()
pin.__Var1
         