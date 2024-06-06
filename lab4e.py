#!/usr/bin/env python3
# Author ID: 124166224

def is_digits(sobj):
    # place code here i- loop through each character in sobj 
    flag = 0 
    for ch in sobj:
        if ch in "0123456789":
            pass
        else:
            flag=1
    if flag==1:
        return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
