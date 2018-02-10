#!/bin/python3

import sys

def revisedRussianRoulette(doors):
    # Complete this function
    #print(doors)
  
    min = 0
    max = 0
    flag = "off"
    for i in range(len(doors)):
        #print(i, "i")
        if doors[i] == 1:
            max += 1
            if doors[i+1] == 1:
                if flag == "off":
                    print("flag changed to on!!!")
                    min += 1
                    print(min, "min")
                    flag = "on"
                else:
                    print("ok")
                    #flag == "on"
                    print("flag changed to off")
                    flag = "off"  
            
            
    print(min, "min")
    print(max, "max")
    
            
    
            
        
        
if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))


