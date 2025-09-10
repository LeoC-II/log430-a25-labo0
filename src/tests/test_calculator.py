"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

class TestCalculator():
    my_calculator = Calculator()
    def test_app(self):
        assert TestCalculator.my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

    # TODO: ajoutez les tests
    def test_addition(self):
        assert TestCalculator.my_calculator.addition(2, 3) == (2+3)

    def test_subtraction(self):
        assert TestCalculator.my_calculator.subtraction(2, 3) == (2-3)

    def test_multiplication(self):
        assert TestCalculator.my_calculator.multiplication(2, 3) == (2*3)

    def test_division(self):
        assert TestCalculator.my_calculator.division(2, 3) == (2/3)

    def test_division_by_zero(self):
        assert TestCalculator.my_calculator.division(2, 0) == "Erreur : division par zéro"