import pytest
from accelerate_runner.solution_tests.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def setup_method(self):
        self.solution = CheckoutSolution()

    def test_valid_skus(self):
        assert self.solution.checkout("A") == 50
        assert self.solution.checkout("AA") == 100
        assert self.solution.checkout("AAA") == 130
        assert self.solution.checkout("AAAAA") == 200
        assert self.solution.checkout("AAAAAA") == 250
        assert self.solution.checkout("B") == 30
        assert self.solution.checkout("BB") == 45
        assert self.solution.checkout("C") == 20
        assert self.solution.checkout("D") == 15
        assert self.solution.checkout("E") == 40
        assert self.solution.checkout("EEB") == 80
        assert self.solution.checkout("FFF") == 20
        assert self.solution.checkout("FFFFFF") == 40

    def test_invalid_skus(self):
        assert self.solution.checkout("a") == -1
        assert self.solution.checkout("1") == -1
        assert self.solution.checkout("ABCa") == -1
        assert self.solution.checkout("") == 0

    def test_mixed_skus(self):
        assert self.solution.checkout("ABCD") == 115
        assert self.solution.checkout("AAABBB") == 205
        assert self.solution.checkout("EEBB") == 110
        assert self.solution.checkout("EEEBB") == 125
        assert self.solution.checkout("ABCDEABCDE") == 280