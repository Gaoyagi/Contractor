# tests.py

from unittest import TestCase, main as unittest_main
from app import app
from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId

sample_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_deck = { 'img': "static/red.jpeg",  'description': 'Red playing cards' }
sample_data = {
    'img': sample_deck['img'],
    'description': sample_deck['description']
}

sample_id = ObjectId('5d55cffc4a3d4031f42827a4')
sample_item = { 'img': "static/red.jpeg",  'description': 'Red playing cards', 'quantity': 1}
sample_item = {
    'img': sample_item['img'],
    'description': sample_item['description'],
    'quantity': sample_item['quantity']
}

class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""
        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    #tests shop home page
    def test_index(self):
        result = self.client.get('/index')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Deck of Cards', result.data)

    #tests cart view page
    def test_cart(self):
        result = self.client.get('/cart')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Currently in cart', result.data)
    
    #tests checkout page
    def test_new(self):
        result = self.client.get('/cart/checkout')
        self.assertEqual(result.status, '405 METHOD NOT ALLOWED')

if __name__ == '__main__':
    unittest_main()