import time

from datetime import datetime


def palindrome(str):
    return str==str[::-1]

start = datetime.now()
p = palindrome("-101")
end = datetime.now()
print p, (end-start)