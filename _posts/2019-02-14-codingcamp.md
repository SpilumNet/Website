---
author: tpan
type: blog
description: Forritunarbúðir 2019
---

Hér getið þið fundið svör við dæmin sem að þið hafið gert ^w^
## PYTHON
```python
def main():
    func = ""
    function_dict = {'summary':summary, 'multi':multi, 'prime':prime, 'dice':dice }
    
    while func != "exit":
        print("=" * 40)
        print("summary\t multi\t prime\t dice\t")
        func = input(">>> ")
        function_dict[func]()

def summary():
    low = int(input("Sláðu inn minnstu töluna: "))
    high  = int(input("Sláðu inn hæstu töluna: "))
    summary = 0
    for x in range(low,high + 1, 1):
        summary = summary + x
    print("Summa alla talna frá", low, "til", str(high) + ":", summary)


def multi():
    for j in range(1,11):
        output = ""
        for x in range(1,11):
            output = output + str(x * j) + " "
        print(output)

def prime():
    for x in range(2,51):
        prime = True
        for j in range(2, x//2+1):
            if x % j == 0:
                prime = False
                break
        if prime:
            print(x)

def dice():
    from random import randint
    while True:
        try:
            diceNum = int(input("Hversu oft viltu kasta? "))
            for i in range(diceNum):
                print("Kast", str(i+1) + ":", randint(1,6))
        except:
            break

main()
```
