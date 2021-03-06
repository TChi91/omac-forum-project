class ATM:

    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance
        self.withdrawals_list = []

    def withdraw(self, request):
        print "======================================"
        print "Welcome to" + self.bank_name
        print "current balance is " + str(self.balance)
        print "======================================"
        if request > self.balance:
            print "we can't give more than " + str(self.balance)
        elif request <= 0:
            print "request is not valide"
        else:
            self.balance -= request
            self.withdrawals_list.append(request)
            while request > 0:
                if request >= 100:
                    print "give 100"
                    request -= 100

                elif request >= 50:
                    print "give 50"
                    request -= 50

                elif request >= 10:
                    print "give 10"
                    request -= 10

                elif request >= 5:
                    print "give 5"
                    request -= 5

                else:
                    print "give " + str(request)
                    request -= request

        return self.balance

    def show_withdrawals(self):
        print "======================================"
        print "withdrawals of " + self.bank_name
        print "======================================"
        for withdrawal in self.withdrawals_list:
            print withdrawal

atm1 = ATM("Smart Bank", 500)
atm2 = ATM("Baraka Bank", 1000)

atm1.withdraw(5555)
atm1.withdraw(100)
atm1.withdraw(55)


atm2.withdraw(100)
atm2.withdraw(300)

atm1.show_withdrawals()
atm2.show_withdrawals()