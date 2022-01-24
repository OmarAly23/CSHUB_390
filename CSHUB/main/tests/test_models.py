from django.test import TestCase
from main.models import User

class BaseModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.user = User(first_name='TechnoKing', last_name='Elon', email='TechnoE@gmail.com', password='@#@')
        cls.user.save()


class UserModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(self.user.first_name, 'TechnoKing')
        self.assertEqual(self.user.last_name, 'Elon')
        self.assertEqual(self.user.email, 'TechnoE@gmail.com')
        self.assertEqual(self.user.password, '@#@')

