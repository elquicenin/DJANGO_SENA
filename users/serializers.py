from rest_framework import serializers
from .models import User, ProgramaFormacion

# el UserserializarAdmin permite visualizar todos los datos de los ususarios
class UserserializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ['password']
        fields= '__all__'
        
class Programaformacionserializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaFormacion
        fields = '__all__'

