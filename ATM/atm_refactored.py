balance = 500

def withdraw(balance, request):
    print ""
    print "current balance is " + str (balance)
    if request > balance:
        print "we can't give more than " + str(balance)
    elif request <= 0:
        print "request is not valide"
    else:
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
            balance -= request
    return balance



balance = withdraw(balance, 277)

balance = withdraw(balance, 30)

balance = withdraw(balance, 5)

balance = withdraw(balance, 500)
