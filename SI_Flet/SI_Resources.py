import math
import flet as fl
import pyodbc as pdb
from datetime import datetime

class Header_Title:
    def __init__(self, txt, event=[]):
        self.title = fl.Container(
            col = 7,
            expand = True,
            bgcolor = Colors().blueIntense,
            alignment = fl.alignment.center,
            content = fl.Text(
                size = 36,
                value = txt,
                color = "white",
                font_family = "Lato",
                weight = fl.FontWeight.BOLD,
            )
        )
        self.bienvenida = fl.Container(
            col = 2,
            ink = True,
            expand = True,
            on_click= event,
            alignment = fl.alignment.center,
            content = fl.Text(
                size = 26,
                value = txt,
                font_family = "Lato",
                text_align = fl.TextAlign.CENTER
            )
        )

class Icons:
    def __init__(self, e) -> None:
        self.back_Icon = fl.IconButton(
            col = 1,
            scale = 4,
            height = 86,
            on_click = e,
            rotate = math.pi, 
            icon_color = Colors().blueIntense, 
            icon = fl.icons.PLAY_ARROW_ROUNDED
        )
        self.logo_Icon = fl.Container(
            col = 2,
            ink = True,
            on_click = e,
            expand = True,
            content = fl.Image(src = f"/images/LogoSurgi.png", scale = 2)
        )
        self.exit_Icon = fl.IconButton(
            col = 1,
            scale = 4,
            height = 86,
            on_click = e,
            data = "close", 
            rotate = math.pi, 
            icon = fl.icons.EXIT_TO_APP,
            icon_color = Colors().blueIntense,    
        )

class Containers:
    def __init__(self, cont):
        self.header = fl.Container(  
            height = 86,
            content = cont,
            bgcolor = "white",
            border_radius = 8,  
            shadow = Shadow().main
        )
        self.body = fl.Container(
            expand = True,
            border_radius = 8,
            bgcolor = Colors().skyBG,
            shadow = Shadow().main,
            content = fl.Column(
                spacing = 0,
                expand = True, 
                controls = cont,
            )
        )

class Shadow:
    def __init__(self):
        self.main = fl.BoxShadow(
            blur_radius=15,
            spread_radius=1,
            offset=fl.Offset(0, 0),
            color=fl.colors.BLUE_GREY_300,
            blur_style=fl.ShadowBlurStyle.INNER,
        )

class Colors:
    def __init__(self) -> None:
        self.skyBG = "#F1F4F9"
        self.blackCard = "#666666"
        self.blueIntense = "#153EC2"
        
class Card:
    def __init__(self, key, value) -> None:
        self.dataCard = fl.Container(
            col = 4,
            height = 100,
            margin = fl.margin.only(left=20,top=0,right=20,bottom=0),
            padding = fl.padding.only(left=20, top=10, bottom=10, right=20),
            content = fl.Column(
                controls = (
                    fl.Text(
                        size = 18,
                        expand = 1,
                        value = key,
                        weight = fl.FontWeight.BOLD,
                        color = Colors().blueIntense,
                        text_align= fl.TextAlign.LEFT
                    ),
                    fl.Container(
                        col = 12,
                        expand = 2,
                        bgcolor = "white",
                        alignment= fl.alignment.center_left,
                        content =  fl.Text(
                            size = 18,
                            value = value,
                            no_wrap = False,
                            color = Colors().blackCard,
                            text_align = fl.TextAlign.LEFT,
                            overflow = fl.TextOverflow.VISIBLE
                        )
                    )
                )
            )
        )

class Filter:
    def __init__(self, resp, label, event, data='', cont=[]):
        self.dropdown = fl.Dropdown(
            col = resp,
            height = 50,
            label = label,
            text_size=14,
            padding=fl.padding.all(0.1),
            hint_text = f"Busqueda por {label}",
            on_change = event,
            options = []
        )
        self.txtField = fl.TextField(
            col = resp,
            data = data,
            height = 50,
            label = label,
            on_submit = event
        )
        self.fill_cont(cont)

    def fill_cont(self, cont):
        for opt in cont:
            self.dropdown.options.append(fl.dropdown.Option(opt))

class Data:
    SelectedRecord = {'EMPRESA': '', 'DEPOSITO': '', 'DESCRIPCION_DEPOSITO': '', 'SECTOR': '', 'TIPO_PRODUCTO': '', 'PRODUCTO': '', 'DESCRIPCION_PRODUCTO': '', 'LOTE': '', 'FECHA_VIGENCIA_LOTE': '', 'STOCK': 0, 'TIPO_ALMACEN': '', 'TIPO_ALMACENAJE': '', 'REGISTRO_SANITARIO': '', 'FECHA_VIGENCIA_REGSAN': '', 'LINEA': '', 'GRUPO': ''}
    route = ""

class Functions:
    def __init__(self, page) -> None:
        self.page = page

    def parse_Data(self, e, route):
        if e is not None:
            Data.SelectedRecord = e.control.data
            print(Data.SelectedRecord['DESCRIPCION_PRODUCTO'])
            print(Data.SelectedRecord['STOCK'])
        Data.route = route
        print(f"Data.route: {Data.route}")
        if route == "/detalle":
            self.page.go(route)

    def window_event(self, e):
        if e.data == "close":
            self.page.dialog.open = True
            self.page.update()

    def yes_click(self, e):
            print("Closing Connection..")
            print(f"yesClick: action={e.control.text}")
            self.page.window_destroy()
            
    def no_click(self, e):
        self.page.dialog.open = False
        print(f"noClick: action={e.control.text}")
        self.page.update()