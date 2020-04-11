from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'code',views.CodeViewSet,base_name='codes')

urlpatterns =[
    path('',views.Home.as_view(),name='Home'),
    path('generate/',views.generation.as_view(),name='Generate'),
    path('login/',views.Login_User.as_view(),name='Login'),
    path('signup/',views.Create_User.as_view(),name='Signup'),
    path('logout/',views.Logout_User,name='Logout'),
    path('codes/<int:id>/',views.Code_view.as_view(),name='Detail'),
    path('profile/',views.Code_view.as_view(),name='Profile'),
    path('api/',include(router.urls)),
    # path('api/',views.CodeViewSet.as_view()),
    # path('api/<int:pk>',views.CodeDetail.as_view()),
    path('api/login/',views.LoginView.as_view()),
    path('api/logout/',views.logoutApi.as_view()),
    path('api/create/',views.User_view.as_view()),

]
             # +router.urls