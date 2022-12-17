# Enter your code here. Read input from STDIN. Print output to STDOUT
from email import utils
import re
import os

def isEmailValid(email):
    return bool(re.match(r'^[a-zA-Z]+[0-9-._]*[a-zA-Z]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email))

for _ in range(int(input())):
    line = input()
    email_tuple = utils.parseaddr(line)

    if (isEmailValid(email_tuple[1])):
        print(utils.formataddr(email_tuple))