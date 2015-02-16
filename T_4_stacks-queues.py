class Stack(object):
    def __init__(self):
        self.que =[]
    def push(self, item):
        self.que.insert(0, item)
    def __str__(self):
        res = ""
        for i in self.que:
            res += str(i)+' '
        return "The stack is: " +'['+res[:-1]+']'
    def clear(self):
        self.que = []
    def pop(self):
        if len(self.que) == 0:
            return None
        return self.que.pop(0)
    def getstack(self):
        return self.que[:]
# create two Stack objects s1 & s2
s1 = Stack()
s2 = Stack()
s1.push(1)
s1.push(10)
s1.push(7)
print s1
test = str(s1)
print "should print:\n  The stack is: [7 10 1]"
print "s1 & s2 creation, filling and printing tests are passed:",test == "The stack is: [7 10 1]"
print
print "Test of pop() method:"
a = s1.pop()
print a
print "should print: 7"
print "Is test passed:", a == 7
print
print "Remaining items are:"
print s1
print "should print: [10 1]"
print
print "Testing of the push() method of Stack object:"
s1.push(20)
s1.push(30)
s1.push(40)
print s1
print "should print: [40 30 20 10 1]"
print
class Queue(object):
    def __init__(self,s1,s2):
        self.stack_1 = s1
        self.stack_2 = s2

    def add(self, item):
        #length = len("The stack is: " + '[' +']')+len(' '*(len(self.stack_1.que)*2-1))
        #print "length=", length
        #print "stack #1:", '{:<35}'.format(self.stack_1), "stack #2:", self.stack_2
        if self.stack_1.que == []:
            
            if self.stack_2.que != [] :
                
                while True:
                    itm = self.stack_2.pop()
                    if itm == None:
                        break
                    self.stack_1.push(itm)
            self.stack_1.push(item)
        elif self.stack_1 != []:
            self.stack_1.push(item)
    def clear(self):
        self.stack_1.clear()
        self.stack_2.clear()
    def pull(self):
        while True:
            item = self.stack_1.pop()
            if item == None:
                break
            self.stack_2.push(item)
        return self.stack_2.pop()
    def __str__(self):
        res = self.stack_2.getstack()
        if res == [] and len(self.stack_1.getstack())> 0:
            res = self.stack_1.getstack()
            res.reverse()
        #res.reverse()
        r =''
        for i in res:
            r += str(i) +' '
        return "The queue is: "+ '['+r[:-1]+']'
# Creating testing items
queue1 = range(11)
queue1.reverse()
print "Testing items for Queue object are:"
print queue1
print
print "Creating a Queue object using s1 & s2 Stack objects"
q1 = Queue(s1, s2)
print 
print q1
print
b=q1.pull()
print "pulling 1:"
print b
print q1
print
b=q1.pull()
print "pulling 10:"
print b
print
b=q1.pull()
print "pulling 20:"
print b
print
b=q1.pull()
print "pulling 30:"
print b
print
print "The queue is now:"
print q1
print "Check if the s1 now is empty list:"
print q1.stack_1.que
print
q1.add(41)
print "the queue after adding 41:"
print q1
print "Internal Stack object representation:"
print q1.stack_1.que
print
print "Testing"
q1.clear()
print q1
print
print "Test #1:"
# Test #1 describes the situation when the item filled completely,
# then all of them are pulled out. 
test_input = range(11)
test_output = list(test_input)
print "The input is {}.\nShould print this: {}"\
      .format(test_input, ' '.join(map(str,test_output)))
for item in test_input:
    q1.add(item)
while True:
    result = q1.pull()
    if result == None:
        break
    print result,
print
print q1

print
print "Test #2:"
# Test #2 describes the situation when the items filled partially,
# then several items are pulled out and after this new item added and
# then pulled out again until the last one.
test_input = range(11) + [33, 44, 55]
test_output = [5, 6, 7, 8, 9, 10, 33, 44, 55]
print "The input is {}.\nShould print this: \n first line: 0 1 2 3 4\n second line: {}"\
      .format(test_input, ' '.join(map(str,test_output)))
for item in test_input:
    q1.add(item)
print
print "The intermediate result (after pulling out first 5 items:"
for i in range(5):
    result = q1.pull()
    if result == None:
        break
    print result,
print
print
print q1
print "Adding another items."
another_items = [33, 44, 55]
for j in range(len(another_items)):
    q1.add(another_items[j])
print q1
print
print "The Final result:"
while True:
    result = q1.pull()
    if result == None:
        break
    print result,
print
print
print q1
