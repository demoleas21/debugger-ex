import sys
import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:

    pdb.set_trace()

    print "To exit this game type 'exit'\n"
    num1 = choice(random2)
    num2 = choice(random1)
    answer = raw_input("What is {} times {}? ".format(num1, num2))

    if answer == 'exit':
        print "Now exiting game!"
        sys.exit()

    elif int(answer) == num1 * num2:
        print "Correct!\n"
    else:
        print "Wrong!\n"
