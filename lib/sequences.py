#!/usr/bin/env python3

def print_fibonacci(length):
 
    list = []
    list.append(0)
    list.append(1)
    
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    while len(list) < length:
        # list.append()
        list.append(list[-1] + list[-2])
        
    
    print(list)
   



print_fibonacci(0)
# => [0, 1, 1, 2, 3, 5, 8, 13, 21]