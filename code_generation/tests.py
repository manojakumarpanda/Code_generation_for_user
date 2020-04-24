import uuid
#import pytest
from django.test import TestCase,SimpleTestCase,Client,RequestFactory
from django.contrib.auth import get_user_model
from .models import profile,User_codes
from django.urls import resolve,reverse
from code_generation import views
from .forms import *


#
#
#
# class Test_models(TestCase):
#
#     @classmethod
#     def setUp(cls):
#         cls.User = get_user_model()
#         cls.user = cls.User.objects.create_user(username='normaluser1', email='normal@user.com', password='password',
#                                         first_name='normal', last_name='user')
#     def test_create_user(self):
#         User = get_user_model()
#         user=user = User.objects.create_user(username='normaluser', email='normal@user.com', password='password',
#                                         first_name='normal', last_name='user')
#         self.assertEqual(user.email, 'normal@user.com')
#         self.assertEqual(user.username, 'normaluser')
#         self.assertEqual(user.first_name, 'normal')
#         self.assertEqual(user.last_name, 'user')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNot(user.username,None)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(ValueError):
#             User.objects.create_user(username='')
#         with self.assertRaises(ValueError):
#             User.objects.create_user(username='', password="password")
#
#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(username='superuser',email='super@user.com',password= 'superpass')
#         self.assertEqual(admin_user.email, 'super@user.com')
#         self.assertEqual(admin_user.username, 'superuser')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNot(admin_user.username,None)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 username='superuser',email='super@user.com', password='foo', is_superuser=False)
#
#
#
#     def test_create_profile(self):
#         #profile_data=profile(mobile_num=9000777333,first_name='normal',last_name='user')
#         profile_created=profile.objects.create(mobile_num=9000777333,first_name='normal',last_name='user',user=self.user)
#         self.assertEqual(profile_created.first_name, 'normal')
#         self.assertEqual(profile_created.last_name, 'user')
#         self.assertEqual(profile_created.full_name, 'normal user')
#         self.assertEqual(profile_created.role,'employee')
#         self.assertEqual(profile_created.user,self.user)
#         self.assertEqual(profile_created.mobile_num,9000777333)
#
#
#     def test_profile(self):
#         #profile_data = profile(role='admin',mobile_num=9000777333, first_name='normal', last_name='user')
#         profile_created = profile.objects.create(role='admin',mobile_num=9000777333, first_name='normal', last_name='user',user=self.user)
#         self.assertEqual(profile_created.first_name, 'normal')
#         self.assertEqual(profile_created.last_name, 'user')
#         self.assertEqual(profile_created.full_name, 'normal user')
#         self.assertEqual(profile_created.role, 'admin')
#         self.assertEqual(profile_created.user, self.user)
#         self.assertEqual(profile_created.mobile_num, 9000777333)
#
#     def code_generation(self):
#         def getid():
#             uid = uuid.uuid4()
#             uid = str(uid).split('-')
#             code = ''.join(uid)[:14:]
#         code=getid()
#         code=User_codes.objects.create(user=self.user,codes=code)
#         self.assertEqual(code.user, self.user)
#         self.assertTrue(code.codes)
#         self.assertTrue(code.created_at)
#         self.assertFalse(code.count)
#         self.assertFalse(code.is_used)
#
#
# class Test_urls(SimpleTestCase):
#
#     def test_Home(self):
#         url=reverse('Home')
#         self.assertEquals(resolve(url).func.view_class,views.Home)
#         self.assertTrue(1)
#
#     def test_generate(self):
#         url=reverse('Generate')
#         self.assertEquals(resolve(url).func.view_class,views.generation)
#         self.assertTrue(1)
#
#     def test_signup(self):
#         url=reverse('Signup')
#         self.assertEquals(resolve(url).func.view_class,views.Create_User)
#         self.assertTrue(1)
#
#     def test_detail(self):
#         url=reverse('Detail',args=(1,))
#         self.assertEquals(resolve(url).func.view_class,views.Code_view)
#         self.assertTrue(1)
#
#     def test_profile(self):
#             url=reverse('Profile')
#             self.assertEquals(resolve(url).func.view_class,views.Code_view)
#             self.assertTrue(1)
#
#     def test_apilogin(self):
#                 url=reverse('Api_Login')
#                 self.assertEquals(resolve(url).func.view_class,views.LoginView)
#                 self.assertTrue(1)
#
#     def test_apilogout(self):
#                     url=reverse('Api_Logout')
#                     self.assertEquals(resolve(url).func.view_class,views.logoutApi)
#                     self.assertTrue(1)
#
#
#     def test_apicreate(self):
#                         url=reverse('Api_Create')
#                         print(resolve(url))
#                         self.assertEquals(resolve(url).func.view_class,views.User_view)
#                         self.assertTrue(1)
#
#
#     def test_Login(self):
#             url=reverse('Login')
#             print(resolve(url))
#             self.assertEquals(resolve(url).func.view_class,views.Login_User)
#             self.assertTrue(1)
#
#     def test_Logout(self):
#         url=reverse('Logout')
#         self.assertEquals(resolve(url).func,views.Logout_User)
#         self.assertTrue(1)
#
#
# class Test_forms(TestCase):
#
#     @classmethod
#     def setUp(cls):
#         cls.User = get_user_model()
#         cls.user = cls.User.objects.create_user(username='normaluser1', email='normal@user.com', password='password',
#                                             first_name='normal', last_name='user')
#
#     def test_code(self):
#         form=admininput(data={'code_num':0})
#         self.assertFalse(form.is_valid())
#
#         form=admininput(data={'code_num':1})
#         self.assertTrue(form.is_valid())
#
#     def test_user_form(self):
#         form1=User_form(data={
#             'username':'user','password':'password1','repassword':'password1',
#             'first_name':'user','last_name':'name','mobile_num':80482093,'email':'user@emil.com'
#         })
#         form2=User_form(data={
#             'username':'','password':'password1','repassword':'password1',
#             'first_name':'user','last_name':'name','mobile_num':80482093,'email':'user@emil.com'
#         })
#         form3=User_form(data={
#             'username':'user','password':'password11','repassword':'password1',
#             'first_name':'user','last_name':'name','mobile_num':80482093,'email':'user@emil.com'
#         })
#         form4=User_form(data={
#             'username':'user','password':'password1','repassword':'password1',
#             'first_name':'','last_name':'name','mobile_num':80482093,'email':'user@emil.com'
#         })
#         form5=User_form(data={
#             'username':'user','password':'password1','repassword':'password1',
#             'first_name':'user','last_name':'','mobile_num':80482093,'email':'user@emil.com'
#         })
#         form6=User_form(data={
#             'username':'user','password':'password1','repassword':'password1',
#             'first_name':'user','last_name':'name','mobile_num':'80482093','email':'user@emil.com'
#         })
#         form5=User_form(data={
#             'username':'user','password':'password1','repassword':'password1',
#             'first_name':'','last_name':'name','mobile_num':80482093,'email':'useremil.com'
#         })
#         form6=User_form(data={
#             'username':'','password':'','repassword':'',
#             'first_name':'','last_name':'','':432,'email':''
#         })
#         # form6=User_form(data={
#         #     'username':'user','password':'password1','repassword':'password1',
#         #     'first_name':'user','last_name':'name','mobile_num':'80482093','email':'user@emil.com'
#         # })
#
#         self.assertTrue(form1.is_valid())
#         self.assertFalse(form2.is_valid())
#         self.assertFalse(form3.is_valid())
#         self.assertFalse(form4.is_valid())
#         self.assertFalse(form5.is_valid())
#         self.assertFalse(form6.is_valid())
#
#
#     def test_login(self):
#         form1=Login_form(data={'username':'username','password':'password1'})
#         form2=Login_form(data={'username':'','password':'password1'})
#         form3=Login_form(data={'username':'username','password':''})
#         form4=Login_form(data={'username':'','password':''})
#
#         self.assertTrue(form1.is_valid())
#         self.assertFalse(form2.is_valid())
#         self.assertFalse(form3.is_valid())
#         self.assertFalse(form4.is_valid())
#
#
class Test_views(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client=Client()
        cls.request=RequestFactory()
        cls.User = get_user_model()
        cls.user = cls.User.objects.create_user(username='normaluser1', email='normal@user.com', password='password',
                                                first_name='normal', last_name='user')

        cls.home=reverse('Home')

    def test_home(self):
        self.url=reverse('Home')
        request=self.request.get(self.url,{'pk':1}, {'name':'Not'})
        responce = self.client.get(self.url)
        self.assertEquals(request.GET['pk'],'1')
        self.assertTrue('name' in request)
        self.assertNotEquals(request.GET['pk'],'2')
        self.assertEquals(responce.status_code,200)
        self.assertTemplateUsed(responce,template_name='exercise/home.html')

    def test_logout(self):
        self.url=reverse('Logout')
        responce=self.client.get(self.url)
        self.assertEquals(responce.status_code,302)
        self.assertEquals(responce.url,'login/?next=/exercise/logout/')

    @classmethod
    def tearDownClass(cls):
        cls.user=get_user_model()
        status,user=cls.user.objects.get(id=1).delete()

