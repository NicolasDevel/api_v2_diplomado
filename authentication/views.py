from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    #Lo primero realizar es obtener el usuario y contraseña que han sido enviados
    username_from_client = request.data.get('username')
    password_from_client = request.data.get('password')

    #Validamos que el usuario exista en la bd
    user = authenticate(username = username_from_client, password = password_from_client)

    #Generamos el token si la autenticacion fue un exito
    if user: 
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'refresh' : str(refresh),
                'token' : str(refresh.access_token)
            },
            status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'error' : "Credenciales invalidas"
            },
            status.HTTP_401_UNAUTHORIZED
        )

