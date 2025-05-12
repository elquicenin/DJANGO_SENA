import cuid
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.

class User(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=25,
        default=cuid.cuid,
        unique=True,
        editable=False
    )
    TipoDocumento = [
        (1, 'CC'),
        (2, 'CE'),
        (3, 'NIT')
    ]
    numero_de_documento = models.IntegerField(unique=True)  
    tipo_de_documento = models.IntegerField(choices=TipoDocumento)
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    direccion = models.TextField()
    correo_electronico = models.EmailField(unique=True, max_length=255)
    razon_social = models.CharField(max_length=255, default="no es empresa", unique=True)
    actividad_economica = models.CharField(default="desempleado", max_length=255)
    password = models.CharField(max_length=255)
    ESTADOS = [
        (1, 'activo'),
        (2, 'inactivo')
    ]
    estado = models.IntegerField(choices = ESTADOS, default = 1)
    numero_de_telefono = models.CharField(max_length = 10, unique=True)
    ROLES = [
        (1, 'administrador'),
        (2, 'empresa'),
        (3, 'sub_administrador'),
    ]
    rol = models.IntegerField(choices = ROLES, default = 1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255,blank = True, null=True)

    def crear_token(self):
        import secrets
        self.token = secrets.token_hex(32)
        self.save()
        return self.token
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)     
        # Esta función toma una contraseña sin encriptar (raw_password)
        # y la convierte en una versión segura (hasheada) usando make_password,
        # que es una función de Django para proteger contraseñas.
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
        # Esta función compara una contraseña sin encriptar (raw_password)
        # con la contraseña encriptada almacenada en self.password.
        # Devuelve True si coinciden, False si no.





class ProgramaFormacion(models.Model):
    #Definicion de los campos
    id = models.CharField(
        primary_key=True,
        max_length=25,
        default=cuid.cuid,
        unique=True,
        editable=False
    )
    nombre_pf = models.CharField( max_length = 50)
    duracion =  models.IntegerField()
    
    PROGRAMAS = [
        (1, 'tecnico'),
        (2,'tecnologo'),
        (3,'operario')
    ]
    niveles_formacion = models.IntegerField(choices = PROGRAMAS, default = '1')

    ESTADOS = [
        (1, 'activo'),
        (2, 'inactivo'),
        (3, 'suspendido')
    ]
    estado = models.IntegerField(choices = ESTADOS, default = 1)
    #el area es la zona de la parte del CDITI ejm ==> (ADSO = Software)

