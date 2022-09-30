import string #import string module
import random #import random module

count=0 #number of dictionaries in list
dictlist = [] #define the dictionary
for i in range(random.randint(2,3)): #define the random number of dictionaries
    size = random.randint(1,3)    #define the random dictionary size for every one of the dictionaries
    keys = random.sample(string.ascii_lowercase,size)  #define the random letters for every one of the dictionaries using the size defined above
    values = (random.randint(0,10) for j in range(size)) #define the random numbers for every one of the dicitonaries using the size defined above with values between 0 and 100
    oneDict = dict(zip(keys,values))  #create the dictionary from the two sequences keys and values
    dictlist.append(oneDict)     #add the dictionary created above to the list of dictionaries
    count = count + 1

print(dictlist)
print(count)



interdict = {}
finaldict = dictlist[0]
doublesdict = {}
finaloutput = {}



for i in range (1, count):
    interdict = dictlist[i]
    for key,value in interdict.items():
        if key in finaldict:
            onedict = {(key, value)}
            doublesdict.update(onedict)
        finaldict[key] = value

print (finaldict)
print (doublesdict)

'''
In this version i am creating a final dictionary with merging all of them and keeping the values of the doubled keys in another dictionary
'''

for key, value in finaldict.items():
    double = 0
    for i in range (0, count):
        interdict = dictlist[i]
        if key in interdict and key in doublesdict:
            if interdict[key]==value:
                double = 1
                maxvalue = interdict[key]
                dictnumber = i+1
                break

'''
Here I am comparing the final dictionary to the list in order to create the final output with the modified keys for the doubles
The problem is that every time it is using the value in the last dictionary the double is found and not in the one with the bigger value
'''

    #if double == 1:
        #print (key)
        #print (maxvalue)
        #print (dictnumber)

    if double == 0:
        onedict = {(key, value)}
        finaloutput.update(onedict)
    else:
        char = key + "_" + str(dictnumber)
        onedict = {(char, maxvalue)}
        finaloutput.update(onedict)


print (finaloutput)

