from . import models
from rest_framework import serializers



class LoginAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'correo_electronico', 'token']
    
    def Validate(self, fields):
        fields.crear_token()
        return {
            'user_id': fields.id,
            'correo_electronico': fields.correo_electronico,
            'token': fields.token
        }


class LoginEmpresaSerializars(serializers.Serializer):
    numero_de_documento = serializers.CharField()

    def validate(self, data):
        documento = data.get('numero_de_documento')

        try:
            user = models.User.objects.get(numero_de_documento= documento)

        except models.User.DoesNotExist:
            raise serializers.ValidationError('user not found')
        
        token = user.crear_token()

        return {
            'user_id': user.id,
            'token': token
        }