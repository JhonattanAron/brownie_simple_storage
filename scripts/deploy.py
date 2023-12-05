from brownie import accounts , config , SimpleStorage , network
import os

def deploy_simple_storage():
    account = accounts.load("aron-account")
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(42 , {"from":account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)

def main():
    deploy_simple_storage()
