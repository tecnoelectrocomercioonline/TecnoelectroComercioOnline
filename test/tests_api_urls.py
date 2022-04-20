from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import *


class Test(SimpleTestCase):

    def api_url_is_resolved(self):
        url = reverse('api')
        self.assertEquals(resolve(url).func, api)

    def api_auth__url_is_resolved(self):
        url = reverse('catalogo')
        self.assertEquals(resolve(url).func, catalogo)
