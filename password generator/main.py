from random import choice

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
random_password = ""

password_length = input("enter length of the password: ")

for char in range(int(password_length)):
    temp = choice(characters)
    random_password += temp

print(random_password)

