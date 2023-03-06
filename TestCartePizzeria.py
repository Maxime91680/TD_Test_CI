from mock import Mock
import unittest
from CartePizzeria import CartePizzeria
from CartePizzeria import CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        pizza = Mock()
        self.cartepizzeria_vide = CartePizzeria()

        self.cartepizzeria_non_vide = CartePizzeria()
        self.cartepizzeria_non_vide.pizzas = [pizza]
    
    def test_is_empty(self):
        self.assertTrue(self.cartepizzeria_vide.is_empty())

    def test_is_not_empty(self):
        self.assertFalse(self.cartepizzeria_non_vide.is_empty())

    def test_is_empty(self):
        assert self.cartepizzeria_vide.nb_pizzas() == 0

    def test_is_empty(self):
        assert self.cartepizzeria_non_vide.nb_pizzas() == 1

    def test_add_pizza(self):
        pizza = Mock()
        self.cartepizzeria_vide.add_pizza(pizza)
        self.assertEqual(self.cartepizzeria_vide.pizzas, [pizza])

    def test_add_pizza_liste_non_vide(self):
        pizza = Mock()

        lst =[]
        for pizza in self.cartepizzeria_non_vide:
            lst.append(pizza)
        self.cartepizzeria_non_vide.add_pizza(pizza)
        self.assertEqual(self.cartepizzeria_non_vide.pizzas, lst + [pizza])

    

if __name__ == "__main__":
    unittest.main()