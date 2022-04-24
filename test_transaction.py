from time import time
from classes.Chain import Chain
from lib.transactions import generate_transaction, calculate_tax, calculate_total

test_transactions = [
        ["burger", 2, 10.99],
        ["fries", 2, 1.99],
        ["hot dog", 1, 6.99]
    ]

if __name__ == "__main__":
    chain = Chain()
    chain.create_genesis_block()
    for transaction_data in test_transactions:
        transaction = generate_transaction(1, time(), transaction_data)
        chain.add_new_transaction(transaction)
        chain.new_block()
    for block in chain.chain:
        print(block.transactions, block.hash, block.prevhash)
