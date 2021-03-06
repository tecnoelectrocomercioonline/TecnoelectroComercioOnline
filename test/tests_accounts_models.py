from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from accounts.views import loginPage, registerPage


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='testuser@test.com', password='test_pass')

    def auth_test(self):
        # Create an instance of a GET request.
        request = self.factory.get('/login/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = registerPage(request)
        # Use this syntax for class-based views.
        response = loginPage.as_view()(request)
        self.assertEqual(response.status_code, 200)
