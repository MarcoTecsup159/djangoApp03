from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

class Proveedor(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    pagina_web = models.URLField()

class Cliente(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefonos = models.ManyToManyField('Telefono')

class Telefono(models.Model):
    numero = models.IntegerField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

class Producto(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Venta(models.Model):
    numero_factura = models.IntegerField(unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    