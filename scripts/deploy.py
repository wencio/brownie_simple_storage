from brownie import accounts, config, SimpleStorage, network
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

private_key=os.getenv("PRIVATE_KEY")
web3_infura_project_id =os.getenv("WEB3_INFURA_PROJECT_ID")
print('esto es una prueba la clave es:')
print (private_key)
print(web3_infura_project_id)



def deploy_simple_storage():
    account = get_account()
    #account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    #voy a buscar un valor con el retrieve 
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15,{"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    #print(transaction)

    #transaccion
    #call

    #print(account)

    #me voy a traer la cuenta que acabo de crear utilizando la linea de comandos
    #brownie esta utilizando ganache-cli por defecto
    #account = accounts.load("freecodecamp-account")
    #print(account)
   # account = accounts.load(os.getenv("PRIVATE_KEY"))

   # estamos importando desde brownie-config la private key
    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()