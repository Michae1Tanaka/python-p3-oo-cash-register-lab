#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.item_prices = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
            self.item_prices.append(price)

    def apply_discount(self):
        discount_total = self.total * self.discount / 100
        self.total -= discount_total
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.items) == 0:
            self.total = 0.0
            self.item_prices = []
        else:
            last_item = self.items.pop()
            last_item_price = self.item_prices.pop()
            self.total -= last_item_price
            while last_item in self.items:
                self.total -= last_item_price
                self.items.pop()
                self.item_prices.pop()
