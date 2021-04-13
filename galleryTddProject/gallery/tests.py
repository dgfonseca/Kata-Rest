from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image
import json


# Create your tests here.
class GalleryTestCase(TestCase):

    def index(request):
        images_list = Image.objects.all()
        return HttpResponse(serializers.serialize("json", images_list))
