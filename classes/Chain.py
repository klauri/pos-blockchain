from time import time
import datetime as d
from classes.Blocks import Block

class Chain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, time(), ["handshake_transaction"], "0", 0)
        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def new_block(self):
        index = self.last_block.index + 1
        timestamp = d.datetime.now()
        last_hash = self.last_block.hash
        transactions = self.unconfirmed_transactions
        block = Block(index, timestamp, transactions, last_hash, 0) #return entire block
        self.chain.append(block)
        return True

    def proof_of_work(self):
        pass