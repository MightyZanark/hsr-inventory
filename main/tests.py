from django.test import TestCase, Client
from main.models import Item

class MainTest(TestCase):
    def test_item_have_all_attribute(self):
        item1 = Item.objects.create(
                    name="Refined Aether",
                    amount=100,
                    description="Lorem ipsum",
                    category="LC_EXP"
                )
        
        self.assertEqual(item1.name, "Refined Aether")
        self.assertEqual(item1.amount, 100)
        self.assertEqual(item1.description, "Lorem ipsum")
        self.assertEqual(item1.category, "LC_EXP")
    
    def test_item_default_category(self):
        item = Item.objects.create(
                    name="Traveler's Guide",
                    amount=100,
                    description="Lorem ipsum",
                )
        
        self.assertEqual(item.category, "CHAR_EXP")
