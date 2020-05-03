from random import *
import string
min_char = 4
max_char = 4
launchcode = ""
launchcodeguess = ""
allchar = string.ascii_lowercase + string.digits
lowerchar = string.ascii_lowercase
digits = string.digits
list = []
while launchcodeguess != launchcode:
    launchcodeguess = "".join(choice(digits) for x in range(randint(min_char, max_char))) + "2022"
    list.append(launchcodeguess)
    print(launchcodeguess)



