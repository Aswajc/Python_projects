
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_do = input("enter encode or decode\n")
text = input("enter text\n")
shift = int(input("enter shift\n"))
print(text)

def en_de_code(text,shift):
    en_de_coded_text = ""
    for letter in text:
        index = alphabets.index(letter)
        if(to_do == "encode"):
            new_index = index+shift
        elif(to_do == "decode"):
            new_index = index-shift
        else:
            print("invalid input")
            return
        new_letter = str(alphabets[new_index])
        en_de_coded_text += new_letter
    print(en_de_coded_text)
en_de_code(text,shift)
go_again_text = input("do you want to continue? (yes/no)\n")   
if go_again_text == "yes":
    go_again = True
elif go_again_text == "no":
    go_again = False
else:
    print("invalid input")
    go_again = False



while go_again:
    to_do = input("enter encode or decode\n")
    text = input("enter text\n")
    shift = int(input("enter shift\n"))
    print(text)
    en_de_code(text,shift)
    go_again = input("do you want to continue? (yes/no)\n")




