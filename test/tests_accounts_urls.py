from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import index, loginPage, registerPage


class Test(SimpleTestCase):

    def indexo_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def loginPage_url_is_resolved(self):
        url = reverse('loginPage')
        self.assertEquals(resolve(url).func, loginPage)

    def registerPage_url_is_resolved(self):
        url = reverse('registerPage')
        self.assertEquals(resolve(url).func, registerPage)

