from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_lista_portafolios_existentes(self):
        image_list = self.client.get('/gallery/', format='json')
        self.assertEqual(image_list.status_code, 200)

    def test_contar_portafolio(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)
        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_add_user(self):
        response = self.client.post('/gallery/addUser/', json.dumps(
            {"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5",
             "email": "test@test.com"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0], 'testUser')

