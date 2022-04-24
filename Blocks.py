from dataclasses import dataclass, field
from time import time
import datetime as d
import hashlib as h

@dataclass
class Block:
    index: int
    timestamp: time
    transactions: list[str] = field(default_factory=list)
    prevhash: str = field(default_factory="0")
    nonce: int = field(default_factory=0)
    hash: str = field(init=False, repr=False)

    def __post_init__(self):
        block_encryption = h.sha256()
        data_to_encrypt = (str(self.index)+str(self.timestamp)+str(self.transactions)+str(self.prevhash)).encode('utf-8')
        block_encryption.update(data_to_encrypt)
        self.hash = block_encryption.hexdigest()
