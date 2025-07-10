from office365.sharepoint.client_context import ClientContext
from django.conf import settings


def get_sharepoint_context():

    creds = {
        "tenant": settings.SHAREPOINT_CONFIG['tenant_id'],
        "client_id": settings.SHAREPOINT_CONFIG['client_id'],
        "thumbprint": settings.SHAREPOINT_CONFIG['thumbprint'],
        "cert_path": settings.SHAREPOINT_CONFIG['certificate_path'],
    }
    
    ctx = ClientContext(settings.SHAREPOINT_CONFIG['site_url']).with_client_certificate(**creds)
    return ctx

def get_sharepoint_lists():
    ctx = get_sharepoint_context()
    lists = ctx.web.lists
    ctx.load(lists)
    ctx.execute_query()
    return lists

def get_list_items(list_title):
    ctx = get_sharepoint_context()
    sp_list = ctx.web.lists.get_by_title(list_title)
    items = sp_list.get_items()
    ctx.load(items)
    ctx.execute_query()
    return items

def update_list_item(list_title, item_id, data):
    ctx = get_sharepoint_context()
    sp_list = ctx.web.lists.get_by_title(list_title)
    item = sp_list.get_item_by_id(item_id)
    
    for field, value in data.items():
        item.set_property(field, value)
    
    item.update()
    ctx.execute_query()
    return True