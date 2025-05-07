import random
letters_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
number_set = ['0', '1', '2', '3', '4', '5', '6']
print("Welcome to password generator")
letters = input("how many letters")
# symbols = input("how many symbols")
numbers = int(input("how many numbers"))
password = ""
for number in range(1, numbers+1):
    random_num = random.choice(number_set)
    password += random_num  
    print(password)