# Django
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login

# Owns
from .models import Profile
from .helpers import *


class LoginView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user is None:
                response['message'] = 'Usuario invalido'
                raise Exception('Usuario invalido')
            
            #If not
            if Profile.objects.filter(user = check_user).first().is_verified:
                response['message'] = 'Tu usuario no esta verificado'
                raise Exception('Usuario no verificado')
                
            
            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('Contraseña incorrecta')
                
            
        except Exception as e :
            print(e)
            
        return Response(response)
            

LoginView = LoginView.as_view()


class RegisterView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user:
                response['message'] = 'Este usuario ya existe'
                raise Exception('Este usuario ya existe')
            
            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generate_random_string(20)
            Profile.objects.create(user = user_obj , token = token)
            #send_mail_to_user(token , data.get('username'))
            response['message'] = 'User created '
            response['status'] = 200
            
                
        except Exception as e :
            print(e)
            
        return Response(response)
            
                
RegisterView = RegisterView.as_view()
        