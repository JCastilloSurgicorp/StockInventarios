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


class HP_Proveedor(models.Model):
    producto = models.CharField(db_column='PRODUCTO', max_length=30, blank=True, null=True)
    proveedor = models.CharField(db_column='PROVEEDOR', max_length=120, blank=True, null=True)
   
    def __str__(self):
        return self.proveedor
    
    class Meta:
        managed = True
        db_table = 'HP_PROVEEDOR'


class SI_Productos(models.Model):
    producto = models.CharField(db_column='PRODUCTO', max_length=30)
    descripcion_producto = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)
    proveedor_id = models.ForeignKey(HP_Proveedor, on_delete=models.DO_NOTHING, db_column='PROVEEDOR_ID', default=5502)
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True)

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
    empr_id = models.ForeignKey(SI_Empresa, on_delete=models.DO_NOTHING, default=4)
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
    producto = models.CharField(db_column='PRODUCTO', max_length=30, blank=True, null=True)
    descr_prod = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)
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
    descr_deposito = models.CharField(db_column='DESCRIPCION_DEPOSITO', max_length=60, blank=True, null=True)
    codigo_qr = models.CharField(db_column='CODIGO_QR', max_length=150, blank=True, null=True) 

    def __str__(self):
        return self.producto
    
    class Meta:
        managed = True
        db_table = 'STOCKS_INVENTARIO'


class SI_UpdateAudit(models.Model):
    producto = models.CharField(db_column='PRODUCTO', max_length=30, blank=True, null=True)
    tipo_producto = models.CharField(db_column='TIPO_PRODUCTO', max_length=6, blank=True, null=True)
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True)
    linea = models.CharField(db_column='LINEA', max_length=60, blank=True, null=True)
    lote = models.CharField(db_column='LOTE', max_length=30, blank=True, null=True)
    deposito = models.CharField(db_column='DEPOSITO', max_length=15, blank=True, null=True)
    sector = models.CharField(db_column='SECTOR', max_length=15, blank=True, null=True)
    estado_old = models.TextField(db_column='ESTADO_OLD', blank=True, null=True)
    estado_new = models.TextField(db_column='ESTADO_NEW', blank=True, null=True)
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)

    def __str__(self):
        return self.lote
    
    class Meta:
        managed = True
        db_table = 'SI_UPDATE_AUDIT'


class GuiasRemision(models.Model):
    empresa = models.ForeignKey(SI_Empresa, on_delete=models.DO_NOTHING, db_column='EMPRESA_ID')
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    atencion = models.CharField(db_column='ATENCION', max_length=15, blank=True, null=True)
    representante = models.CharField(db_column='REPRESENTANTE', max_length=60, blank=True, null=True)
    motivo = models.CharField(db_column='MOTIVO_TRASLADO', max_length=50, blank=True, null=True)
    cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)
    entrega = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True)
    fecha_guia = models.DateField(db_column='FECHA_GUIA', blank=True, null=True)
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    obs = models.CharField(db_column='OBSERVACION', max_length=500, blank=True, null=True)
    tipo_pedido = models.CharField(db_column='TIPO_PEDIDO', max_length=50, blank=True, null=True)
    paciente = models.CharField(db_column='PACIENTE', max_length=60, blank=True, null=True)
    fecha_cirugia = models.DateField(db_column='FECHA_CIRUGIA', blank=True, null=True)
    ruc_cliente = models.CharField(db_column='RUC_CLIENTE', max_length=20, blank=True, null=True)
    kits_guia = models.CharField(db_column='KITS_GUIA', max_length=200, blank=True, null=True)
    deposito = models.CharField(db_column='DEPOSITO', max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'GUIAS_REMISION'


class GR_Descripcion(models.Model):
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    prod = models.CharField(db_column='PRODUCTO', max_length=20, blank=True, null=True)
    descr_prod = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True) 
    proveedor = models.CharField(db_column='PROVEEDOR', max_length=150, blank=True, null=True)
    sector = models.CharField(db_column='SECTOR', max_length=15, blank=True, null=True)
    nro_item = models.IntegerField(db_column='NUMERO_ITEM', blank=True, null=True)
    cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=18, decimal_places=2, blank=True, null=True)
    lote = models.CharField(db_column='LOTE', max_length=30, blank=True, null=True)
    venc_lote = models.DateField(db_column='VENCIMIENTO_LOTE', blank=True, null=True)
    empr_id = models.IntegerField(db_column='EMPRESA_ID', blank=True, null=True)
    ubicacion_sector = models.CharField(db_column='UBICACION_SECTOR', max_length=120, blank=True, null=True)
    id_concat = models.BigIntegerField(db_column='ID_CONCAT', blank=True, null=True)
    kits_items = models.CharField(db_column='KITS_ITEM', max_length=120, blank=True, null=True)
    codigo_qr = models.CharField(db_column='CODIGO_QR', max_length=150, blank=True, null=True) 

    def __str__(self):
        return self.prod
    
    class Meta:
        managed = True
        db_table = 'GR_DESCRIPCION'


