---
author: tpan
type: blog
description: Forritunarbúðir 2019
---

### Hér getið þið fundið svör við dæmin sem að við höfum farið í gegnum o3o
Endilega afritið þetta inní IDE-ið ykkar til þess að skoða eða breyta einhverju!
## PYTHON
```python
import os
from os import system

def main():
    
    s = ' '
    func = ""
    funcls = ['hewwo', 'gagnatypa', 'reikniadgerd', 'mathsafn', 'heiltolur','beraSaman', 'summa', 'margfalda', 'primtolur', 'teningur']
    
    function_dict = {'hewwo':hewwo, 'gagnatypa':gagnatypa,
                     'reikniadgerd':reikniadgerd, 'mathsafn':mathsafn,
                     'heiltolur':heiltolur, 'beraSaman':beraSaman,
                     'summa':summa, 'margfalda':margfalda,
                     'primtolur':primtolur, 'teningur':teningur }
    
    while func != "exit":
        os.system('cls')
        print("=" * 40)
        for i in range(len(funcls)):
            print(funcls[i], end=4*s)
            if (i+1) % 4 == 0:
                print()
        print()
        func = input(">>> ")
        print("-" * 40)
        function_dict[func]()
        input("[ENTER]")

def hewwo():
    print("Hewwo OwO *gibs all da huggos* ^w^")

def gagnatypa():
    nafn = input("Hvað heitir þú? ")
    print("Góðan daginn", nafn + "! Velkominn í forritunarbúðir tækniskólans")
    aldur = input("Hvað ertu gamall/gömul? ")
    print("Nú nú, þú ert bara", aldur, "ára!")

def reikniadgerd():
    C = input("Sláðu inn celsíus: ")
    C = float(C)
    F = (1.8 * C) + 32
    print("Farenheit:", str(F))


def mathsafn():
    number = int(input("Sláðu inn tölu: "))
    power  = int(input("Sláðu inn veldi: "))
    outcome = number ** power
    print(number, "í", power, "veldi er:", outcome)

def heiltolur():
    degres = int(input("Sláðu inn gráður: "))
    wholerings = degres // 360
    leftover = degres - (wholerings * 360)
    print("Heilir hringir : " + str(wholerings))
    print("Afangur af gráðum : " + str(leftover))

def beraSaman():
    fyrritala = int(input("Sláðu inn tölu (fyrri): "))
    seinnitala = int(input("Sláðu inn tölu (seinni): "))

    if fyrritala == seinnitala:
        print("tölurnar eru jafnar")
        
    elif fyrritala > seinnitala:
        print(str(fyrritala) + " er stærri en " + str(seinnitala))
        
    else:
        print(str(seinnitala) +" er stærri en " + str(fyrritala))

def summa():
    nedrimork = int(input("Sláðu inn minnstu töluna: "))
    efrimork  = int(input("Sláðu inn hæstu töluna: "))
    summa = 0
    
    for x in range(nedrimork,efrimork + 1, 1):
        summa = summa + x
        
    print("Summa alla talna frá", nedrimork, "til", str(efrimork) + ":", summa)


def margfalda():
    for j in range(1,11):
        output = ""
        
        for x in range(1,11):
            output = output + str(x * j) + " "
            
        print(output)

def primtolur():
    for x in range(2,51):
        prime = True
        
        for j in range(2, x//2+1):
            if x % j == 0:
                prime = False
                break
            
        if prime:
            print(x)

def teningur():
    from random import randint
    while True:
        try:
            kost = int(input("Hversu oft viltu kasta? "))
            for i in range(kost):
                print("Kast", str(i+1) + ":", randint(1,6))
                
        except:
            break

main()
```
