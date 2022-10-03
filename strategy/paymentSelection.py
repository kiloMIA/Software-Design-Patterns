from paymentMethod import *

class paymentSelection:
    
    def __init__(self, paymentMethod):
        self._paymentMethod = paymentMethod
    
    def deposit(self, money, periodOfTime):
        return self._paymentMethod.deposit(money,periodOfTime)


if __name__ == '__main__':

    kaspi = Kaspi()
    payment_selection = paymentSelection(kaspi)
    print('You will gain: ', payment_selection.deposit(60,365))

    halyk = Halyk()
    payment_selection = paymentSelection(halyk)
    print('You will gain: ', payment_selection.deposit(60,365))

    jusan = Jusan()
    payment_selection = paymentSelection(jusan)
    print('You will gain: ', payment_selection.deposit(60,365))