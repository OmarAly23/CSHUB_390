import sys, os
import django
from main import models
from main.models import User
from main.models import Resource

sys.path.insert(0, "/path/to/parent/of/courseware") # /home/projects/my-djproj

# from manage import DEFAULT_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'CSHUB.settings')
django.setup()



resource_connection = Resource.objects.all()

print(resource_connection)