class GuiasRemision_OC(models.Model):
    empresa = models.ForeignKey(SI_Empresa, on_delete=models.DO_NOTHING, db_column='EMPRESA_ID')
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    atencion = models.CharField(db_column='ATENCION', max_length=15, blank=True, null=True)
    representante = models.CharField(db_column='REPRESENTANTE', max_length=60, blank=True, null=True)
    motivo = models.CharField(db_column='MOTIVO_TRASLADO', max_length=50, blank=True, null=True)
    cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)
    entrega = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True)
    fecha_guia = models.DateField(db_column='FECHA_GUIA', blank=True, null=True)
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    obs = models.CharField(db_column='OBSERVACION', max_length=500, blank=True, null=True)
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)
    nro_proceso = models.CharField(db_column='NRO_PROCESO', max_length=20, blank=True, null=True)
    tipo_pedido = models.CharField(db_column='TIPO_PEDIDO', max_length=50, blank=True, null=True)
    paciente = models.CharField(db_column='PACIENTE', max_length=60, blank=True, null=True)
    fecha_cirugia = models.DateField(db_column='FECHA_CIRUGIA', blank=True, null=True)
    ruc_cliente = models.CharField(db_column='RUC_CLIENTE', max_length=20, blank=True, null=True)
    kits_guia = models.CharField(db_column='KITS_GUIA', max_length=200, blank=True, null=True)
    deposito = models.CharField(db_column='DEPOSITO', max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'GUIAS_REMISION_OC'


class GR_Descripcion_OC(models.Model):
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    prod = models.CharField(db_column='PRODUCTO', max_length=20, blank=True, null=True)
    descr_prod = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)
    proveedor = models.CharField(db_column='PROVEEDOR', max_length=150, blank=True, null=True)
    sector = models.CharField(db_column='SECTOR', max_length=15, blank=True, null=True)
    nro_item = models.IntegerField(db_column='NUMERO_ITEM', blank=True, null=True)
    cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=18, decimal_places=2, blank=True, null=True)
    lote = models.CharField(db_column='LOTE', max_length=30, blank=True, null=True)
    venc_lote = models.DateField(db_column='VENCIMIENTO_LOTE', blank=True, null=True)
    empr_id = models.IntegerField(db_column='EMPRESA_ID', blank=True, null=True)
    ubicacion_sector = models.CharField(db_column='UBICACION_SECTOR', max_length=120, blank=True, null=True)
    id_concat = models.BigIntegerField(db_column='ID_CONCAT', blank=True, null=True)
    kits_items = models.CharField(db_column='KITS_ITEM', max_length=120, blank=True, null=True)
    codigo_qr = models.CharField(db_column='CODIGO_QR', max_length=150, blank=True, null=True) 
    
    def __str__(self):
        return self.prod
    
    class Meta:
        managed = True
        db_table = 'GR_DESCRIPCION_OC'


class GR_Busqueda(models.Model):
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    fecha_guia = models.DateField(db_column='FECHA_GUIA', blank=True, null=True)
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)
    fecha_cirugia = models.DateField(db_column='FECHA_CIRUGIA', blank=True, null=True)
    zona = models.CharField(db_column='ZONA', max_length=60, blank=True, null=True)
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'GR_BUSQUEDA'


