from django.test import TestCase, Client
from Restuarant.models import Menu
from Restuarant.serializers import MenuSerializer




class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title= "Rice", price=120, inventory=20)
        Menu.objects.create(title= "Beans", price=150, inventory=30)
        Menu.objects.create(title= "Beef", price=270, inventory=40)
        Menu.objects.create(title= "wheat", price=220, inventory=50)
        
  
    def test_getall(self):
        request = self.client.get(path='/restuarant/menu/')
        response = request.data
        menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(menu_items, many=True).data
        self.assertEqual(request.status_code , 200 )
        self.assertEqual(response, serialized_items)