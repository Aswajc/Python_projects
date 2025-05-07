string = ["1","2","3","4","5","6"]
random_word = "aswaj"
count = 5
display_word =[]
for letter in random_word:
    display_word += "_"
print(display_word)

while "_"  in display_word:
    input_letter = input("guess a letter \n")
    for letter in range(len(random_word)):
        if random_word[letter] == input_letter:
            display_word[letter] = input_letter
    if input_letter not in random_word:
        count -= 1
        print("you lose a life")
        if count == 0:
            print("you lose")
            break   
    print(display_word)
else:
    print("you win")