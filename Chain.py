from time import time
from Blocks import Block

class Chain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, time(), ["init_transaction"], 0)
        genesis_block.hash = genesis_block.hash_block()
        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self, block):
        index = block.index + 1
        timestamp = d.datetime.now()
        hashblock = block.hash
        data = ["Transaction " + str(index)]
        block = Block(index, timestamp, data, hashblock) #return entire block
        self.chain.append(block)
        return True