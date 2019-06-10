

l=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

X = int(input("please enter X value to check if it is in range of 10 - 50"))

a = (X in l)
print(a)

if (a is True) :
    print("YES i am in range")

if (a is False) :
    print ("Oops")    
