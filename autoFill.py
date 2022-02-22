import numpy as np
import string
import re

prob={}    
trigram={}
bigram={}


file = open("Sports_Data.txt", "r", encoding="utf8")
data = file.read()
file.close()

#split data in single words
data=data.split()
words= [w.strip(" ") for w in data]
#print(wordsTokens)

#--------------------------------------------------------------------------------------------------- 

#calculating probabilities of co-occers
for i in range(len(words)-2):
    seq=' '.join(words[i:i+3])
    if seq not in trigram.keys():
        trigram[seq]=1
    else:
        trigram[seq]+=1
        
  
for i in range(len(words)-1):
    seq=' '.join(words[i:i+2])
    if seq not in bigram.keys():
        bigram[seq]=1
    else:
        bigram[seq]+=1


for tri in trigram:
    bi= tri.split()
    seq=' '.join(bi[0:2])

    prob[tri]=trigram[tri]/bigram[seq]

#print(ngrams.keys())
#print(ngrams.values())
#print(" ")
#print(model.keys())
#print(model.values())
#print(" ")
#print(prob.keys())
#print(prob.values())
    
#---------------------------------------------------------------------------------------------------
    
#predicted funcion
def Run(input):
    input_word=input.split(" ")
    output=[]
    for i in prob.keys():
        if input in  i :
            if i.split(" ")[0] == input_word[0] and i.split(" ")[1] == input_word[1]:
                output.append((i,prob[i]))

    output.sort(key=lambda x: x[1],reverse=True) #descending

    numOfSuggestions= 5
    if numOfSuggestions > len(output):
        numOfSuggestions = len(output)

    for i in range(numOfSuggestions):
        print(output[i][0].split(" ")[2])

#---------------------------------------------------------------------------------------------------                
def main():
    predicted = input('Enter your first 2 words : ')
    Run(predicted)

main()
