import datetime as d
import hashlib as h

class Block:
    def __init__(self, index, timestamp, transactions, prevhash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prevhash = prevhash
        self.hash = self.hash_block()
        self.nonce = nonce

    def hash_block(self):
        block_encryption = h.sha256()
        data_to_encrypt = (str(self.index)+str(self.timestamp)+str(self.transactions)+str(self.prevhash)).encode('utf-8')
        block_encryption.update(data_to_encrypt)
        return block_encryption.hexdigest()
