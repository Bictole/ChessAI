# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:43:01 2020

@author: morin
EASY EXAMPLE
"""
import random
import graph as g

            


def max_Q(s,nb):
    maxi = nb%3+1
    for i in range (len(s.quality)):
        
        if(s.quality[i]>s.quality[maxi]):
            maxi = i
              
    return maxi
        
        

def Qlearning(learning_rate, episode):
    G = g.new_graph()
    for i in range(0,episode):
        l = 1
        e = 1
        current = 0
        for i in range(0,4):
            s = G[current]
            nb = random.randint(0,1)
            if(nb<e):
                a = random.randint(0,3)
            else:
                a = max_Q(s,current)
            
            
            s_bis = G[a] #action 1 leads to state 1, action 2 to state 2, ...
            s.quality[a] = l*(s_bis.reward + 0.4*max_Q(s_bis,a) + (1-l)*s.quality[a])
            l *=0.99
            e*=0.99
            print("S",current,"---->","S",a)
            if(s_bis == G[3]):
                break
            
            current = a
            
            
    display(G)
    #time.sleep(10)  
    
def display(G):
    
    for i in range (len(G)):
        print("S",i)
        current = G[i]
        for stat in range(len(G)):
            if(stat != i):
                print("----> S",stat, "   P =",current.proba[stat], "   Q =",current.quality[stat])
                print("\n\n")
                
                
            
          
        