from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done(self):
        item = Item.objects.create(name='Test done')
        self.assertFalse(item.done)
