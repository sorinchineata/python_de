import string #import string module
import random #import random module

count=0 #number of dictionaries in list
dictlist = [] #define the dictionary
for i in range(random.randint(2,100)): #define the random number of dictionaries
    size = random.randint(1,26)    #define the random dictionary size for every one of the dictionaries
    keys = random.sample(string.ascii_lowercase,size)  #define the random letters for every one of the dictionaries using the size defined above
    values = (random.randint(0,100) for j in range(size)) #define the random numbers for every one of the dicitonaries using the size defined above with values between 0 and 100
    oneDict = dict(zip(keys,values))  #create the dictionary from the two sequences keys and values
    dictlist.append(oneDict)     #add the dictionary created above to the list of dictionaries
    count = count + 1

print(dictlist)
print(count)


finaldict = {}

for i in range(0, count):
    dict1 = dictlist[i]
    for j in range (i+1, count):
        dict2 = dictlist[j]
        for key_1,value_1 in dict1.items():
            double = 0
            dictnum = i+1
            maxvalue = dict1[key_1]
            for key_2,value_2 in dict2.items():
                if key_1 == key_2 and dict1[key_1]!=dict2[key_2]:
                    double = 1
                    if maxvalue < dict2[key_2]:
                        maxvalue = dict2[key_2]
                        dictnum = j+1
                    char = key_1 + "_" + str(dictnum)
'''
I tried to take the dictionaries in the list and to compare them to see if the key is multiple dictionaries
At the the end of the comparison if it wasn't a double i would add to the final dictionary the key and the value as they are
In case of a double i would modify the key to have the number of the dictionary in which it was found.
The problem seems to be at the last dictionary which isn't merged to the final one and also with this solution, if it would be a double in the last one
it would be taken as it is
'''

            if double == 0:
                onedict = {(key_1, dict1[key_1])}
                # print(onedict)
                finaldict.update(onedict)

            else:onedict = {(char,maxvalue)}
                #print(onedict)
            finaldict.update(onedict)


print (finaldict)