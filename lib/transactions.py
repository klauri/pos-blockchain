def generate_transaction(stream_id, trading_time, transaction_data):
    pre_tax_amount = transaction_data[1] * transaction_data[2]
    total_amount = pre_tax_amount + calculate_tax(pre_tax_amount)
    transaction = [stream_id, trading_time, pre_tax_amount, total_amount]
    return transaction

def calculate_subitem_total(price, quantity):
    subitem_total = price * quantity

def calculate_tax(pre_tax_amount):
    taxrate = 0.0635
    return pre_tax_amount * taxrate

def calculate_total(price: float, quantity: int):
    return price * quantity