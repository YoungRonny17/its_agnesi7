# - Tuple: Collezioni di dati ORDINATE, IMMUTABILI  e permettono duplicati.
# -> v = ('Roma', 'Milano', 'Napoli')
# t = tuple
# tuple() | type() | len() | count(val)
# Accedere ad elementi di una tupla tramite un indice
# t[i] | t[i:i] | t[:i] | t[i:] | t[-i:-i]
# Non è possibile modificare elementi di una tupla
# Unire due o piu tuple con +  
# Copiare una tupla nt = tuple(t) | nt = t
# è possibile fare l'unpacking di una tupla a più variabili
# a, b, c = t

ta = ('Roma', 'Milano', 'Napoli', 'Roma')
print(ta, type(ta))
t = tuple(['Roma', 'Milano', 'Napoli', 'Roma'])
print(t, type(t), len(t), t.count('Roma'))

l = list(t)
l.append('Torino')
t = tuple(l)
print(t, type(t), len(t), t.count('Roma'))

print(t[1])
print(t[1:3]) # slicing

#unire due o piu tuple con +
bigt = ta + t # type: ignore
print(ta) # type: ignore
print(t)
print(bigt)


#copiare una tupla nt = tuple(t)
newt = tuple(bigt)
print(newt)

#Unpack di una tupla
t = ('Roma', 'Milano', 'Napoli')
t1 = t[0]
t1, t2 = t[0], t[1]
(c1, c2, c3) = t
print(c1)
print(c2)
print(c3)

#Iterare Tuple
i = 0
while i < len(t):
    print(t[i])
    i += 1
    
print("----------------------------")

for ele in t:
    print(ele)
    
    
# Crea una tupla chiamata persona contenente le seguenti informazioni:
# nome, cognome, età, città
# Stampa l'intera tupla
# Stampa separatamente ciascun elemento della tupla(Uno per riga)
# inserendo una etichetta chiara (Nome: , Cognome: ...)
# verifica se l'età è maggiore o uguale a 18 e stampa un messaggio 
# adeguato (La persona nome cognome è maggiorenne oppure minorenne)