#class GR_UpdateAudit(models.Model):
    #nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    #empresa = models.IntegerField(db_column='EMPRESA_ID', blank=True, null=True)
    #nro_item = models.IntegerField(db_column='NUMERO_ITEM', blank=True, null=True)
    #estado_old = models.TextField(db_column='ESTADO_OLD', blank=True, null=True)
    #estado_new = models.TextField(db_column='ESTADO_NEW', blank=True, null=True)
    #fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)

    #def __str__(self):
       # return self.nro_fact
    
    #class Meta:
        #managed = True
        #db_table = 'GR_UPDATE_AUDIT'


class Fact_Busqueda(models.Model):
    nro_fact = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    fecha_emision = models.DateField(db_column='FECHA_EMISION', blank=True, null=True)
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nro_fact
    
    class Meta:
        managed = True
        db_table = 'FACT_BUSQUEDA'


class Fact_Detalle(models.Model):
    id_fact = models.IntegerField(db_column='ID_FACT', blank=True, null=False)
    nro_fact = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True)
    fecha_emision = models.DateField(db_column='FECHA_EMISION', blank=True, null=True)
    monto = models.IntegerField(db_column='MONTO', blank=True, null=True)
    moneda = models.CharField(db_column='MONEDA', max_length=20, blank=True, null=True)
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)
    cond_pago = models.CharField(db_column='CONDICION_PAGO', max_length=60, blank=True, null=True)
    vendedor = models.CharField(db_column='VENDEDOR', max_length=60, blank=True, null=True)
    cancelado = models.CharField(db_column='CANCELADO', max_length=1, blank=True, null=True)
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)
    cobrado = models.DecimalField(db_column='COBRADO', max_digits=18, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(db_column='SALDO', max_digits=18, decimal_places=2, blank=True, null=True)
    nc_fact_canje = models.CharField(db_column='NC_FACTURA_CANJE', max_length=35, blank=True, null=True)
    nc_anulacion = models.CharField(db_column='NC_ANULACION', max_length=35, blank=True, null=True)
    tit_grat = models.CharField(db_column='TITULO_GRATUITO', max_length=1, blank=True, null=True)
    empresa = models.CharField(db_column='EMPRESA', max_length=150, blank=True, null=True)
    dir_entr = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True)
    sede = models.CharField(db_column='SEDE', max_length=60, blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)
    tipo_cliente = models.CharField(db_column='TIPO_CLIENTE', max_length=60, blank=True, null=True)
    usuario_registro = models.CharField(db_column='USUARIO_REGISTRO', max_length=60, blank=True, null=True)
    zona = models.CharField(db_column='ZONA', max_length=60, blank=True, null=True)
    afecto_detr = models.CharField(db_column='AFECTO_DETRACCION', max_length=1, blank=True, null=True)
    afecto_ret = models.CharField(db_column='AFECTO_RETENCION', max_length=1, blank=True, null=True)
    monto_soles = models.DecimalField(db_column='MONTO_SOLES', max_digits=18, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nro_fact
    
    class Meta:
        managed = True
        db_table = 'FACT_DETALLE'


class Fact_UpdateAudit(models.Model):
    id_fact = models.IntegerField(db_column='ID_FACT', blank=True, null=False)
    nro_fact = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True)
    estado_old = models.TextField(db_column='ESTADO_OLD', blank=True, null=True)
    estado_new = models.TextField(db_column='ESTADO_NEW', blank=True, null=True)
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)

    def __str__(self):
        return self.nro_fact
    
    class Meta:
        managed = True
        db_table = 'FACT_UPDATE_AUDIT'


