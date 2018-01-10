
#1) Print 1-255.
def tr():
    for x in range(1,256):
        print x 
tr()



#2) Print Ints and Sum 0 - 255.
def ATK():
    sum=0
    for x in range (0, 255+1):
        sum += x
        print sum
ATK()


#3) Find and Print Max.
list=[1,5,21,75,12,84]

def MIK(list):
    max = list[0]
    for x in range(0, len(list)):
        if list[x] > max:
            max = list[x]
    print max

MIK(list)


#4) Array with Odds.
def tab():
    for x in range(1,256, 2):
        print x
tab() 


#5) Greater than Y.
list=[1,5,21,75,12,84]
def y2k(list):
    count = 0
    for x in range(0, len(list)):
        if list[x] > count:
            count +=1
    print x

y2k(list)


#6) Max, Min Average.
list=[1,5,21,75,12,84]
def mma(list):
    max = 0
    min = list[0]
    sum = 0
    for x in range(0, len(list)):
        if list[x] > max:
            max = list[x]
        if list[x] < min:
            min = list[x]
        sum += list[x]
    average = sum / len(list)
    print (min, max, average)

mma(list)

#7) Swap String for Array of Negative Values.
list=[1, -5,21,75,-12,-84]
def swap(list):
    for x in range(0,len(list)):
        if list[x] <0:
            list[x] = "negative"
    print list
swap(list)           

#8) Print Odds 1-255.
def odds():
    for x in range(1, 256, 2):
        print x

odds()



#9) Iterate and Print Array
list=[1, 42, 12, 63, 74, 23, 62, 14]

def it(list):
    for x in range(0, len(list)):
        print list[x]
it(list) 



#10) Get and Print Average.
list=[1, 42, 12, 63, 74, 23, 62, 14]
def avg(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    average = sum / len(list)
    print average

avg(list) 


#11) Square the Values.
list=[1, 42, 12, 63, 74, 23, 62, 14]
def square(list):
    for x in range(0, len(list)):
        list[x] = list[x] * list[x]
    print list

square(list)


#12) Zero Out Negative Numbers.
list=[1, -5, 21,75 ,-12 ,-84]
def zero(list):
    for x in range (0, len(list)):
        if list[x] < 0:
            list[x] = 0
    print list

zero(list)      


#13) Shift Array Values.
list=[1, 5, 21, 75, 12, 84]
def shift(list):
    for x in range(1, len(list)):
        list[x - 1] = list[x]
        if x == len(list) - 1:
            list[x] = 0
    print list

shift(list)