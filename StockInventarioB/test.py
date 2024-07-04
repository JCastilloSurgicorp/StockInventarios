from django.db import models
import uuid

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text

    class Meta:
        managed = True
        db_table = 'StockInventarioB_question'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

    class Meta:
        managed = True
        db_table = 'StockInventarioB_choice'

class StocksPwrapp(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    empresa = models.CharField(db_column='EMPRESA', max_length=50, blank=True, null=True) 
    deposito = models.CharField(db_column='DEPOSITO', max_length=15)  
    descripcion_deposito = models.CharField(db_column='DESCRIPCION_DEPOSITO', max_length=60, blank=True, null=True)  
    sector = models.CharField(db_column='SECTOR', max_length=15)  
    tipo_producto = models.CharField(db_column='TIPO_PRODUCTO', max_length=6)
    producto = models.CharField(db_column='PRODUCTO', max_length=30) 
    descripcion_producto = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)  
    lote = models.CharField(db_column='LOTE', max_length=30) 
    fecha_vigencia_lote = models.DateField(db_column='FECHA_VIGENCIA_LOTE', blank=True, null=True) 
    stock = models.DecimalField(db_column='STOCK', max_digits=18, decimal_places=4, blank=True, null=True)
    tipo_almacen = models.CharField(db_column='TIPO_ALMACEN', max_length=20, blank=True, null=True)
    tipo_almacenaje = models.CharField(db_column='TIPO_ALMACENAJE', max_length=50, blank=True, null=True)  
    registro_sanitario = models.CharField(db_column='REGISTRO_SANITARIO', max_length=32, blank=True, null=True) 
    fecha_vigencia_regsan = models.DateField(db_column='FECHA_VIGENCIA_REGSAN', blank=True, null=True) 
    linea = models.CharField(db_column='LINEA', max_length=60, blank=True, null=True)  
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True)  

    def __str__(self):
        return self.producto
    
    class Meta:
        managed = True
        db_table = 'STOCKS_PWRAPP'
        unique_together = (('tipo_producto', 'producto', 'lote', 'deposito', 'sector'),)


class DocguiPwrapp(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=10)  # Field name made lowercase.
    numero_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50)  # Field name made lowercase.
    nro_item = models.IntegerField(db_column='NRO_ITEM')  # Field name made lowercase.
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha_guia = models.DateField(db_column='FECHA_GUIA', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    producto = models.CharField(db_column='PRODUCTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcion_producto = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(db_column='LOTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nro_proceso = models.CharField(db_column='NRO_PROCESO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    atencion = models.CharField(db_column='ATENCION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    representante = models.CharField(db_column='REPRESENTANTE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    motivo_traslado = models.CharField(db_column='MOTIVO_TRASLADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='OBSERVACION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='SECTOR', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vencimiento_lote = models.DateField(db_column='VENCIMIENTO_LOTE', blank=True, null=True)  # Field name made lowercase.
    usa_oc_cliente = models.CharField(db_column='USA_OC_CLIENTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)  # Field name made lowercase.
    direccion_entrega = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCGUI_PWRAPP'


class DocvenPwrapp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero_factura = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha_emision = models.DateField(db_column='FECHA_EMISION', blank=True, null=True)  # Field name made lowercase.
    moneda = models.CharField(db_column='MONEDA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='MONTO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipo_cliente = models.CharField(db_column='TIPO_CLIENTE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    condicion_pago = models.CharField(db_column='CONDICION_PAGO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cancelado = models.CharField(db_column='CANCELADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cobrado = models.DecimalField(db_column='COBRADO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='SALDO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nc_factura_canje = models.CharField(db_column='NC_FACTURA_CANJE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nc_anulacion = models.CharField(db_column='NC_ANULACION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    titulo_gratuito = models.CharField(db_column='TITULO_GRATUITO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion_entrega = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sede = models.CharField(db_column='SEDE', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCVEN_PWRAPP'


class DocVentas(models.Model):
    fcrmvh_codemp = models.CharField(db_column='FCRMVH_CODEMP', max_length=10)  # Field name made lowercase.
    fcrmvh_modfor = models.CharField(db_column='FCRMVH_MODFOR', max_length=2)  # Field name made lowercase.
    fcrmvh_codfor = models.CharField(db_column='FCRMVH_CODFOR', max_length=6)  # Field name made lowercase.
    fcrmvh_nrofor = models.IntegerField(db_column='FCRMVH_NROFOR')  # Field name made lowercase.
    fcrmvh_fchmov = models.DateTimeField(db_column='FCRMVH_FCHMOV')  # Field name made lowercase.
    fcrmvh_coflis = models.CharField(db_column='FCRMVH_COFLIS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fcrmvh_nrocta = models.CharField(db_column='FCRMVH_NROCTA', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_VENTAS'

