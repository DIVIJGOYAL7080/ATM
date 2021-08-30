class Atm():
    def __init__(self, cardNumber, pinNumber, currentBalance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.currentBalance = currentBalance

    def printCardNUmber(self):
        print("Your Card Number Is " + str(self.cardNumber))

    def printPinNUmber(self):
        print("Your Pin Number Is " + str(self.pinNumber))

    def printcurrentBalance(self):
        print("Your Current Balance Is " + str(self.currentBalance))

card1 = Atm(4785, 123456, 100000)

card1.printCardNUmber()
card1.printPinNUmber()
card1.printcurrentBalance()