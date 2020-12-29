##Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

##Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

 = int(input('please enter a  positive number: '))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
        steps += 1
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        print(c0)
        steps += 1
        
print('steps taken: ', steps)