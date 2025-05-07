import random
word_list = ["aswaj","apple","asim","orange"]
random_num = random.randint(0,int(len(word_list)- 1))
chosen_word = word_list[random_num]
print(chosen_word)


guessed_letter = input("Guess a letter ")
if guessed_letter in chosen_word:
    print("success")
    letter_list = []
    for letter in chosen_word:
        if guessed_letter == letter:
            letter_list += guessed_letter
        else:    
            letter_list += "_" 
    else:
        print("error")    

    print(letter_list)
    print(len(letter_list)) 


else:
    print("failed")


