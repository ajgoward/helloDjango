from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required')

    def done_is_not_required(self):
        form = ItemForm({'name': 'testing'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
