import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from item.models import Product
from item.models import Category

class ProductModelTest(TestCase): 
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.user = User.objects.create_user(username='testuser')

        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            description='Test Description',
            price=9.99,
            created_by=self.user
        )

    def test_product_str_method(self):
        expected_str = 'Test Product'
        self.assertEqual(str(self.product), expected_str)

    def test_product_defaults(self):
        self.assertFalse(self.product.is_sold)
        self.assertIsNone(self.product.image)

    def test_product_created_at(self):
        self.assertIsInstance(self.product.created_at, datetime.datetime)

class PageTest(TestCase):
  def test(self):
    response = self.client.get('/')

    self.assertEqual(response.status_code, 200)
