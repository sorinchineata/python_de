import string #import string module
import random #import random module

count=0 #number of dictionaries in list
dictlist = [] #define the dictionary
for i in range(random.randint(2,2)): #define the random number of dictionaries
    size = random.randint(1,3)    #define the random dictionary size for every one of the dictionaries
    keys = random.sample(string.ascii_lowercase,size)  #define the random letters for every one of the dictionaries using the size defined above
    values = (random.randint(0,3) for j in range(size)) #define the random numbers for every one of the dicitonaries using the size defined above with values between 0 and 100
    oneDict = dict(zip(keys,values))  #create the dictionary from the two sequences keys and values
    dictlist.append(oneDict)     #add the dictionary created above to the list of dictionaries
    count = count + 1

print(dictlist)
print(count)

interdict = {}
finaldict = {}

maxdict = -1

print (interdict)

for i in range(0, count-1):
    dict1 = dictlist[i]
    for j in range (i+1, count):
        dict2 = dictlist[j]
        for key_1 in dict1.items():
            double = 0
            for key_2 in dict2.items():
                if key_1 == key_2:
                    double = 1
                    maxvalue = interdict[key]
                    if maxvalue < currentdict[keyd]:
                        maxvalue = currentdict[keyd]
                        dictnum = j+1
                    char = key_1 + "_" + str(dictnum)
            if double == 1:
                onedict = (char,maxvalue)
            else: onedict = (key_1,dict[key_1])
            dictlist.append(onedict)


