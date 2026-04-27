#Questo è un commento
#CTRL + ù serve ad attivare/disattivare il commento

#Python NON è un linguaggio fortemente tipizzato
#String miaVar -> Java -> fortemente tipizzato

miaVar = 5
#print(miaVar, type(miaVar))
miaVar = "testo"
#print(miaVar, type(miaVar))
miaVar = True
#print("Il valore di miaVar è:", miaVar, "e il suo tipo è:", type(miaVar))

#abc = None

# Nomenclatura di un elemento python
# CamelCase | PascalCase | SnakeCase
nomeDatoVariabile = 0     #CamelCase
NomeDatoVariabile = 0     #PascalCase
nome_dato_variabile = 0   #SnakeCase
nomedatovariabile = 0     #Classic
NOME_DATO_COSTANTE = 0 # Convenzione per le costanti

# Assegnazione singole
x = 1
y = 2
z = 3

#Assegnazioni multiple
x,y,z = 1,2,3
x = y = z = 1

#Tipo di dato in Python
#int      -> numeri interi       -> d=5
#float    -> numeri decimali     -> d=5.5
#str      -> stringhe di testo   -> d="testo"
#boolean  -> valori booleani     -> d=True o False
#none     -> valore nullo        -> d=None

# Funzioni predefinite in python
#print(args)    -> Funzione che stampa nel terminale il valore di args
#type(var)      -> Funzione che restituisce il tipo di dato di una variabile
#input()        -> Funzione che permette l'inserimento di valori da tastiera
#len()          -> Funzione che restituisce la lunghezza di una stringa o di una lista
#help(func)         -> Funzione che restituisce la documentazione di una funzione passata come parametro

#Funzioni predefinite di Casting
#int(param)      -> Funzione che converte un valore in un numero intero (formato int)
#float(param)    -> Funzione che converte un valore in un numero decimale (formato float)
#str(param)      -> Funzione che converte un valore in una stringa (formato stringa)
#bool(param)     -> Funzione che converte un valore in un booleano (formato booleano)
# bool(0) | bool('') | bool([]) | bool(()) | bool({}) -> False


miaVar = "Sono una Stringa"
print(miaVar)
print(type(miaVar))
print(len(miaVar))
nome = input("Inserisci un nome: ")
print("Il nome che hai inserito è:" + nome)
age = input("Inserisci la tua età: ") #stringa
eta = int(age) #trasformo la stringa in un valore intero
eta = float(age) #trasformo il numero intero in un numero decimale
eta = bool(age) #trasformo il numero intero in un valore booleano
print(eta, "è di ",type(eta))

print("FINE")

if nome.lower() == "leyon":
    print("Sei il GOAT")
else:
    print("Chi sei?")

# String in Python
# Per creare una stringa in Python si possono utilizzare sia le virgolette doppie ("") che le virgolette singole ('')
# Per creare una stringa multiriga si possono utilizzare le triple virgolette (""" """) o (''' ''')
# Possiamo accedere a ogni singolo carattere di una stringa tramite l'indice[i]
# Possiamo selezionare una porzione di stringa tramite la sintassi [n:m]
# Funzioni predefiniti per manipolare le stringhe:
# lower() -> restituisce una copia della stringa con tutti i caratteri in minuscolo
# upper() -> restituisce una copia della stringa con tutti i caratteri in maiuscolo
# strip() -> restituisce una copia della stringa con gli spazi bianchi iniziali e finali rimossi
# replace(old, new, count) -> restituisce una copia della stringa con tutte le occorrenze di 'old' sostituite da 'new', ma solo la prima occorrenza (count)
# split() -> restituisce una lista di parole separate da spazi
# format() -> restituisce una stringa formattata con i valori passati come argomenti

multiStr = """Sono   
            una 
                  stringa"""
#        0123456789....                  
str = "Sono una stringa" #stringa a singola riga   
print(str[1])
print(str[5:8])
print(str[:8])
print(str[5:])
print(str[-5:-1])
print(str[-7:])

print(str.lower())              #restituisce una copia della stringa con tutti i caratteri in minuscolo
print(str.upper())              #restituisce una copia della stringa con tutti i caratteri in maiuscolo
print(str.strip())              #restituisce una copia della stringa senza gli spazi bianchi iniziali e finali
print(str.replace('n','x',1))   #restituisce una copia della stringa con tutte le occorrenze di 'n' sostituite da 'x', ma solo la prima occorrenza (1)
print(str.split())              #restituisce una lista di parole separate da spazi
print(str)                      #stampa la stringa originale
nome = "Leyon"
cognome = "Jayawardana"
eta = 20
#saluta = "Ciao " + nome + " " +  cognome + " " + "sono una stringa!"
saluta = "Ciao {} {} anni {}sono una stringa!"
print(saluta.format(nome, cognome, eta)) #restituisce una stringa formattata con i valori passati come argomenti
saluta = "Ciao {1} {0} anni {2}sono una stringa!"
print(saluta.format(cognome, nome, eta))                   #print(saluta)
#                      0       1    2
saluta = "Ciao {name} {lastname} anni {age}sono una stringa!"
print(saluta.format(name = nome, lastname = cognome, age = eta)) 

print(f"Ciao {nome} {cognome} anni {eta} sono una stringa!") 

# if-else

# if condizione:
#    istruzione
# else:
#    istruzione

age = 20
if age >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")
    
    