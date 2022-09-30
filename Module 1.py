import random  # defining the functions for generating and manipulating random integers
randlist=[] #define the list
for i in range(0,100):
    n=random.randint(0,100) #generate one random integer between 0 and 100 - for 100 times
    randlist.append(n) #add the random element to the list

def bubblesort(randlist): #define a function which will do the bubble sort
    for i in range(0,98):
        for j in range(i, 99):
            if randlist[j]<randlist[i]: #comparing every number in the list with the next one
                                        #if the next number is smaller than the previous one, the numbers will swap
                x=randlist[i]
                randlist[i]=randlist[j]
                randlist[j] = x
    return
bubblesort(randlist) #run the function earlier defined

odd=0 #define the integer odd to keep the count for odd numbers
sumodd=0 #define the integer sumodd to keep the sum for odd numbers
even=0 #define the integer even to keep the count for even numbers
sumeven=0 #define the integer sumeven to keep the sum for even numbers

for i in range(0,100):
    if (randlist[i]%2) ==0: #if the number is divided by 2 we'll add one to the count of odd numbers and will add the number to sumodd
        odd = odd+1
        sumodd = sumodd+randlist[i]
    else:                   #else we'll ad one to the count of even numberss and will add the number to sumeven
        even = even+1
        sumeven = sumeven+randlist[i]

print (sumodd/odd) #print the average for odd numbers
print (sumeven/even) #print the average for even numbers


