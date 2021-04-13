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

