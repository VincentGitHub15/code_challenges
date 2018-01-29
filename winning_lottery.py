#!/bin/python3

import sys

def winningLotteryTicket(tickets):
    # Complete this function
    #print(tickets, "tickets")
    for i in range(len(tickets)):
        print(tickets[i], "i")
        for j in range(len(tickets)):
            print(tickets[j], "j")
            a = str(tickets[i])
            b = str(tickets[j])
            mylist = []
            mylist.append(a)
            mylist.append(b)
            print(mylist)
    #print(result)

if __name__ == "__main__":
    n = int(input().strip())
    tickets = []
    tickets_i = 0
    for tickets_i in range(n):
       tickets_t = str(input().strip())
       tickets.append(tickets_t)
    result = winningLotteryTicket(tickets)
    #print(result)