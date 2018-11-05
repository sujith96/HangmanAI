
# coding: utf-8


# Importing the unigram frequency model


import csv
mydictwords= {}
with open('unigram_freq.csv', mode='r') as infile:
        reader = csv.reader(infile)
        count = 0
        for rows in reader:
            if(count!=0):
                k = rows[0].upper()
                v = rows[1]
                mydictwords[k]=int(v)
            count = 1



#Generating List of words filtered with length of words


list_1_word = {k:v for k,v in mydictwords.iteritems() if len(k)==1}
list_2_word = {k:v for k,v in mydictwords.iteritems() if len(k)==2}
list_3_word = {k:v for k,v in mydictwords.iteritems() if len(k)==3}
list_4_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==4}
list_5_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==5}
list_6_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==6}
list_7_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==7}
list_8_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==8}
list_9_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==9}
list_10_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==10}
list_11_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==11}
list_12_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==12}
list_13_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==13}
list_14_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==14}
list_15_word = {k:v for k,v in 
mydictwords.iteritems() if len(k)==15}


# In[4]:
# To get the dictionaries for each word in the sentence


import get_dictofprobs
options = {
    1:list_1_word,
    2:list_2_word,
    3:list_3_word,
    4:list_4_word,
    5:list_5_word,
    6:list_6_word,
    7:list_7_word,
    8:list_8_word,
    9:list_9_word,
    10:list_10_word,
    11:list_11_word,
    12:list_12_word,
    13:list_13_word,
    14:list_14_word,
    15:list_15_word
    }
def dict_for_eachword(w,l,alphabet):
        listofwords = options[len(w)]
        return get_dictofprobs.get_dictofprobs(w,l,listofwords,alphabet)


# To replace the sentence with the letters in the correct places


def hangman(real,w,l):
    ans=""
    count = 0
    flag = 0;
    for i in real:
        if(i==l):
            flag = 1
            w = w[0:count]+l+w[count+1:]
        count+=1
    return w
        


# Given a sentence generating the blank spaces


def get_blanks_from_sentence(s):
    w=""
    for i in s:
        if(i!=" "):
            w+="_"
        else:
            w+=" "
    return w



# Getting the best letter given a sentence and an updated alphabet


def best_letter_sentence(alphabet1,sentence):
    temp_dict = {}
    list_predict=sentence.split()
    #alphabet1.remove("I")
    for letter in alphabet1:
        temp_dict[letter] = 1.0
    for blank in list_predict:
        #print((blank))
        temp_dict1 = dict_for_eachword(blank,[],alphabet1)
        #print(temp_dict1)
        for k in temp_dict:
            temp_dict[k]=temp_dict1[k]+temp_dict[k]
        #print(temp_dict)
    sorted_letter_prob = sorted(temp_dict.items(),key=operator.itemgetter(1),reverse=True )
    #print(sorted_letter_prob)
    return sorted_letter_prob[0][0]


#Generating the list of 100000 common words from the unigram list


import operator
mydict_sorted = sorted(mydictwords.items(),key=operator.itemgetter(1),reverse=True )
common_words=[]
count=0
for i in mydict_sorted:
    if(count<=1000):
        common_words.append(i[0])
    count+=1



# Running the model for a random sentence length with random words from the list of common words

def run_hangman():
        import random
        length_of_sentence= random.randint(3,6)
        actual_sentence = ""
        for i in range(length_of_sentence):
            actual_sentence+=(random.choice(common_words)+" ")
        print(actual_sentence)
        new_sentence = get_blanks_from_sentence(actual_sentence)
        alphabet1 = []
        for letter in range(65, 91):
                            alphabet1.append(chr(letter))
        wrong_attempts = 0
        while(new_sentence.lower()!=actual_sentence.lower()):
            print("New Sentence",new_sentence)
            next_letter = best_letter_sentence(alphabet1,new_sentence)
            print("Best Letter: ",next_letter)
            temp_sentence = new_sentence
            new_sentence = hangman(actual_sentence.upper(),new_sentence,next_letter)
            if(new_sentence==temp_sentence):
                print("WRONG!!")
                wrong_attempts+=1
            if(wrong_attempts>=3):
                print("DEAD")
                break
            alphabet1.remove(next_letter)
            
        if(wrong_attempts<3):
            return 1
            print("YOU WIN!!!!")
        else:
            return 0
            print("WRONG ATTEMPTS: ",wrong_attempts)

user_input = 0
while(user_input!=2):
        user_input = input ("Run Random hangman? If Yes Press 1. To end program press 2 ")
        if(user_input==1):
            print("Hangman Running")
            if(run_hangman()==1):
                print("YOU WIN!!")
        if(user_input==2):
            print("Thank You")
    

