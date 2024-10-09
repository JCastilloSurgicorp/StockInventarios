import flet as fl
import SI_Resources as re
from fastapi import FastAPI
#import flet_fastapi_proxy_path as flet_fastapi
from StockInventarioClass import StockInventario
from DetalleStockInventarioClass import DetalleStock

appName = "App Stock Inventario"
app = FastAPI()

def main(page: fl.Page):
    page.title = appName
    page.bgcolor = "#F5F5F5"
    page.theme_mode = fl.ThemeMode.LIGHT
    page.window.prevent_close = True
    confirm_dialog = fl.AlertDialog(
        modal=True,
        title=fl.Text("Please confirm"),
        content=fl.Text("Do you really want to exit this app?"),
        actions=[
            fl.ElevatedButton("Yes", on_click=re.Functions(page).yes_click, bgcolor=fl.cupertino_colors.ACTIVE_GREEN),
            fl.OutlinedButton("No", on_click=re.Functions(page).no_click),
        ],
        actions_alignment=fl.MainAxisAlignment.END,
    )
    page.overlay.append(confirm_dialog)
    page.on_window_event = re.Functions(page).window_event

    SI = StockInventario(page)
    
    DS = DetalleStock(page)
    
    pages = {'/SI_Flet':fl.View("/SI_Flet",[SI]), '/detalle':fl.View("/detalle", [DS])}

    def route_change(e: fl.RouteChangeEvent):
        page.views.clear()
        page.views.append(pages[page.route])
        if page.route == '/detalle':
            DS.__init__(page)
        if page.route == '/':
            page.update()
            if re.Data.route != '/detalle':
                SI.load_data(e)
        
    def view_pop(view):
        page.views.pop()
        print(f"view: {view}")
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    #await page.add_async(SI)

if __name__ == "__main__":
    fl.app(target=main, assets_dir='./assets') #-> (FastAPI | None)
#app.mount("/", flet_fastapi.app(main, proxy_path=f'/{appName}'))