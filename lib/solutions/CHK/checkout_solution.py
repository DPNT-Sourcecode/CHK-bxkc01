from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        count = Counter(skus)
        total = 0

        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1

        while count['A'] >= 3:
            count['A'] -= 3
            total += 130

        while count['B'] >= 2:
            count['B'] -= 2
            total += 45
            
        total += count['A'] * 50 
        total += count['B'] * 30
        total += count['C'] * 20
        total += count['D'] * 15
        
        return total


