class Test_CHK:
    def test_CHK(self):
        from solutions.CHK import checkout_solution

        assert checkout_solution.CheckoutSolution().checkout("A") == 50
        assert checkout_solution.CheckoutSolution().checkout("ABCD") == 115
        assert checkout_solution.CheckoutSolution().checkout("AAAAA") == 175
        