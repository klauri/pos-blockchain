from time import time
from Chain import Chain
from Blocks import Block

def generate_transaction(stream_id, trading_time, commodity, amount):
    transaction = [stream_id, trading_time, commodity, amount]
    return transaction

if __name__ == "__main__":
    chain = Chain() 

    commodity = ["burger", 2, 10.99]
    tax = 10.99 * 0.0635
    amount = commodity[1] * commodity[2]
    transaction = generate_transaction(1, time(), commodity, amount)
    chain.add_new_transaction(transaction)
    chain.new_block()
    for block in chain.chain:
        print(block.transactions, block.hash, block.prevhash)
