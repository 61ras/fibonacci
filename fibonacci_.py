# recursive kodlama
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
            
 #iteratif kodlama
def fibonacci(sinir):
      sayi1=0
      sayi2=1
      print(sayi1)
      print(sayi2)
      for i in range(sinir-2):
        sayi3=sayi1+sayi2
        print(sayi3)
        sayi1=sayi2
        sayi2=sayi3

sinir=int(input("Lütfen sınır degerini giriniz:\n"))
if(sinir>0): fibonacci(sinir)
else:
     sinir=int(input("Sınır değeri pozitif olmalı!:\n"))
     fibonacci(sinir)
