startstring =''' tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''



#normalize the text in startstring
def normalize_text(text):
    text = text.lower()
    #remove empty space at the beginning of the text
    text = text.lstrip()
    #remove empty space at the end of the text
    text = text.rstrip()
    text = text.replace(" iz ", " is ")
    #remove empty rows
    text = text.replace("\n", " ")
    #remove extra spaces
    import re
    def remove_spaces(str):
        return re.sub(r' {2,}' , ' ', str)
    text = remove_spaces(text)
    return text
startstring = normalize_text(startstring)

#replace '. '   with '.'
def replace_dot(text):
    text = text.replace(". ", ".")
    return text
startstring = replace_dot(startstring)

#create a sentence with the last words of each sentence in startstring
def create_sentence(text):
    text = text.split(".")
    last_words = []
    for sentence in text:
        if len(sentence) > 1:
            last_words.append(sentence.split()[-1])
    return " ".join(last_words).capitalize() + "."
last_sentence = create_sentence(startstring)

#add the new sentence to the end of startstring
startstring = startstring + last_sentence



#capitalize the first letter of each sentence in startstring
def capitalize_first_letter(text):
    text = text.split(".")
    new_text = []
    for sentence in text:
        if len(sentence) > 1:
            new_text.append(sentence[0].upper() + sentence[1:])
    return ". ".join(new_text) + ". "
startstring = capitalize_first_letter(startstring)

print (startstring)

#count the number of white spaces in startstring
def count_white_spaces(text):
    count = 0
    for i in text:
        if i.isspace():
            count+=1
    return count
    
print ('\nNumber of white spaces:', count_white_spaces(startstring))


