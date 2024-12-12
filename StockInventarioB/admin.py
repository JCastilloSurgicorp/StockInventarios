from django.contrib.auth.models import Group, User
from django.contrib import admin
from .models import *


class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class GuiasRemisionAdmin(admin.ModelAdmin):
    list_display = ["nro_guia", "fecha_guia","atencion", "representante", "motivo", "estado", "id_app"]
    search_fields = ["nro_guia"]

class GuiasRemision_OC_Admin(admin.ModelAdmin):
    list_display = ["nro_guia", "fecha_guia","atencion", "representante", "motivo", "estado", "oc_cliente", "nro_proceso","id_app"]
    search_fields = ["nro_guia"]

class GR_DescripcionAdmin(admin.ModelAdmin):
    list_display = ["id", "nro_guia", "nro_item", "prod", "lote", "cantidad", "codigo_qr", "ubicacion_sector", "empr_id"]
    search_fields = ["nro_guia", "prod"]
    list_filter = ["codigo_qr"]

class GR_Descripcion_OC_Admin(admin.ModelAdmin):
    list_display = ["id", "nro_guia", "nro_item", "prod", "lote", "cantidad", "codigo_qr", "ubicacion_sector", "empr_id"]
    search_fields = ["nro_guia", "prod"]
    list_filter = ["codigo_qr"]

class GR_BusquedaAdmin(admin.ModelAdmin):
    list_display = ["id", "nro_guia", "fecha_guia", "oc_cliente", "fecha_cirugia", "zona", "id_app"]

class SI_LineaAdmin(admin.ModelAdmin):
    list_display = ["id", "linea"]

class SI_GrupoAdmin(admin.ModelAdmin):
    list_display = ["id", "grupo", "linea_id"]

class SI_DepositosAdmin(admin.ModelAdmin):
    list_display = ["id", "deposito", "descripcion_deposito", "empr_id"]

class SI_ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "producto", "descripcion_producto", "grupo", "proveedor_id"]

class StocksInventarioAdmin(admin.ModelAdmin):
    list_display = ["producto", "descr_prod", "lote", "fecha_vigencia_lote", "stock", "codigo_qr","tipoProd_id", "dep_id", "sector_id"]
    search_fields = ["producto", "descr_prod"]
    #list_filter = ["tipoProd_id", "tipoAlm_id"]

class Fact_BusquedaAdmin(admin.ModelAdmin):
    list_display = ["id", "nro_fact", "fecha_emision", "oc_cliente", "id_app"]

class Fact_DetalleAdmin(admin.ModelAdmin):
    list_display = ["nro_fact", "fecha_emision", "monto", "moneda", "nombre_cliente", "cond_pago", "cobrado", "saldo", "empresa"]

class HP_ProveedorAdmin(admin.ModelAdmin):
    list_display = ["id", "producto", "proveedor"]

@admin.action(description="Mark selected records as 'Picking Pendiente'")
def Pendiente(modeladmin, request, queryset):
    queryset.update(status_picking="Picking Pendiente")

@admin.action(description="Mark selected records as 'Picking En Proceso'")
def Proceso(modeladmin, request, queryset):
    queryset.update(status_picking="Picking En Proceso")

@admin.action(description="Mark selected records as 'Picking Terminado'")
def Terminado(modeladmin, request, queryset):
    queryset.update(status_picking="Picking Terminado")

class HojaPickingAdmin(admin.ModelAdmin):
    list_display = ["id", "nro_guia", "fecha_atencion","status_picking", "tipo_pedido", "ubicacion_sector", "sector", "empr_id"]
    actions = [Pendiente, Proceso, Terminado]

class Pend_GuiasAdmin(admin.ModelAdmin):
    list_display = ["nro_guia", "f_guia", "cant_pend","repr", "nombre_cliente", "zona", "tipo_venta", "empr", "id_app"]

class Pend_ItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "nro_guia", "item", "prod", "desc_prod", "cant_pend", "lote", "id_app"]


# Register your models here.
#admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(HP_Proveedor, HP_ProveedorAdmin)
admin.site.register(SI_Productos, SI_ProductoAdmin)
admin.site.register(SI_Grupo, SI_GrupoAdmin)
admin.site.register(SI_Linea, SI_LineaAdmin)
admin.site.register(SI_Depositos, SI_DepositosAdmin)
admin.site.register(SI_TipoProductos)
admin.site.register(SI_Empresa)
admin.site.register(SI_TipoAlmacen)
admin.site.register(SI_Sector)
admin.site.register(StocksInventario, StocksInventarioAdmin)
admin.site.register(GuiasRemision, GuiasRemisionAdmin)
admin.site.register(GR_Descripcion, GR_DescripcionAdmin)
admin.site.register(GuiasRemision_OC, GuiasRemision_OC_Admin)
admin.site.register(GR_Descripcion_OC, GR_Descripcion_OC_Admin)
admin.site.register(GR_Busqueda, GR_BusquedaAdmin)
admin.site.register(Fact_Busqueda, Fact_BusquedaAdmin)
admin.site.register(Fact_Detalle, Fact_DetalleAdmin)
admin.site.register(HojaPicking, HojaPickingAdmin)
admin.site.register(Pend_Guias, Pend_GuiasAdmin)
admin.site.register(Pend_Items, Pend_ItemsAdmin)