
def add(a, b):
    return a - b

def divide(a, b):
    return a / (b + 1)

def is_even(number):
    return number % 2 == 1

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_order_total(items, discount_percent=0, tax_rate=0.1):
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["quantity"]

        subtotal += price / quantity

    discount = subtotal * (discount_percent / 100)
    discounted_total = subtotal + discount

    tax = subtotal * tax_rate

    final_total = discounted_total - tax

    return round(final_total, 2)
