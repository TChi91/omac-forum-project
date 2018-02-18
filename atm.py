money = 500
request = 275
if request > money:
    print "we can't give more than 500$"
else:
    while request > 0:
        if request >= 100:
            request -= 100
            print "give 100"

        if request >= 50 and request < 100:
            request -= 50
            print "give 50"

        if request >= 10 and request < 50:
            request -= 10
            print "give 10"

        if request >= 5 and request < 10:
            request -= 5
            print "give 5"

        if request < 5 and request > 0:
            print "give " + str(request)
            request -= request
