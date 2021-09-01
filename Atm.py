class Atm(object):
    def __init__(self,cardNumber,atmPin):
        self.cardNumber = cardNumber
        self.atmPin = atmPin

    def CashWithdrawal(self):
        print("Cash withdrawed...")

    def BalanceEnquiry(self):
        print("Yo currently have 100000 Rupees...")

details = Atm("A63K37KD037MGEX8","9247")
print(details.CashWithdrawal())
print(details.BalanceEnquiry())
