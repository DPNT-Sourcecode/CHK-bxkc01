from collections import Counter
from dataclasses import dataclass, field
from typing import Callable, List, Tuple


ITEMS = {
"A":50,
"B":30,
"C":20,
"D":15,
"E":40,
"F":10,
"G":20,
"H":10,
"I":35,
"J":60,
"K":80,
"L":90,
"M":15,
"N":40,
"O":10,
"P":50,
"Q":30,
"R":50,
"S":30,
"T":20,
"U":40,
"V":50,
"W":20,
"X":90,
"Y":10,
"Z":50,

}

def buy_x_product_for_offer_price(item: str, qty: int, offer_price: int) -> Callable:
    def offer(items: list[str]) -> Tuple[int, list[str]]:
        """
        Calculate the discounted total for a given item and remove the items from the list.
        """
        count = items.count(item)
        groups = count // qty
        remainder = count % qty

        total = groups * offer_price + remainder * item.price

        items = [i for i in items if i != item] 
        return total, items
    return offer

def buy_x_get_y_free(item:str , x_qty: int, y_item: str, y_qty: int) -> Callable:
    """
    Buy x amount of item and get y amount of another item for free.
    """
    def offer(items: list[str]) -> Tuple[int, list[str]]:
        """
        Calculate the discounted total for a given item and remove the items from the list.
        """
        count_x = items.count(item)
        count_y = items.count(y_item)
        
        groups = count_x // x_qty * y_qty
        free_items = min(count_y, groups)

        while free_items:
            items.remove(y_item)
            free_items -= 1

        total = count_x * item.price

        items = [i for i in items if i != item] 
        return total, items

    return offer

ITEMS = {
    'A': Item('A', 50, offers=[
        buy_x_product_for_offer_price(Item('A', 50), 5, 200),
        buy_x_product_for_offer_price(Item('A', 50), 3, 130),
    ]),
    'B': Item('B', 30, offers=[
        buy_x_product_for_offer_price(Item('B', 30), 2, 45),
    ]),
    'C': Item('C', 20),
    'D': Item('D', 15),
    'E': Item('E', 40, offers=[
        buy_x_get_y_free(Item('E', 40), 2, Item('B', 30), 1),
    ]),
    'F': Item('F', 10, offers=[
        buy_x_get_y_free(Item('F', 10), 3, Item('F', 10), 1),
        
    ]),
    'G': Item('G', 20),
    'H': Item('H', 10, offers=[
        buy_x_product_for_offer_price(Item('H', 10), 5, 45),
        buy_x_product_for_offer_price(Item('H', 10), 10, 80),
        ]),
    'I': Item('I', 35),
    'J': Item('J', 60),
    'K': Item('K', 70, offers=[
        buy_x_product_for_offer_price(Item('K', 70), 2, 150),
    ]),
    'L': Item('L', 90),
    'M': Item('M', 15),
    'N': Item('N', 40, offers=[
        buy_x_get_y_free(Item('N', 40), 3, Item('M', 15), 1),
    ]),
    'O': Item('O', 10),
    'P': Item('P', 50, offers=[
        buy_x_product_for_offer_price(Item('P', 50), 5, 200),
    ]),
    'Q': Item('Q', 30, offers=[
        buy_x_product_for_offer_price(Item('Q', 30), 3, 80),
    ]),
    'R': Item('R', 50, offers=[
        buy_x_get_y_free(Item('R', 50), 3, Item('Q', 30), 1),
    ]),
    'S': Item('S', 30),
    'T': Item('T', 20),
    'U': Item('U', 40, offers=[
        buy_x_get_y_free(Item('U', 40), 3, Item('U', 40), 1),
    ]),
    'V': Item('V', 50, offers=[
        buy_x_product_for_offer_price(Item('V', 50), 2, 90),
        buy_x_product_for_offer_price(Item('V', 50), 3, 130),
    ]),
    'W': Item('W', 20),
    'X': Item('X', 90),
    'Y': Item('Y', 10),
    'Z': Item('Z', 50),
}



class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        count = Counter(skus)
        total = 0

        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1
        

        for item in ITEMS.values():
            for offer in item.offers:
        
        # # Handle F
        # group_of_F3 = count['F'] // 3
        # rem_F3 = count['F'] % 3

        # total += group_of_F3 * 20 + rem_F3 * 10

        # # Handle E
        # while count['E'] >= 2 and count['B'] >= 1:
        #     count['B'] -= 1
        #     count['E'] -= 2
        #     total += 80
        
        # # Handle B
        # while count['B'] >= 2:
        #     count['B'] -= 2
        #     total += 45

        # # Handle A
        # group_of_A5 = count['A'] // 5
        # rem_A5 = count['A'] % 5 

        # group_of_A3 = rem_A5 // 3
        # rem_A3 = rem_A5 % 3

        # total += group_of_A5 * 200 + group_of_A3 * 130 + rem_A3 * 50
            
        # # the remaining skus
        # total += count['B'] * 30
        # total += count['C'] * 20
        # total += count['D'] * 15
        # total += count['E'] * 40

        # return total
       