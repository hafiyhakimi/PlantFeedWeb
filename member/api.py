from ast import Delete
import json
from pyexpat import model
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get(user=user)
        return Response(token.key)

class UserList(APIView):

    def get(self, request):
        model =Person.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Login
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    body = json.loads(request.body)
    email = body['email'] 
    password = body['password']

    try:
        Account = Person.objects.get(Email=email, Password=password)
        token = Token.objects.get_or_create(user=Account)[0].key
        user = Token.objects.get(key=token).user
        print(user.Name)
        Res = {
            "Name": Account.Name,
            "Age": Account.Age,
            "DateOfBirth": Account.DateOfBirth,
            #"email": Account.Email,
            "Username":Account.Username,
            "Email": Account.Email,
            "token": token
            
        }
        return Response(Res)
    except BaseException as e:
         return Response({'message': 'Incorect Email or Password'})
        #raise ValidationError({"400": f'{str(e)}'})

#Get user from token
@api_view(['GET'])
@permission_classes([AllowAny])
def getUserFromToken(request, pk):
    user = Token.objects.get(key=pk).user
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)


