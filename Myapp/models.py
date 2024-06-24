from django.db import models

# Create your models here.

class Tipo_obra(models.Model):
    medium = models.CharField(max_length=20, blank=False, null=False)
    id_obra = models.AutoField(db_column='idObra', primary_key=True)
    
    def __str__(self):
        return str(self.medium)
    
    
class Obra(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.TextField()
    autor = models.CharField(max_length=20)
    tipo_obra = models.ForeignKey(Tipo_obra, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return str(self.nombre)
    
    
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "cotizacion"]

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre