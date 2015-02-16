def closest(lst):
    """ input - a list of integers.
        output - the element that closest to the mean value.
        If two elements have the same difference the lower returned. """
    closestEl = None
    if len(lst) == 0:
        return closestEl
    mean = sum(lst)/float(len(lst))
    print "the mean value:", mean
    for elem in lst:
        if closestEl == None or (abs(mean-elem) < abs(closestEl-mean)):
            closestEl = elem
        elif abs(mean-elem) == abs(mean-closestEl):
            if elem < closestEl:
                closestEl = elem
    return closestEl

lst1 = [1,2,2,2,3]
ans = closest(lst1)
test_value = 2
print str(ans) + ". Is correct:", ans == test_value
print
lst1 = []
ans = closest(lst1)
test_value = None
print str(ans) + ". Is correct:", ans == test_value
print
lst1 = [1]
ans = closest(lst1)
test_value = 1
print str(ans) + ". Is correct:", ans == test_value
print
lst1 = [13,4,7,9,0,1,3,4]
ans = closest(lst1)
test_value = 4
print str(ans) + ". Is correct:", ans == test_value
print
lst1 = [6,3,4,8,4]
# mean = 5; 6 and 4 have the same difference, 4 should be returned.
ans = closest(lst1)
test_value = 4
print str(ans) + ". Is correct:", ans == test_value
