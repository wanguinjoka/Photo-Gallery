from django.test import TestCase
from .models import Location,Category,Photo

# Create your tests here.
#testing Save classmethod
class PhotoTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Photo(name = 'testpic', description='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
