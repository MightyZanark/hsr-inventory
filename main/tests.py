from django.test import TestCase
from main.models import Item

class MainTest(TestCase):
    def test_item_have_all_attribute(self):
        item1 = Item.objects.create(
                    name="Traveler's Guide",
                    amount=100,
                    description="Lorem ipsum",
                    category="CHAR_EXP"
                )
        
        self.assertEqual(item1.name, "Traveler's Guide")
        self.assertEqual(item1.amount, 100)
        self.assertEqual(item1.description, "Lorem ipsum")
        self.assertEqual(item1.category, "CHAR_EXP")
