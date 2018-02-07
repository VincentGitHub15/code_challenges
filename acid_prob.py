#!/bin/python3


import sys

def acidNaming(acid_name):


    if acid_name[len(acid_name)-1] == "c":
        if acid_name[len(acid_name)-2] == "i":
            #print("FOUND IC")
            
            if acid_name[0] == "h":
                #print("first h is H")
                if "hydro" in acid_name:
                    return "non-metal acid"
            else:
                return "polyatomic acid"
    else:
        return "not an acid"


if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)