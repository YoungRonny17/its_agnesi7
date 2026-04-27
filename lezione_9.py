# Stack delle chiamate

def func1():
    print('Start func1.')
    
def func2():
    print('Start func2.')
    func1()
    print('End func2.')

def func3():
    print('Start func3.')
    func2()
    print('End func3.')
    
# func3()
# print('FINE')

def ricorsiva(n):
    print('Funzione ricorsiva:', n)
    if n == 0:
        print('Ricorsione finita.')
        return
    ricorsiva(n-1) #in attesa nello stack delle chiamate
    # riparte da qui dopo la fine della ricorsione
    print('Fine Funzione ricorsiva:', n)
    
# ricorsiva(5)

def fattoriale(n):
    if n == 0:
        print('Ricorsione finita.')
        return 1
    print('Fattoriale: ', n)
    precedente = fattoriale(n-1)
    return n * precedente

result = fattoriale(10)
print(result)

# 5 * fattoriale(4) -> 5 * 24
# 4 * fattoriale(3) -> 4 * 6
# 3 * fattoriale(2) -> 3 * 2
# 2 * fattoriale(1) -> 2 * 1
# 1 * fattoriale(0) -> 1 * 1
# 1

import sys
# Python ha un limite di profondita dello stack
print(sys.getrecursionlimit())


#Comprehensions in python
# permettono di creare collezioni di dati in modo:
# -> Compatto
# -> Leggibile
# -> Efficiente

# è una sintassicompatta per creare collezioni come Liste, Set, Dizionari partendo da un iterabile
# è un'alternativa più concica al ciclo for

# List Comprehension
# [espressione for elemento in iterabile]
numeri  = [1, 2, 3, 4, 5]

# x = valore
# Soluzione utilizzando un ciclo for
quadrati = []
for x in numeri:
    q = x ** 2
    quadrati.append(q)
    
print(quadrati)

# Soluzione utilizzando List Comprehension
quadrati = [x ** 2 for x in numeri]
print(quadrati)

# Con utilizzo di una condizione
pari = [x for x in numeri if x % 2 == 0]
print(pari)

# Con utilizzo di if-else
elementi = ["pari" if x % 2 == 0 else "dispari" for x in numeri]
print(elementi)