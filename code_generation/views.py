from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .mixins import CustomMixin
from django.views.generic import View,DetailView
from django.contrib.auth import authenticate,login,logout
from .models import User_codes,User,profile
from .forms import admininput,User_form,Login_form
from .dacorators import roles_allowed
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from .serialisers import User_Create_serialiser,code_serialisers,Login_serialiser



class LoginView(APIView):
    def post(self,request):
        serialiser=Login_serialiser(data=request.data)
        serialiser.is_valid(raise_exception=True)
        user=serialiser.validated_data['user']
        login(request,user)
        token,created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=200)

class logoutApi(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        logout(request)
        return Response({'message':'logout the user'},status=200)


# class Home(CustomMixin,View):
#     auth_template_name='exercise/List code.html'
#     template_name     = 'exercise/home.html'
#     def get(self,request):
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 data=User_codes.objects.all()
#             else:
#                 try:
#                     data=User_codes.objects.filter(is_used=True)
#                     template = self.auth_template_name
#                     return render(request, template, context={'tittle': 'Home Page', 'data': data})
#                 except User.DoesNotExist:
#                     messages.info(request,'there is no active data found')
#                 except:
#                     messages.error(request,'Some thing went wrong please try again')
#
#         return render(request,self.template_name,{'tittle':"Home Page"})
class Home(CustomMixin,View):
    auth_template_name='exercise/List code.html'
    template_name     = 'exercise/home.html'
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data=User_codes.objects.all()
                template=self.auth_template_name
                return render(request, template, context={'tittle': 'Home Page', 'data': data})
            else:
                try:
                    data = User_codes.objects.filter(is_used=True)
                    template = self.auth_template_name
                    return render(request, template, context={'tittle': 'Home Page', 'data': data})
                except User_codes.DoesNotExist:
                    messages.error(request, 'There no used code is avalilable')
                    return render(request, self.template_name, {'tittle': 'Home'})

        return render(request, self.template_name, {'tittle': "Home Page"})



@method_decorator(roles_allowed,name='dispatch')
@method_decorator(login_required(login_url='login/'),name='dispatch')
class generation(CustomMixin,View):
    template_name='exercise/Admin_input.html'
    form_class=admininput
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={'tittle':'Admin input','form':self.form_class})

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST or None)
        if form.is_valid():
            self.num=request.POST['code_num']
            for i in range(int(self.num)):
                try:
                    code=self.get_uid()
                    code_genrated=User_codes.objects.create(codes=code,user=request.user)
                except ValueError:
                    raise ValueError('There some invalid data found')

            return redirect('/')

        return render(request,self.template_name,context={'tittle':'Admin input','form':self.form_class})


class Create_User(View):
    form_class      =User_form
    template_name   ='Accounts/User_creat.html'

    def get(self,request,*args,**kwargs):
        template    ='exercise/Signup.html'
        context     ={'tittle':'User From','user_form':self.form_class}
        return render(request,template,context=context)

    def post(self,request,*args,**kwargs):
        User_form = self.form_class(request.POST or None)
        try:

            if User_form.is_valid():
                data=request.POST
                user = User(email=data['email'],username  =data['username'],
                            first_name  =data['first_name'],last_name =data['last_name'],
                            )
                user.set_password(raw_password=data['password'])
                user.save()
                user_profile=profile.objects.create(mobile_num=data['mobile_num'],
                            first_name  =data['first_name'],last_name =data['last_name'],user=user)

                messages.success(request,'The user is created successfully')
                user=authenticate(username=data['username'],password=data['password'])
                if user is not None:
                    login(request, user)
                return HttpResponseRedirect('/')

        except AttributeError:
            messages.error(request, 'There is some error try latter')
        except TypeError:
            messages.error(request, 'There is some error try latter')

        except ValueError:
            messages.error(request,'you have entered some wrong input')
        return HttpResponseRedirect('/')

#for the user login
class Login_User(View):
    form_class      =Login_form
    template_name   ='exercise/Login Page.html'

    def get(self,request,*args,**kwargs):
        context ={'tittle':'Login form','form':self.form_class}
        template=self.template_name
        return render(request,template,context=context)

    def post(self,request,*args,**kwargs):
        form    =self.form_class(request.POST or None)
        context = {'title': 'Login', 'form': form}
        template=self.template_name
        if form.is_valid():
            username=form.cleaned_data['username']
            user =authenticate(username=username,
                              password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
        return render(request,template,context=context)



@login_required(login_url='login/')
def Logout_User(request):
    logout(request)
    return HttpResponseRedirect('/')


@method_decorator(login_required(login_url='login/'),name='dispatch')
@method_decorator(roles_allowed,name='dispatch')
class Code_view(View):
    template_name = 'exercise/Detail Page.html'
    def get(self,request,id,*args,**kwargs):
        try:
            data = User_codes.objects.get(id=id)
            data.count+=1
            data.save()
            return render(request,self.template_name,{'tittle':'Detail Page','data':data})
        except User_codes.DoesNotExist:
            messages.info(request,'The is no data found')

        except:
            messages.info(request,'Some thing went wrong ')
            return redirect('Home')





class User_view(APIView):
    def post(self,request):
        serialser=User_Create_serialiser(data=request.data)
        if serialser.is_valid():
            return Response({'message':'User is created successfully'})

class CodeViewSet(viewsets.ModelViewSet):
    serializer_class =code_serialisers
    queryset = User_codes.objects.filter(is_used=True)
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminUser]
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        def get_object(self):
            obj=super().get_object()
            obj.count+=1
            obj.save()
            return obj
        # do your customization here
        instance=get_object(self)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

