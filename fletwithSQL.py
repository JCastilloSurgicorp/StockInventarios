import flet as fl
import SI_Resources as re
from StockInventarioClass import StockInventario
from DetalleStockInventarioClass import DetalleStock

if __name__ == "__main__":
    def main(page: fl.Page):
        page.title = "App Stock Inventario"
        page.bgcolor = "#F5F5F5"
        page.theme_mode = fl.ThemeMode.LIGHT
        page.window_prevent_close = True
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
        page.dialog = confirm_dialog
        page.on_window_event = re.Functions(page).window_event

        SI = StockInventario(page)
        
        DS = DetalleStock(page)
        
        pages = {'/':fl.View("/",[SI]), '/detalle':fl.View("/detalle", [DS])}

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


    fl.app(target=main, assets_dir='./assets', port=8000)