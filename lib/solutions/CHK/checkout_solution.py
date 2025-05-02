from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        count = Counter(skus)
        total = 0

        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1
        
        
        # Handle F
        group_of_3 = count['F'] // 3
        rem_3 = count['F'] % 3

        total += group_of_3 * 20 + rem_3 * 10

        # Handle E
        while count['E'] >= 2 and count['B'] >= 1:
            count['B'] -= 1
            count['E'] -= 2
            total += 80
        
        # Handle B
        while count['B'] >= 2:
            count['B'] -= 2
            total += 45

        # Handle A
        group_of_5 = count['A'] // 5
        rem_5 = count['A'] % 5 

        group_of_3 = rem_5 // 3
        rem_3 = rem_5 % 3

        total += group_of_5 * 200 + group_of_3 * 130 + rem_3 * 50
            
        # the remaining skus
        total += count['B'] * 30
        total += count['C'] * 20
        total += count['D'] * 15
        total += count['E'] * 40
        
        return total
    

    def handle_A(self, count: Counter, total: int) -> int:
        """ Divide into groups of 3 and 5, calculate the min total"""
       
