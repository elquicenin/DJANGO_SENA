from . import models
from .serializers import UserserializerAdmin, Programaformacionserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# un decorador es un añadido a la clase
@api_view(['GET','POST'])
def UserAdmin(request):
    if request.method == 'GET':
        users = models.User.objects.all()
        users_serializer = UserserializerAdmin(users, many = True)
        return Response(users_serializer.data)
    
    if request.method == 'POST':
        users_serializer = UserserializerAdmin(data=request.data)
        if users_serializer.is_valid():
            user = users_serializer.save() 
            user.set_password(request.data['password'])  
            user.save()  
            return Response(users_serializer.data)
        return Response(users_serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
    # el pk es lo que va despues de una url funciona para captar datos desde la url
def UserDatailsAdmin(request, pk):

    user = get_object_or_404(models.User, id=pk)
    
    if not pk:
        return Response({'message': 'Faltó el ID'}, status=status.HTTP_400_BAD_REQUEST)
#-------------------------------SESION DEL METODO GET PARA ENCONTRAR UN SOLO USUARIO ----------------------------------------#
    # funcion para encontrar un solo usuario
    if request.method == 'GET':
            serializer = UserserializerAdmin(user)  
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
#-----------------------------------------------------------------------------------------------------------------------------#
#---------------------------------SESION DEL METODO PUT PARA ACTUALIZAR DATOS DEL USUSARIO------------------------------------#
    if request.method == 'PUT':
        user_serializer = UserserializerAdmin(user, data  = request.data, partial=True) #se le manda el usuario, y se le manda la data de cambio
        #con el partial=True no es necesario cambiar todos los campos, solo los que se les envia por medio del metodo PUT
        if user_serializer.is_valid():
            serializer = user_serializer.save() 
            serializer.set_password(request.data['password'])  
            serializer.save()
            return Response({"message": "cambios existosos","user": user_serializer.data}, status= status.HTTP_200_OK)
        return Response({
            "message": "Datos no guardados con éxito",
            "errors": user_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
#------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------SESION METODO DELETE-------------------------------------------------------------#
    if request.method == 'DELETE':
            user.delete()
            return Response({'message ':'se elimino existosamente'}, status= status.HTTP_200_OK )
#------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------SESION METODOS PROGRMAS DE FORMACION ----------------------------------------------#
@api_view(['GET', 'POST'])
def PF_admin(request):
    if request.method == 'GET':
        Programas_form = models.ProgramaFormacion.objects.all()
        programas_form_serializers = Programaformacionserializer(Programas_form, many = True)
        return Response(programas_form_serializers.data)

    if request.method == 'POST':
        PF_serializers = Programaformacionserializer(data = request.data)
        if PF_serializers.is_valid():
            PF_serializers.save()
            return Response(PF_serializers.data)
        return Response(PF_serializers.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def PfDetailsAdmin(request, pk):
    Pf_user = get_object_or_404(models.ProgramaFormacion, id= pk)

#------------------------------------------SESION METODO PUT------------------------------------------------------------#
    if request.method == 'GET':
        Program_form = Programaformacionserializer(Pf_user)
        return Response ({'message':'promagrama de formacion', 'Pf_user': Program_form.data}, status=status.HTTP_200_OK)
#----------------------------------------------------------------------------------------------------------------------#

#------------------------------------------SESION METODO PUT------------------------------------------------------------#
    if request.method == 'PUT':
        Program_form = Programaformacionserializer (Pf_user, data = request.data, partial=True)
        if Program_form.is_valid():
            Program_form.save()
            return Response({'message': 'cambios guardados exitosamente', 'Program_form': Program_form.data },status=status.HTTP_200_OK)
        return Response({'message': 'cambios no validos', 'errors': Program_form.error_messages}, status=status.HTTP_400_BAD_REQUEST)
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------SESION METODO DELETE----------------------------------------------------------#
    if request.method == 'DELETE':
        Pf_user.delete()
        return Response({'message':'programa de formacion eliminado con exito'}, status=status.HTTP_200_OK)
#------------------------------------------------------------------------------------------------------------------------#
