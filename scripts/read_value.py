from time import clock_settime
from brownie import SimpleStorage, accounts, config

def read_contract():
    print (SimpleStorage)
    # para interactuar con el contrato basicamente lo uso como un arreglo
    # usa -1 porque me dice el ultimo contrato deployed go take the index than ne less than the length (-1)
    # para interactuar con el contrato necesito la direccion y el ABI
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())
    

def main():
    read_contract()
