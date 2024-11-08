from django.contrib import admin
from .models import *


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

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(HP_Proveedor)
admin.site.register(SI_Productos)
admin.site.register(SI_Grupo)
admin.site.register(SI_Linea)
admin.site.register(SI_Depositos)
admin.site.register(SI_TipoProductos)
admin.site.register(SI_Empresa)
admin.site.register(SI_TipoAlmacen)
admin.site.register(SI_Sector)
admin.site.register(StocksInventario)
admin.site.register(GuiasRemision)
admin.site.register(GR_Descripcion)
admin.site.register(GuiasRemision_OC)
admin.site.register(GR_Descripcion_OC)
admin.site.register(GR_Busqueda)
admin.site.register(Fact_Busqueda)
admin.site.register(Fact_Detalle)
admin.site.register(HojaPicking)
admin.site.register(Pend_Guias)
admin.site.register(Pend_Items)