from todo.models import Product
from django.test import TestCase

# Create your tests here.

class ProductModelTests(TestCase):
    def test_check_if_instance_is_created_with_not_done_by_default(self):
        new_product = Product()
        self.assertEqual(new_product.done, True, 'Newly created product should be not done by default')
