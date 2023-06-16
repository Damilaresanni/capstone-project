from django.test import TestCase
from Restuarant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Rice", price=100, inventory =129)
        self.assertEqual(str(item), 'Rice : 100')