# import pytest
# from unittest import TestCase
# from code_generation.models import *
# import uuid
# from django.contrib.auth import get_user_model
# import mixer
#
# class Test_models(TestCase):
#
#     @classmethod
#     def setUp(cls):
#         cls.User = get_user_model()
#         cls.user = cls.User.objects.create_user(username='normaluser1', email='normal@user.com', password='password',
#                                         first_name='normal', last_name='user')
#
#
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


# import pytest
# from unittest import TestCase
# from django.contrib.auth import get_user_model
#
#
#
# class Test_model(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.user = get_user_model()
#
#     def test_user_create(self):
#         self.user=get_user_model()
#         user=self.user.objects.create_user(username='john', email='lennon@thebeatles.com',password= 'johnpassword')
#         assert 2!= 1
#         assert self.user.objects.count() == 1
#         assert user.username=='john'
#
#     def test_username_taken(self):
#         self.taken=self.user.objects.create_user(username='jhon',password='jhonpass')
#         assert self.taken


# class Test_models:
#     @staticmethod
#     def func(x):
#         return x+1
#
#     def test_answer(self):
#         assert Test_models.func(3) != 5

