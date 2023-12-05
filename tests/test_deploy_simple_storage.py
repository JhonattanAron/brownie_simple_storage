from brownie import accounts , SimpleStorage , network

def test_deploy():
    # Arrage -> Organizar o arreglar
    account = accounts[0]
    # Act-> hacer algo
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert -> Comprobar que a ido bien
    assert starting_value == expected

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("aron-account")


def test_updating_storage():
    # * Arrage
    account = accounts[0]
    # * Act
    simple_storage = SimpleStorage.deploy({"from":account})
    txn = simple_storage.store(42, {"from":account})
    txn.wait(1)
    expected = 42
    print(simple_storage.retrieve())
    # * Assert
    assert simple_storage.retrieve() == expected




    
