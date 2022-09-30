import string #import string module
import random #import random module

count=0 #number of dictionaries in list
dictlist = [] #define the dictionary
for i in range(random.randint(2,10)): #define the random number of dictionaries
    size = random.randint(1,26)    #define the random dictionary size for every one of the dictionaries
    keys = random.sample(string.ascii_lowercase,size)  #define the random letters for every one of the dictionaries using the size defined above
    values = (random.randint(0,100) for j in range(size)) #define the random numbers for every one of the dicitonaries using the size defined above with values between 0 and 100
    oneDict = dict(zip(keys,values))  #create the dictionary from the two sequences keys and values
    dictlist.append(oneDict)     #add the dictionary created above to the list of dictionaries
    count = count + 1

print(dictlist)
print(count)

interdict = {}
finaldict = {}
doublesdict = {}
finaloutput = {}

for i in range (0, count):
    interdict = dictlist[i]
    for key,value in interdict.items():
        if key in finaldict:
            onedict = {(key, value)}
            doublesdict.update(onedict)
        finaldict[key] = value

print (finaldict)
print (doublesdict)

for key, value in finaldict.items():
    currkey = key
    currvalue = value
    if key in doublesdict:
        maxvalue = value
        for i in range (0, count):
            interdict = dictlist[i]
            if key in interdict and interdict[key]>=maxvalue:
                maxvalue = interdict[key]
                dictnumber = i+1
        currvalue = maxvalue
        currkey = key + "_" + str(dictnumber)

    onedict = {(currkey, currvalue)}
    finaloutput.update(onedict)


print (finaloutput)



