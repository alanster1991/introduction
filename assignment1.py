#print all integers from 0 to 150
for num in range(0, 151):
    print(num)


#print all the multiples of 5 from 5 to 1000
for num in range(5,1001):
    if num % 5 == 0:
        print(num)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


#Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for num in range(0, 500001):
    if num % 2 != 0:
        total += num
print(total)
    
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for num in range(2018, 0, -4):
    print(num)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(lowNum, highNum, mult):
    for num in range(lowNum, highNum+1, mult):
        print(num+1)

print(flexible_counter(2,9,3))