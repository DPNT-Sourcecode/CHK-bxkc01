from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        count = Counter(skus)
        total = 0

        if any(not sku.isalpha() or not sku.isupper() for sku in skus):
            return -1
        
        
        # Handle F
        group_of_F3 = count['F'] // 3
        rem_F3 = count['F'] % 3

        total += group_of_F3 * 20 + rem_F3 * 10

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
        group_of_A5 = count['A'] // 5
        rem_A5 = count['A'] % 5 

        group_of_A3 = rem_A5 // 3
        rem_A3 = rem_A5 % 3

        total += group_of_A5 * 200 + group_of_A3 * 130 + rem_A3 * 50
            
        # the remaining skus
        total += count['B'] * 30
        total += count['C'] * 20
        total += count['D'] * 15
        total += count['E'] * 40

        return total
       
