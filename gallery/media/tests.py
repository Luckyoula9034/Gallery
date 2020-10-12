from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'lucky', last_name ='Oula', email ='luckyoula.com')

