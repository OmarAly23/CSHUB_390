from django.test import TestCase
# Create your tests here.

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_loginpage(self):
        response = self.client.get('/signin')
        self.assertEqual(response.status_code, 301)

    def test_signuppage(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 301)

    def test_logoutpage(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 301)

    def test_addpage(self):
        response = self.client.get('/addPage')
        self.assertEqual(response.status_code, 301)