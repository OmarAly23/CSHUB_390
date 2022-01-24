from django.test import Client
import main.views
import main.models
from main.models import User
from django.urls import reverse

client = Client()

response = client.get(reverse('signin'))
print(response.status_code)

user1 = User(first_name='TechnoKing', last_name='Elon', email='TechnoE@gmail.com', password='@#@')
user1.save()
