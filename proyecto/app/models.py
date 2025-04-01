from django.db import models

# Create your models here.
# Modelo para guardar los productos en la base de datos.
class Producto(models.Model):
    CATEGORIAS = (
        ('Electronica', 'Electrónica'),
        ('Ropa', 'Ropa'),
        ('Hogar', 'Hogar'),
        ('Belleza', 'Belleza'),
        ('Libros', 'Libros'),
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='Electronica')

    def __str__(self):
        return self.nombre

# Modelo para guardar las ubicaciones en la base de datos.
class Ubicacion(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    
    def __str__(self):
        return f"Latitud: {self.lat}, Longitud: {self.lon}"