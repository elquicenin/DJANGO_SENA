from . import models
from .serializers import LoginAdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['POST'])
def LoginAdmin(request):

        if request.method == 'POST':
            correo = request.data.get('correo_electronico')
            password = request.data.get('password')

            if not correo or not password:
                return Response({'message': 'Correo y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = models.User.objects.get(correo_electronico=correo)
            except models.User.DoesNotExist:
                return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            if not user.check_password(password):
                return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

            serializer = LoginAdminSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['POST'])
def LoginEmpresa(request):

    if request.method == 'POST':
        # tipo_documento = request.data.get('tipo_de_documento')
        rol = request.data.get('Rol')
        documento = request.data.get('numero_de_documento')
        correo = request.data.get('correo_electronico')
        password = request.data.get('password')

        if not rol:
            return Response({'message: no eres empresa'}, status=status.HTTP_404_NOT_FOUND)

        if not correo or not password or not documento:
            return Response({'message: campos requeridos'}, status=status.HTTP_404_NOT_FOUND)
        try:
            user = models.user_login.objects.get(numero_documento=documento)
        except models.user_login.DoesNotExist:
            return Response({'message: usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(password):
            serializer = LoginAdminSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)