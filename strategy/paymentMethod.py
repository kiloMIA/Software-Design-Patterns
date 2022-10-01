from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def deposit(self,money,periodOfTime):
        pass

class Kaspi(PaymentMethod):
    def deposit(self,money,periodOfTime):
        InterestRate = 2,5
        return money * (periodOfTime/365) * InterestRate
    
class Halyk(PaymentMethod):
    def deposit(self,money,periodOfTime):
        InterestRate = 1,5
        return money * (periodOfTime/365) * InterestRate

class Jusan(PaymentMethod):
    def deposit(self,money,periodOfTime):
        InterestRate = 3
        return money * (periodOfTime/365) * InterestRate
        
       
       
    
#class cash():
 #   failureCounter = 0
  #  def operation(self, durability, valid):
   #     if durability < 50:
    #        print("Paper is fractioned beyond believe, we can't accept it ")
     #       failureCounter += 1     
      #  if valid == False:
       #     print("This bill is fabricated by unauthorized party, you're going to face the law in all it's harshness")
        #    failureCounter += 1  
        #return failureCounter

        

 

   