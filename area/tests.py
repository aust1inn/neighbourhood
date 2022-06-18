from django.test import TestCase
from .models import *
# Create your tests here.


class HoodTest(TestCase):
    def setUp(self):
        self.Githu = Location.objects.create(name='Githu')

        self.malton = Hood.objects.create(
            hood_name='malton',occupants_count =1, location=self.Githu)

    def test_instance(self):
        self.malton.save()
        self.assertTrue(isinstance(self.malton, Hood))

    def test_get_hoods(self):
        self.malton.save()
        hoods = Hood.get_hoods()
        self.assertTrue(len(hoods) > 0)

   

class BusinessTest(TestCase):
    def setUp(self):
        self.viatu= Business.objects.create(b_name='viatu-fresh',b_description='fundi sawa',b_email='fundi.test.com')

    def test_instance(self):
        self.viatu.save()
        self.assertTrue(isinstance(self.viatu,Business))

    def test_get_business(self):
        self.viatu.save()
        business = Business.get_business()
        self.assertTrue(len(business) >0 )

class PostsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='aust1inn')
        self.Githu = Location.objects.create(name='Githu')

        self.malton = Hood.objects.create(
            hood_name='malton',occupants_count =1, location=self.Githu)

        self.security= Posts.objects.create(title='power outage',content='kplc needs to do sth',posted_by= self.user, hood= self.malton)

    def test_instance(self):
        self.security.save()
        self.assertTrue(isinstance(self.security,Posts))

    def test_delete_posts(self):
        self.security.save()
        self.security.delete()
        self.assertTrue(len(Posts.objects.all()) == 0)