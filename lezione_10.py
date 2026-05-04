# La programmazione orientata agli oggetti (OOP) si basa su:
# •	classi → modelli
# •	oggetti → istanze

# Permette di:
# •	organizzare il codice
# •	modellare il mondo reale
# •	migliorare la riusabilità

# Definizione di classe
# class MiaClasse:
# Creazione di un oggetto:
# obj = MiaClasse()

# Metodi nell classi
# Un meto è una funzione definita all'interno di una Classe e serve a:
# •	operare sui dati di un oggetto
# •	definire il comportamento dell'oggetto
# •	incapsulare logica

# Differenza fondamentale
# Funzione  -> indipendente
# Metodo    -> legato ad una classe

# Metodo di istanza -> il tipo più comune
# •	lavora sui dati dell'oggetto tramite 'self'

# Il parametro 'self' rappresenta:
# •	l'istanza corrente
# •	il collegamento tra il meto e l'oggetto

# Metodo di classe -> condiviso tra tutti gli oggetti della classe
# Un metodo di classe lavora sulla classe e non sull'istanza della classe
# si definisce utilizzando @classmethod

# Un linguaggio ad oggetti si poggia su 4 principi fondamentali:
# •	Incapsulamento
# •	Ereditarietà
# •	Polimorfismo
# •	Astrazione

# Incapsulamento è uno dei principi fondamentali della OOP
# Consiste nel nascondere i dati interni
# e permettere l'accesso ai dati solo tramite dei metodi controllati.
# Obiettivo: proteggere lo stato interno di un oggetto
# evitare modifiche non valide
# Rendere così il codice più sicuro e manutenibile

# Convenzioni e Sintassi per rappresentare un attributo public, protected, private:
# self.prop     -> public
# self._prop    -> protected
# self.__prop   -> private

# Vantaggi dell’incapsulamento
# Protegge i dati
# Riduce bug
# Migliora la manutenzione
# Permette validazione automatica
# Facilita il refactoring

# Errori comuni
# Usare variabili pubbliche sempre
# Usare get_ e set_ come in Java -> In Python è meglio: @property

class Automobile:
    # modello = 'Dodge Charger'
    # marca = 'Ford'
    # targa = 'AB123CD'
    
    #costruttore
    def __init__(self, marca, modello, targa, colore):
        self.marca = marca
        self.modello = modello
        self.targa = targa
        self.colore = colore
        self.targa = None
        self.incrementa()
        
    # Metodo di istanza
    def info(self):   # self serve per accedere agli attributi e metodi dell'istanza
        print(f"Automobile: {self.marca} {self.modello} Targa:{self.targa} Colore {self.colore} Targa: {self.targa}")

    @classmethod
    def incrementa(cls):
        cls.totale += 1   # cls = classe
        
# auto1.marca = 'Ford'
# auto1.modello = 'Shelby GT500'
# auto1.targa = 'EF456GH'
        
auto1 = Automobile('Ford', 'Dodge Charger', 'AB123CD')
# auto1.incrementa()
# print(auto1.totale)
auto2 = Automobile('Ford', 'Shelby GT500', 'EF456GH')
# auto2.incrementa()
# print(auto2.totale)
auto1.colore = 'Nero'


print(auto1)
print(auto2)

auto1.info()
auto2.info()

print(Automobile.totale)


class ContoCorrente:

    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome
        self.__saldo = 0

    # Metodo di istanza
    def info(self):
        print(f"Conto corrente di {self.__nome} {self.__cognome} Saldo: {self.__saldo}")
    
    # Property
        
    # Metodo migliore: usare le 'property'
    # Le 'property' sono il modo più Pythonico per fare incapsulamento.
    #Esempio con @property
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        if importo <= 0:
            raise ValueError("Importo non valido!!!")
            print("Non puoi aggiungere importi negativi")
            return
        self.__saldo = importo        

c = ContoCorrente("Mario", "Rossi")
c.saldo = 200 # Sto utilizzando il metodo Setter
c.saldo = -25 # Sto utilizzando il metodo Setter
print(c.saldo) # Sto utilizzando il metodo Getter
c.info()
c.info()

class Studente:
    
    def __init__(self, nome, matricola):
        self.__matricola = matricola
        self.__nome = nome
        self.__voti = []
        
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def voti(self):
        return self.__voti
        
    # Metodi di istanza
    def info(self):
        return f'Studente {self.__nome} matricola: {self.__matricola} voti: {self.__voti}'

    # Metodi di istanza
    def aggiungi_voto(self, voto):
        if voto > 0 and voto <= 30:
            self.__voti.append(voto)
        else:
            print('Hai aggiunto un valore errato')
    
    # Metodo di classe
    @classmethod
    def __genera_matricola(cls):
        cls.__contatore_matricola += 1
        matricola = cls.__contatore_matricola 
        if matricola < 10:
            matricola = f'US000{matricola}'
        elif matricola < 100:
            matricola = f'US00{matricola}'
        elif matricola < 1000:
            matricola = f'US0{matricola}'
        else:
            matricola = f'US{matricola}'
        return matricola
    
    
s1 = Studente('Mario Rossi')
s2 = Studente('Giuseppe Verdi')
s3 = Studente('Francesca Neri')
# Errore logico richiamare il metodo genera_matricola() al di fuori della classe studente
# s.genera_matricola() 

s1.aggiungi_voto(30)
s1.aggiungi_voto(25)
s1.aggiungi_voto(18)

print(s1.info())