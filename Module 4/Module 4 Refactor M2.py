import random
import string

def random_dictionary():
    i = 0
    oneDict = {}
    while i < random.randint(1,26):
        oneDict [random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        i += 1
    return oneDict

def dict_list():
    i=0
    dictlist = [] 
    while i < random.randint(2,10):
        dictlist.append(random_dictionary())
        i += 1
    return dictlist

def common_dict(dictlist):
    interdict = {}
    for i in range(len(dictlist)):
        for key,value in dictlist[i].items():
            if key not in interdict.keys():
                interdict[key] = [[value], [i+1]]
            elif key in interdict.keys():
                interdict[key][0].append(value)
                interdict[key][1].append(i+1)
    return interdict

     
def final_dictionary(dict):
    finaldict = {}
    for key, value in dict.items():
        if len(value[0]) > 1:
            max_val = max(value[0])
            key = key + '_' + str(value[1][value[0].index(max_val)])
            finaldict[key] = max_val
        elif len(value[0]) == 1:
            finaldict[key] = value[0][0]
    return finaldict


generated_list = dict_list()
print ('List of random generated dictionaries: ' + str(generated_list)+ '\n')
print ('Final dictionary:' + str(final_dictionary(common_dict(generated_list))))

