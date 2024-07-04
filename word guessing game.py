#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
name=input('what is your name?')
print('Goodluck!',name)
words=['computer','laptop','mouse','notepad','mathematics','python']
word=random.choice(words)
print('Guess the characters')
guesses=''
turns=10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print('_')
            failed += 1
    if failed == 0:
        print ('you win')
        print ('The word is:',word)
        break
    print()
    guess=input('Guess a character:')
    guesses += guess
    if guess not in word:
        turns -= 1
        print('wrong')
        print('you have', + turns , 'more guesses')
        if turns == 0:
            print('you loose')


# In[ ]:




