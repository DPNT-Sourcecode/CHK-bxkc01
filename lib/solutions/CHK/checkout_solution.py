from collections import Counter
from dataclasses import dataclass, field
from typing import Callable, List, Tuple


PRICE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}


@dataclass
class Discount:
    item: str
    qty: int
    price: int


@dataclass
class Offer:
    item: str
    qty: int
    offer_item: str
    offer_qty: int


DISCOUNTS = [
    Discount("A", 5, 200),
    Discount("A", 3, 130),
    Discount("B", 2, 45),
    Discount("H", 2, 45),
    Discount("H", 10, 80),
    Discount("K", 2, 150),
    Discount("P", 5, 200),
    Discount("Q", 3, 80),
    Discount("V", 2, 90),
    Discount("V", 3, 130),
]

OFFERS = [
    Offer("E", 2, "B", 1),
    Offer("F", 3, "F", 1),
    Offer("N", 3, "M", 1),
    Offer("R", 3, "Q", 1),
    Offer("U", 3, "U", 1),
]

# def buy_x_product_for_offer_price(item: str, qty: int, offer_price: int) -> Callable:
#     def offer(items: list[str]) -> Tuple[int, list[str]]:
#         """
#         Calculate the discounted total for a given item and remove the items from the list.
#         """
#         count = items.count(item)
#         groups = count // qty
#         remainder = count % qty

#         total = groups * offer_price + remainder * item.price

#         items = [i for i in items if i != item]
#         return total, items
#     return offer

# def buy_x_get_y_free(x_item:str , x_qty: int, y_item: str, y_qty: int) -> Callable:
#     """
#     Buy x amount of item and get y amount of another item for free.
#     """
#     def offer(items: list[str]) -> int:
#         """
#         Calculate the discounted total for a given item and remove the items from the list.
#         """
#         count_x = items.count(x_item)
#         count_y = items.count(y_item)

#         groups = count_x // x_qty * y_qty
#         free_items = min(count_y, groups)

#         return free_items * ITEMS[y_item]

#     return offer


# # Need to calculate the best price when there are multiple offers
# def calculate_best_price(qty: int, price: int, offers: List[Offer]) -> int:
#     """
#     Calculate the best price for a given quantity of items and a list of offers.
#     """



class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        def handle_offer(item: str, discounts: List[Discount], offers: List[Offer], count: Counter, total: int) -> Tuple[Counter, int]:
            """
            Handle the offer for a given item.
            """
            
            # Sort discounts by item price
            discounts.sort(key=lambda x: x.price/x.qty, reverse=True)
            for discount in discounts:
                if count[item] >= discount.qty:
                    groups = count[item] // discount.qty
                    remainder = count[item] % discount.qty

                    total += groups * discount.price 
                    count[item] = remainder

            # Handle offers
            for offer in offers:
                if count[item] >= offer.qty:
                    groups = count[item] // offer.qty
                    remainder = count[item] % offer.qty

                    total += groups * PRICE[offer.offer_item]
                    count[offer.offer_item] -= groups * offer.offer_qty
                    count[item] = remainder

            return count, total


        
        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1
        
        count = Counter(skus)
        skus = set(skus)
        total = 0

        for item in skus:
            if item not in PRICE:
                return -1
            
            discounts = [d for d in DISCOUNTS if d.item == item]
            offers = [o for o in OFFERS if o.item == item]
        

            count, total = handle_offer(item, discounts, offers, count, total)

        return total


