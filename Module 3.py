start_str =  ''' tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

count = 0
for i in start_str:
    if i.isspace():
        count+=1


#remove empty rows
#lower all the words
interstr= start_str.replace("\n", " ")
interstr = interstr.lower()

import re
def remove_spaces(str):
    return re.sub(r' {2,}' , ' ', str)
interstr = remove_spaces(interstr)

#function to return last word from sentence
def final_str(str):
    res = str.split(' ')
    fin = res[len(res)-1]
    return([fin])

last_word_stc = ''

nodot_str = interstr.split(".")
for every_stc in nodot_str:
    last_word = final_str(every_stc)
    last_word_stc = last_word_stc + last_word[0] +' '

last_word_stc = last_word_stc.replace("  ", ".")

split_str = interstr.split("paragraph.")
fin_str = ''
fin_str = split_str[0] + 'paragraph. '+ last_word_stc + split_str[1]
fin_str = fin_str.replace(" iz ", " is ")

string_final = ''
nodot_str = fin_str.split(".")

for i in nodot_str:
    if len(i)>1:
        string_final = string_final + i[1].upper()+i[2:]+ '. '


print("Final text is:")
print (string_final)
print ('\nNumber of white spaces:', count)