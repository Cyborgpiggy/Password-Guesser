from random import *
import string
min_char = 8  # Min Char in password
max_char = 8  # Max Char in password
launchcode = open("", "r+")  # Put name of file
str = launchcode.read(1000)
launchcodeguess = ""
allchar = string.ascii_lowercase + string.digits + string.ascii_uppercase
lowerchar = string.ascii_lowercase
digits = string.digits
list = []
while launchcodeguess != str:
    launchcodeguess = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    list.append(launchcodeguess)
    print(launchcodeguess)
print(list)



