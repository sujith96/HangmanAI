
# coding: utf-8

# In[2]:


def get_dictofprobs (new_word, incorrectly_guessed, listofwords, alphabet):
        
        # To get the word list dictionary with the probabilities for each word
        total_word_count=0
        for word in listofwords:
            total_word_count+=listofwords[word]
        for word in listofwords:
            listofwords[word]=float(listofwords[word])/total_word_count
        
        
        # To get the words filtered according to the intermediate stages in the game i.e according to "new_word"
        count = 0
        for letter in new_word:
            if(letter=='_'):

                filtered_dict = {k:v for k,v in listofwords.iteritems() if(k[count] in alphabet)}

            else:
                filtered_dict = {k:v for k,v in listofwords.iteritems() if(k[count]==letter)}


            listofwords = dict(filtered_dict)
            
            count+=1

        
        # To Calculate the frequencies of each word in the filtered dictionary
        total_subfreq=0;
        for k in filtered_dict:
            total_subfreq+=filtered_dict[k]
        ans=0


        # To Calculate the probabilities of each individual letter
        letter_prob={}
        for k1 in alphabet:
           
            for k in filtered_dict:

            
                if k1 in k:
                   
                    ans+=1*filtered_dict[k]
            letter_prob[k1]=round(ans/total_subfreq ,4)       
            
            ans=0

        # To get the dictionary of all letters with their probabilities in a descending order
        import operator
        sorted_letter_prob = sorted(letter_prob.items(), key=operator.itemgetter(1),reverse=True)
        alphabet = []
        sorted_letter_prob = dict(sorted_letter_prob)
        
        for letter in range(65, 91):
            alphabet.append(chr(letter))
        for k in alphabet:
            if(k in sorted_letter_prob):
                continue
            else:
                sorted_letter_prob[k]=0.0
        sorted_letter_prob = sorted(sorted_letter_prob.items(),key=operator.itemgetter(1),reverse=True )
        sorted_letter_prob = dict(sorted_letter_prob)   
        return(sorted_letter_prob)

