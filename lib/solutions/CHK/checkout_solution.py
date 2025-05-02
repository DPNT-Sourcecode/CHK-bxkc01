from collections import Counter

PRICE_A = 50
PRICE_B = 30
PRICE_C = 20
PRICE_D = 15
PRICE_E = 40


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        count = Counter(skus)

        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1
        
        total = self.handle_offers(count)
            
        total += count['A'] * PRICE_A 
        total += count['B'] * PRICE_B
        total += count['C'] * PRICE_C
        total += count['D'] * PRICE_D
        total += count['E'] * PRICE_E
        
        return total

    def handle_offers(self, count: Counter) -> int:
        total = 0

        while count['E'] >= 2 and count['B'] >= 1:
            count['B'] -= 1
            total += 80

        while count['A'] % 5 == 0:
            count['A'] -= 5
            total += 200

        while count['A'] >= 3:
            count['A'] -= 3
            total += 130

        while count['B'] >= 2:
            count['B'] -= 2
            total += 45

        return total