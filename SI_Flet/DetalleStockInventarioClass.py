import flet as fl
import SI_Resources as re

class DetalleStock(fl.Container):

    def __init__(self, page):
        super().__init__()
        
        self.expand = True
        
        self.page = page
        #self.page.window_prevent_close = True
        #self.page.on_window_event = re.Functions(self.page).window_event

        self.parse = re.Data()

        self.DS_Form = []

        self.DS_Body_Container = re.Containers(self.DS_Form).body

        self.DS_Header_Container = re.Containers(
            fl.ResponsiveRow(
                expand = True,
                controls = [
                    re.Icons(lambda _:self.page.go("/")).back_Icon,
                    re.Header_Title("Detalle Stock Inventario").title,
                    re.Header_Title("Bienvenido, <UserFullName>", lambda _:print("Bienvenida Clicked!")).bienvenida,
                    re.Icons(lambda _:print("Logo Clicked!")).logo_Icon
                ]
            ) 
        ).header

        self.DS_Screen_Container = fl.SafeArea(fl.Column([self.DS_Header_Container,self.DS_Body_Container]))
    
        self.content = self.DS_Screen_Container

        self.printData(self.page)


    def popView(self):
        self.page.go("/", True)
        print("into popView")

    def printData(self, e):
        self.DS_Form.clear()
        print(f"printData: {e.route}")
        self.DS_Form.append(
            fl.Column(
                spacing = 20,
                expand = True,
                scroll = fl.ScrollMode.AUTO,
                controls = [
                    fl.ResponsiveRow(
                        controls = [
                            re.Card("Código de Producto", self.parse.SelectedRecord['PRODUCTO']).dataCard,
                            re.Card("Descripción de Producto", self.parse.SelectedRecord['DESCRIPCION_PRODUCTO']).dataCard,
                            re.Card("Tipo de Producto", self.parse.SelectedRecord['TIPO_PRODUCTO']).dataCard
                        ]
                    ),
                    fl.ResponsiveRow(
                        controls = [
                            re.Card("Stock", self.parse.SelectedRecord['STOCK']).dataCard,
                            re.Card("Lote", self.parse.SelectedRecord['LOTE']).dataCard,
                            re.Card("Vigencia de Lote", self.parse.SelectedRecord['FECHA_VIGENCIA_LOTE']).dataCard,
                        ]
                    ),
                    fl.ResponsiveRow(
                        controls = [
                            re.Card("Línea", self.parse.SelectedRecord['LINEA']).dataCard,
                            re.Card("Grupo", self.parse.SelectedRecord['GRUPO']).dataCard,
                            re.Card("Empresa", self.parse.SelectedRecord['EMPRESA']).dataCard,
                        ]
                    ),
                    fl.ResponsiveRow(
                        controls = [
                            re.Card("Depósito", self.parse.SelectedRecord['DEPOSITO']).dataCard,
                            re.Card("Descripción de Almacén", self.parse.SelectedRecord['DESCRIPCION_DEPOSITO']).dataCard,
                            re.Card("Tipo de Almacén", self.parse.SelectedRecord['TIPO_ALMACEN']).dataCard
                        ]
                    ),
                    fl.ResponsiveRow(
                        controls = [
                            re.Card("Tipo de Almacenaje", self.parse.SelectedRecord['TIPO_ALMACENAJE']).dataCard,
                            re.Card("Resgistro Sanitario", self.parse.SelectedRecord['REGISTRO_SANITARIO']).dataCard,
                            re.Card("Fecha de Vigencia de Registro Sanitario", self.parse.SelectedRecord['FECHA_VIGENCIA_REGSAN']).dataCard
                        ]   
                    )
                ]
            )
        )
        self.page.update()
        print(f"printData: {self.parse.SelectedRecord['PRODUCTO']}")
