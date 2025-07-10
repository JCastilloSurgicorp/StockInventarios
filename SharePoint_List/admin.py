from django.contrib import admin
from .models import Auxiliares
from .service import get_sharepoint_lists, get_list_items, update_list_item
from django.shortcuts import render, redirect
from django.urls import path
from django import forms

class AuxiliaresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def get_queryset(self, request):
        # Obtener listas de SharePoint
        lists = get_sharepoint_lists()
        return [
            Auxiliares(
                Title=lst.properties['Title'],
                Id=lst.properties['Id']
            ) for lst in lists
        ]
    
    def list_items_view(self, request, list_id):
        items = get_list_items(list_id)
        context = {
            'items': items,
            'list_id': list_id,
            'opts': self.model._meta
        }
        return render(request, 'admin/sharepoint_list_items.html', context)
    
    def edit_item_view(self, request, list_id, item_id):
        items = get_list_items(list_id)
        item = next((i for i in items if i.properties['Id'] == int(item_id)), None)
        
        if request.method == 'POST':
            data = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
            update_list_item(list_id, item_id, data)
            return redirect(f'../../{list_id}/items/')
        
        class ItemForm(forms.Form):
            for field in item.properties.keys():
                if field not in ['Id', 'Attachments', 'GUID']:
                    locals()[field] = forms.CharField(
                        initial=item.properties.get(field, ''),
                        label=field
                    )
        
        form = ItemForm()
        context = {
            'form': form,
            'item': item,
            'list_id': list_id,
            'opts': self.model._meta
        }
        return render(request, 'admin/sharepoint_edit_item.html', context)
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<str:list_id>/items/', self.admin_site.admin_view(self.list_items_view)), 
            path('<str:list_id>/items/<str:item_id>/change/', self.admin_site.admin_view(self.edit_item_view)),
        ]
        return custom_urls + urls


admin.site.register(Auxiliares, AuxiliaresAdmin)
