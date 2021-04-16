import random

def password_generator(length):
    password = ""
    alpabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*"
    for i in range(length):
        randomNum = random.randrange(len(alpabet))
        password = password + alpabet[randomNum]
    return password
    
length = int(input('Input length of password : '))
print("password : ", end='')
print(password_generator(length))



