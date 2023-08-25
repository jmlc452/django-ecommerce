from django.db import models

# Create your models here.

class categoria_producto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta : 
        verbose_name = "Category_Product"
        verbose_name_plural = "Categorys_Product"
        
    def __str__(self) -> str:
        return self.nombre

class producto(models.Model):
    nombre = models.CharField( max_length=50)
    descripcion = models.TextField(null=True)
    categoria = models.ForeignKey(categoria_producto, on_delete=models.CASCADE)
    imagen = models.ImageField( upload_to="tienda",blank=True,null=True)
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self) -> str:
        return self.nombre
    
    