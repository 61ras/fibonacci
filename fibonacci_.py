# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:45:49 2020

@author: Aslih
"""

def fibonacci(sinir):
      if sinir < 2:
          return sinir
      else :
          return (fibonacci(sinir-1) + fibonacci(sinir-2))
      

sinir=int(input("Lütfen sınır degerini giriniz:\n"))
while sinir:
    if(sinir>0):
        print("Fibonacci Dizisi:")  
        for i in range(sinir):  
            print(fibonacci(i)) 
            
        break
    else:
        sinir=int(input("Sınır değeri pozitif olmalı!:\n"))