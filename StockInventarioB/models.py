from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class SI_Linea(models.Model):
    linea = models.CharField(db_column='LINEA', max_length=60, blank=True, null=True) 

    def __str__(self):
        return self.linea
    
    class Meta:
        managed = True
        db_table = 'SI_Linea'

class SI_Grupo(models.Model):
    linea_id = models.ForeignKey(SI_Linea, on_delete=models.DO_NOTHING)
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True) 

    def __str__(self):
        return self.grupo
    
    class Meta:
        managed = True
        db_table = 'SI_Grupo'

class SI_Productos(models.Model):
    producto = models.CharField(db_column='PRODUCTO', max_length=30)
    descripcion_producto = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)
    grupo_id = models.ForeignKey(SI_Grupo, on_delete=models.DO_NOTHING) 

    def __str__(self):
        return self.producto
    
    class Meta:
        managed = True
        db_table = 'SI_Productos'

class SI_TipoProductos(models.Model):
    tipo_producto = models.CharField(db_column='TIPO_PRODUCTO', max_length=6)

    def __str__(self):
        return self.tipo_producto
   
    class Meta:
        managed = True
        db_table = 'SI_TipoProductos'


class SI_Empresa(models.Model):
    empresa = models.CharField(db_column='EMPRESA', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.empresa
   
    class Meta:
        managed = True
        db_table = 'SI_Empresa'


class SI_Depositos(models.Model):
    empr_id = models.ForeignKey(SI_Empresa, on_delete=models.DO_NOTHING)
    deposito = models.CharField(db_column='DEPOSITO', max_length=15)  
    descripcion_deposito = models.CharField(db_column='DESCRIPCION_DEPOSITO', max_length=60, blank=True, null=True) 

    def __str__(self):
        return self.deposito
   
    class Meta:
        managed = True
        db_table = 'SI_Depositos'


class SI_TipoAlmacen(models.Model):
    tipo_almacen = models.CharField(db_column='TIPO_ALMACEN', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.tipo_almacen
   
    class Meta:
        managed = True
        db_table = 'SI_TipoAlmacen'


class SI_Sector(models.Model):
    sector = models.CharField(db_column='SECTOR', max_length=15)

    def __str__(self):
        return self.sector
   
    class Meta:
        managed = True
        db_table = 'SI_Sector'


class StocksInventario(models.Model):
    prod_id = models.ForeignKey(SI_Productos, on_delete=models.DO_NOTHING)
    tipoProd_id = models.ForeignKey(SI_TipoProductos, on_delete=models.DO_NOTHING)
    dep_id = models.ForeignKey(SI_Depositos, on_delete=models.DO_NOTHING)
    sector_id = models.ForeignKey(SI_Sector, on_delete=models.DO_NOTHING) 
    tipoAlm_id = models.ForeignKey(SI_TipoAlmacen, on_delete=models.DO_NOTHING)
    stock = models.DecimalField(db_column='STOCK', max_digits=18, decimal_places=2, blank=True, null=True)
    lote = models.CharField(db_column='LOTE', max_length=30)
    fecha_vigencia_lote = models.DateField(db_column='FECHA_VIGENCIA_LOTE', blank=True, null=True)
    tipo_almacenaje = models.CharField(db_column='TIPO_ALMACENAJE', max_length=50, blank=True, null=True)
    registro_sanitario = models.CharField(db_column='REGISTRO_SANITARIO', max_length=32, blank=True, null=True)
    fecha_vigencia_regsan = models.DateField(db_column='FECHA_VIGENCIA_REGSAN', blank=True, null=True)  

    def __str__(self):
        return self.lote
    
    class Meta:
        managed = True
        db_table = 'STOCKS_INVENTARIO'