# Metodi speciali (Dunder)
# Python definisce metodi speciali
# Sono chiamati anche:
# -> Dunder methods
# -> Double Underscore
# -> Magic methods

# Metodi Dunder comuni sono:
# -- __init__ -> costruttore di una classe
# -- __str__ -> stampa user_friendly
# -- __repr__ -> stampa di debug
# -- __len__ -> restituisce la lunghezza
# -- __add__ -> la somma +
# -- __eq__ -> l'uguaglianza ==
# -- __lt__ -> verfica se è minore < (less than)
# -- __gt__ -> verifica se è maggiore > (greater than)

class Persona:
    __id = 0
    def __init__(self, name, age):  # Costruttore -> viene eseguito automaticamente alla creazione di un oggetto
        Persona.__id += 1
        self.name = name
        self.age = age
    def __str__(self):  #Equivalente del metodo toString -> rappresentazione leggibile dell'oggetto
        return f'Persona - nome: {self.name} anni: {self.age}'
    def __repr__(self):  #Equivalente del metodo toString -> rappresentazione tecnica (per debug)
        return f'Debug: {self.name} - {self.age}'
p1 = Persona('Mario Rossi', 45)  # -> __init__
p2 = Persona('Giuseppe Verdi', 70)
# x = p

print(p1)  # __str__
# print(x)
print(repr(p1)) # __repr__


class Classe:
    def __init__(self, name, students):
        self.name = name
        self.students = students
        
    def __str__(self):
        return f'Classe: {self.name} Studenti: {self.students}'
    
    def __len__(self): #Permette di utilizzare len() su un oggetto della classe
        return len(self.students)
    
c1 = Classe('Data Analyst', ['Mario Rossi', 'Giuseppe Verdi', 'Francesca Cuccuru', 'Antonio Conte'])  # Utilizzo di len()
print(c1)

# l = ['Mario Rossi', 'Giuseppe Verdi', 'Francesca Cuccuru', 'Antonio Conte']
# print(len(l))
print(len('Data Analyst'))  #Utilizzo di len() su una stringa
print(len(c1))
print('Numero di studenti:', len(c1))  # Utilizzo di len() su un oggetto custom

# # Operatore +
# x = 25
# y= 10
# z = x + y

class Numero:
    def __init__(self, valore):
        self.valore = valore
        
    def __add__(self, other):
           return Numero(self.valore + other.valore)
    
    def __str__(self):
        return f'Numero: {self.valore}'
# x = p1 + p2
n1 = Numero(30)
n2 = Numero(50)
n3 = n1 + n2
print(n3)

class Vettore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'
    
    def __repr__(self):
        return f'Vettore(X: {self.x}, Y: {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vettore):
            print('Operazione non supportata')
            return
        
        return Vettore(self.x+other.x, self.y+other.y)
    
    def __eq__(self, other):  # Oprator overloading -> permette di verificare l'uguaglianza dei valori presenti tra più oggetti e numeri
        return self.x == other.x and self.y == other.y
    
v1 = Vettore(1, 2)
v2 = Vettore(3, 4)
# v3 = v1 + v2
v3 = v1 + n1
v3 = v1 + v2
print(v3)

# Di default == confronta l'indirizzo alla zona di memoria
v4 = v1
print(v1 ==v4)

# Esempio completo
class Carrello:
    def __init__(self):
        self.__prodotti = []
        # self.__totale = 0 -> Soluzione alternativa
        
    @property
    def prodotti(self):
        return self.__prodotti        
        
    def aggiungi(self, prezzo):
        self.__prodotti.append(prezzo)
        # self.__totale += prezzo -> Soluzione alternativa
        
    def __add__(self, other):
        nuovoCarrello = Carrello()
        nuovoCarrello.__prodotti = self.__prodotti + other.__prodotti
        return nuovoCarrello
        
    def __len__(self):
        return len(self.__prodotti)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    def __str__(self):
        return f'Carrello con {len(self)} prodotti, Totale: {sum(self.__prodotti)}'
    
c = Carrello()
c.aggiungi(25)
c.aggiungi(13)
c.aggiungi(24)

print(c)

oc = Carrello()
oc.aggiungi(8)
oc.aggiungi(24)
print(oc)

tc = c + oc
print(tc)

print('----------------------------------------------------------------------------------------------')

# Caso pratico completo
# Sistema di carrello avanzato

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
            
    def __str__(self):
        return f'Prodotto: {self.name} £{self.price}'
    
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
        
class Cart:
    def __init__(self):
        self.__products = []
        
    @property
    def products(self):
        return self.__products
    @products.setter
    def products(self, productList):
        self.__products = productList
        
    def addCart(self, product):
        self.products.append(product)
        
    def totalCart(self):
        # Soluzione 1
        # total = 0
        # for product in self.products:
        #     total += product.price
        # return total
        return sum([product.price for product in self.products])
    
    def __add__(self, other):
        if not isinstance(other, Cart):
            print('Operazione non supportata')
            return
        new = Cart()
        new.products = self.products + other.products
        return new
    
    def __len__(self):
        return len(self.products)
    
    def __str__(self):
        return f'Carrello con {len(self)} prodotti - Totale: {sum(self.products)}'
    
    
p1 = Product('Libro', 10)
p2 = Product('Libro', 10)
p3 = Product('Sartphone', 100)

c= Cart()
c.addCart(p1)
c.addCart(p2)
c.addCart(p3)

oc = Cart()
oc.addCart(Product('Jeans', 98))

tc = c + oc

print(c)
# print(p1)
# print(p1 == p2)