from paymentMethod import *

class paymentSelection:
    
    def __init__(self, paymentMethod):
        self._paymentMethod = paymentMethod
    
    def deposit(self, money, periodOfTime):
        return self._paymentMethod(self,money,periodOfTime)
