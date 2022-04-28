from time import time
from classes.Chain import Chain
from classes.Transaction import Transaction, Item, LineItem

item1 = Item(0, "burger", 10.99)
item2 = Item(1, "fries", 1.99)
item3 = Item(2, "hot dog", 6.99)

line1 = LineItem(item1, 2)
line2 = LineItem(item2, 2)
line3 = LineItem(item3, 1)

test_transaction1 = [
    line1,
    line2,
    line3
]

test_transaction2 = [
    line1,
    line3
]

test_transaction3 = [
    line3
]

if __name__ == "__main__":
    chain = Chain()
    transactions = [
        Transaction(stream_id=1001, line_items=test_transaction1),
        Transaction(stream_id=1001, line_items=test_transaction2),
        Transaction(stream_id=1001, line_items=test_transaction3)
    ]
    for transaction in transactions:
        chain.add_new_transaction(transaction)
        chain.new_block()    
    for block in chain.chain:
        print(f"Hash: {block.hash} Previous hash: {block.prevhash}")
