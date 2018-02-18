money = 500
request = 278
if request > money:
    print "we can't give more than" + str(money)
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
