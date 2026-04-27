# Sistema Registrazione Utente
# Stai sviluppando un semplice programma da terminale 
# per registrare un utente e mostrare un riepilogo formattato.

# Il programma deve:
# Chiedere all’utente: nome, cognome, età
#Eseguire le seguenti operazioni:
# - Convertire l’età da stringa a intero
# - Calcolare la lunghezza del nome e cognome
# Trasformare:
# - nome → maiuscolo
# - cognome → minuscolo
# Stampare un riepilogo con:
# - nome completo formattato
# - età
# - lunghezza nome e cognome
# - tipo della variabile età

# Usare obbligatoriamente:
# - input()
# - print()
# - type()
# - len()
# Usare almeno 2 metodi delle stringhe:
# .upper()
# .lower()
# .strip()
# Inserire controlli if per:
# età negativa
# nome vuoto


nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
age = input("Inserisci la tua età: ")
age = int(age)
print(len(nome), len(cognome))
nome = nome.upper()
cognome = cognome.lower()
print(f"""Nome completo è: {nome} {cognome} 
      Eta: {age}
      Lunghezza nome: {len(nome)}
      Lunghezza cognome: {len(cognome)}
      Tipo della variabile età: {type(age)}""")

if age <0:
    print("L'eta inserita è negativa")
else:
    print("L'eta inserita è positiva")
    
if nome.strip() == "":
    print("Non hai inserito un nome(è vuoto!)")