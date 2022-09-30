import string #import string module
import random #import random module

count=0 #number of dictionaries in list
dictlist = [] #define the dictionary
for i in range(random.randint(2,10)): #define the random number of dictionaries
    size = random.randint(1,26)    #define the random dictionary size for every one of the dictionaries - maximum is 26 because we have 26 small letters in the english alphabet
    keys = random.sample(string.ascii_lowercase,size)  #define the random letters for every one of the dictionaries using the size defined above
    values = (random.randint(0,100) for j in range(size)) #define the random numbers for every one of the dicitonaries using the size defined above with values between 0 and 100
    oneDict = dict(zip(keys,values))  #create the dictionary from the two sequences keys and values
    dictlist.append(oneDict)     #add the dictionary created above to the list of dictionaries
    count = count + 1 #will be used to keep track of the number of dictionaries in the list

print('List of random generated dictionaries:')
print(dictlist)
#print(count)

currdict = {} #will be used in for in order to check the dictionaries one by one
interdict = {} #will be an intermediate version of the union off all dictionaries
doublesdict = {} #will be used to save all the double keys
finaldict = {} #will be the final output

for i in range (0, count):
    currdict = dictlist[i]
    for key,value in currdict.items():
        if key in interdict:
            onedict = {(key, value)}
            doublesdict.update(onedict)
        interdict[key] = value

#In the code above the interdict is created by merging all the dictionaries in the list and also keeping score of every key that appears in multiple dictionaries

#print (interdict)
#print (doublesdict)

for key, value in interdict.items(): #Taking every key in the intermediate dictionary
    currkey = key  #currkey takes the value of key and will be modified in the next steps if is in multiple dicitonaries
    currvalue = value #currvalue takes the value of 'value' and will be modified in the next steps if the key above is in multiple dicitonaries
    if key in doublesdict: #if the key above is in the dictionary with the doubles
        for i in range (0, count): #taking all the dictionaries in the list one by one to find the one with the maximum value related to the key and the number of that dictionary
            currdict = dictlist[i]
            if key in currdict and currdict[key]>=currvalue: #if the key is the current dictionary from the list and the value related to the key is bigger than the currvalue
                currvalue = currdict[key] #the currvalue will take the value related to the key from the current dictionary
                dictnumber = i+1 #we will take the number of the dictionary by adding 1 to the i value (the first dictionary is at [0] so we have to add 1)
        currkey = key + "_" + str(dictnumber)  #we will modify the value of currkey by addin "_" and the number of the dictionary with the max value

    onedict = {(currkey, currvalue)} #creating the dictionary with the values updated above
    finaldict.update(onedict) #concatenate the dictionary created above to the final dictionary

print('Final dictinary:')
print (finaldict)