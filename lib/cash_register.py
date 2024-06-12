#!/usr/bin/env python3

class CashRegister:
    def __init__(self,discount= 0):
        self.discount = discount
        self.total= 0
        self.items= []
        self.total_price= []
      
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self,discount):
        if discount > 0:
            self._discount = discount
        else:
            self._discount = discount
    
    @property
    def total(self):
        return self._total
      
    @total.setter
    def total(self,total):
        self._total= total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self,items):
        self._items = items
    
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self,total_price):
        self._total_price = total_price

    def add_item(self,title,price, quantity = None):

        # result = 0
        if type(quantity) == int:
            self.total += price * quantity
            title_list = [ title for number in range(quantity) ]
            self.items.extend(title_list)
            self.total_price.append(price * quantity)
        else:
          # result += price
          self.total += price
          self.items.append(title)
          self.total_price.append(price)
  



    def apply_discount(self):
      if self.discount > 0:
          convert = self.discount / 100
          discounts = 1.0 - convert
          self.total = int(self.total * discounts)
          print(f"After the discount, the total comes to ${self.total}.")
      else:
        self._total = self.total
        print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.total_price[-1]
        

