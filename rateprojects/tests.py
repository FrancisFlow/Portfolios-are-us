from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.francis=User(username="Francis", email="Francis@example.com", password="password" )
        self.profile=Profile(user=self.francis, profile_pic='image.jpg', phone_number=2222222222, bio='I am developers')
        self.francis.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.francis, User))

class ProjectTestClass(TestCase):
    def setUp(self):
        self.francis=User(username="Francis", email="Francis@example.com", password="password" )
        self.project=Project(project_name='blank', image='image2.jpg', link='http://example.com', categories='website', user=self.francis)

        self.francis.save()
        self.project.save_project()

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()

    def test_project_instanct(self):
        self.assertTrue(isinstance(self.project, Project)) 


    def test_search_project(self):
        project=Project.search_by_name('blank')
        self.assertTrue(project.image=='image2.jpg')
    
    def test_delete_project(self):
        projectX=Project.objects.all()
        self.assertEqual(len(projectX),1)
        self.project.delete_project()
        projectY= Project.objects.all()
        self.assertEqual(len(projectY),2)



