from django.test import Client


c = Client()
response = c.post('/signin', {'first_name': 'testing', 'last_name': 'lname', 'email': 'test@gmail.com', 'password': '123t'})
print(response.status_code)


