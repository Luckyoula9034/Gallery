from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.lucky= Editor(first_name = 'lucky', last_name ='Oula', email ='luckyoula.com')
    # Testing Save Method
    def test_save_method(self):
        self.lucky.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)    

