from accounts.forms import HomeForm


class TestForms(SimpleTestCase):

    def test_form_valid_data(self):
        form = HomeForm(data={
            'name': 'test',
            'email': 'testmail@mail.com',
            'subject': 'TestSubject',
            'message': 'TestMessagee'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = HomeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
