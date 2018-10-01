from django.test import TestCase
from .models import Location,Category,Photo

# Create your tests here.
#testing Save classmethod
class PhotoTestClass(TestCase):

    def setUp(self):
        # Creating a new photo and saving it
        self.testpic= Photo(name = 'testpic', description='Muriuki', email ='james@moringaschool.com')
        self.testpic.save_()

        # Creating a new location and saving it
        self.testloc = Location(name = 'Nairobi')
        self.new_testloc.save()

        self.new_category= Category(name = 'nightlife')
        self.new_category.save()

    def tearDown(self):
        Photo.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_copy_image(self):
        self.new_Photo.save_Photo()
        Photo.copy_image("")

        self.assertEqual(self.new_Photo.photo_image,pyperclip.paste())
