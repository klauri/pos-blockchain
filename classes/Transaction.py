from dataclasses import dataclass, field
from time import time

@dataclass
class Item:
    item_id: int
    description: str
    price: float
    taxable: bool = True

@dataclass
class LineItem:
    item: Item
    quantity: int
    sell_price: float = field(init=False)

    def __post_init__(self):
        self.sell_price = self.item.price * self.quantity

@dataclass
class Transaction:
    stream_id: str
    line_items: list[LineItem]
    time: time = time()
    sub_total: float = 0
    total: float = 0
    tax_rate: float = 0.0635

    def __post_init__(self):
        for line_item in self.line_items:
            self.sub_total += line_item.sell_price
        self.total = round(self.sub_total * (1 + self.tax_rate), 2)