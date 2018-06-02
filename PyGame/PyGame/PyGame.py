import time
import random

name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

print (" ")

time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

with open(r"""C:\Users\MATIAS\Desktop\Proiecte Programare\VisualStudio2017\PythonProj\PyGame\PyGame\words.txt""") as word_file:
    words = word_file.read().split() 
word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:         

    failed = 0             

    for char in word:      

        if char in guesses:    
            print (char)    
        else:  
            print ("_")
       
            failed += 1    
    
    if failed == 0:        
        print ("You won")  
   
        break              

    print

    guess = input("guess a character:") 
 
    guesses += guess                    
 
    if guess not in word:  
  
        turns -= 1        
 
        print ("Wrong")
 
        print ("You have", + turns, 'more guesses' )
 
        if turns == 0:           
            print ("You Loose\n",  "The word was: ", word)

