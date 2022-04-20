from django.contrib.auth.models import AnonymousUser, User
from accounts.forms import UserRegisterForm


class TestForms(SimpleTestCase):

    def test_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'test',
            'email': 'test@example.com',
            'phone_no': '+506 88880000',
            'password1': 'passtest',
            'password2': 'passtest',
            'first_name': 'TestName',
            'last_name': 'TestLName'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
