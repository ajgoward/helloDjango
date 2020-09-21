from django.test import TestCase
from .models import Item


class TestDjango(TestCase):

    def test_get_todolist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def edit_item_page(self):
        item = Item.objects.create(name='Test to do')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def can_add_item(self):
        response = self.client.post('/add', {'name': 'test'})
        self.assertRedirects(response, '/')

    def can_toggle(self):
        item = Item.objects.create(name='Test to do')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')

    def can_delete(self):
        item = Item.objects.create(name='Test to do', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
