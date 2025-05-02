from lib.solutions import checkout_solution

class Test_CHK:
    def test_CHK(self):
        assert checkout_solution.CheckoutSolution().checkout("A") == 50
        assert checkout_solution.CheckoutSolution().checkout("ABCD") == 115
        assert checkout_solution.CheckoutSolution().checkout("AAAAA") == 175
        