class HojaPicking(models.Model):
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    gr_id = models.ForeignKey(GuiasRemision, on_delete=models.DO_NOTHING, db_column='GR_ID', null=True)
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True)
    nro_proceso = models.CharField(db_column='NRO_PROCESO', max_length=20, blank=True, null=True)
    gr_oc_id = models.ForeignKey(GuiasRemision_OC, on_delete=models.DO_NOTHING, db_column='GR_OC_ID', null=True)
    status_picking = models.CharField(db_column='STATUS_PICKING', max_length=60, blank=True, null=True)
    atencion = models.CharField(db_column='ATENCION', max_length=60, blank=True, null=True)
    firma_atencion = models.CharField(db_column='FIRMA_ATENCION', max_length=60, blank=True, null=True)
    fecha_atencion = models.DateTimeField(db_column='FECHA_ATENCION', blank=True, null=True)
    almacen = models.CharField(db_column='ALMACEN', max_length=60, blank=True, null=True)
    firma_almacen = models.CharField(db_column='FIRMA_ALMACEN', max_length=60, blank=True, null=True)
    fecha_almacen = models.DateTimeField(db_column='FECHA_ALMACEN', blank=True, null=True)
    distribucion = models.CharField(db_column='DISTRIBUCION', max_length=60, blank=True, null=True)
    firma_distribucion = models.CharField(db_column='FIRMA_DISTRIBUCION', max_length=60, blank=True, null=True)
    fecha_distribucion = models.DateTimeField(db_column='FECHA_DISTRIBUCION', blank=True, null=True)
    cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)
    tipo_venta = models.CharField(db_column='TIPO_VENTA', max_length=60, blank=True, null=True)
    tipo_pedido = models.CharField(db_column='TIPO_PEDIDO', max_length=50, blank=True, null=True)
    sector = models.CharField(db_column='SECTOR', max_length=15, blank=True, null=True)
    ubicacion_sector = models.CharField(db_column='UBICACION_SECTOR', max_length=120, blank=True, null=True)
    lima_provincia = models.IntegerField(db_column='LIMA_PROVINCIA', blank=True, null=True)
    empr_id = models.ForeignKey(SI_Empresa, db_column='EMPRESA_ID', on_delete=models.DO_NOTHING, blank=True, null=True) 
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'HOJA_PICKING'

class HP_UpdateAudit(models.Model):
    id_hp = models.IntegerField(db_column='ID_HP', blank=True, null=False)
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=20, blank=True, null=True)
    empr_id = models.ForeignKey(SI_Empresa, db_column='EMPRESA_ID', on_delete=models.DO_NOTHING, blank=True, null=True)
    estado_old = models.TextField(db_column='ESTADO_OLD', blank=True, null=True)
    estado_new = models.TextField(db_column='ESTADO_NEW', blank=True, null=True)
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)
    picking_time = models.TimeField(db_column='PICKING_TIME', blank=True, null=True)

    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'HP_UPDATE_AUDIT'

class Pend_Guias(models.Model):
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    repr = models.CharField(db_column='REPRESENTANTE', max_length=60, blank=True, null=True)
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True)
    zona = models.CharField(db_column='ZONA', max_length=60, blank=True, null=True)
    tipo_venta = models.CharField(db_column='TIPO_VENTA', max_length=60, blank=True, null=True)
    empr = models.CharField(db_column='EMPRESA', max_length=10, blank=True, null=True)
    f_guia = models.DateField(db_column='FECHA_GUIA', blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True) 
    cant_pend = models.IntegerField(db_column='CANT_PEND_TOTAL', blank=True, null=True)    
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'PEND_GUIAS'


class Pend_Items(models.Model):
    id_concat = models.CharField(db_column='ID_CONCAT', max_length=40, blank=True, null=True)
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    item = models.IntegerField(db_column='ITEM', blank=True, null=True)  
    prod = models.CharField(db_column='PRODUCTO', max_length=20, blank=True, null=True)
    desc_prod = models.CharField(db_column='DESCRIPCION_PRODUCTO', max_length=120, blank=True, null=True)
    cant_pend = models.IntegerField(db_column='CANTIDAD_PENDIENTE', blank=True, null=True) 
    lote = models.CharField(db_column='LOTE', max_length=30, blank=True, null=True)
    v_lote = models.DateField(db_column='VENCIMIENTO_LOTE', blank=True, null=True)
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True)
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'PEND_ITEMS'


class Pend_Update_Audit(models.Model):
    id_concat = models.CharField(db_column='ID_CONCAT', max_length=40, blank=True, null=True)
    nro_guia = models.CharField(db_column='NUMERO_GUIA', max_length=50, blank=True, null=True)
    item = models.IntegerField(db_column='ITEM', blank=True, null=True)
    accion = models.CharField(db_column='ACCION', max_length=20, blank=True, null=True)
    cant_pend_old = models.IntegerField(db_column='CANT_PEND_OLD', blank=True, null=True) 
    cant_pend_new = models.IntegerField(db_column='CANT_PEND_NEW', blank=True, null=True) 
    f_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)
    
    def __str__(self):
        return self.nro_guia
    
    class Meta:
        managed = True
        db_table = 'PEND_UPDATE_AUDIT'