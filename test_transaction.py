from time import time
from Chain import Chain
from Blocks import Block

def sold_commodity(id, name, quantity, sale_price):
    return (id, name, quantity*sale_price)

def generate_transaction(stream_id, trading_time, commodity, amount):
    transaction = [stream_id, trading_time, commodity, amount]
    return transaction

if __name__ == "__main__":
    chain = Chain()
    chain.create_genesis_block()

    commodity = sold_commodity(1, "burger", 2, 10.99)
    tax = 10.99 * 0.0635
    amount = commodity[-1]
    transaction = generate_transaction(1, time(), commodity, amount)
    #chain.new_block(transaction)
    print(chain.last_block)
