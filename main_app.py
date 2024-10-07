import math
from datetime import datetime
import flet as fl
import pyodbc as pdb

def main(page: fl.Page):
    page.title = "App Stock Inventario"
    page.bgcolor = "#F5F5F5"
    page.theme_mode = fl.ThemeMode.LIGHT

    SI_DataTable = fl.DataTable(
        column_spacing=20,
        bgcolor="F1F4F9",
        columns=[
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1)),
            fl.DataColumn(fl.Container(height=1))
        ],
        rows=[]
    )


    def connectSQL(sqlQuery):
        init= datetime.now()
        cnxn = pdb.connect('DRIVER={SQL Server}; SERVER=SVRSURGI\\SVRBIOPRO; DATABASE=SURGICORP_POWERAPPS; UID=powerapps;PWD=*Surgi007; Trusted_connection=no')
        cursor = cnxn.cursor()
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        description = cursor.description
        cursor.close()
        cnxn.close()
        fin = datetime.now()
        print("Tiempo de Conexión con SQL:",fin - init)
        return result,description


    def fill_DataTable(result, description):
        init= datetime.now()
        columns = [column[0] for column in description]
        rows = [dict(zip(columns,row)) for row in result]
        SI_DataTable.rows.clear()
        for row in rows:
            SI_DataTable.rows.append(
                fl.DataRow(
                    cells=[
                        fl.DataCell(fl.Text(row['PRODUCTO'], color="#153EC2", width=100, size=14, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['DESCRIPCION_PRODUCTO'], color="#153EC2", width=340, size=14, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['TIPO_PRODUCTO'], color="#153EC2", width=120, size=14, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['DEPOSITO'], color="#153EC2", width=80, size=14, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['DESCRIPCION_DEPOSITO'], color="#153EC2", width=340, size=14, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['FECHA_VIGENCIA_LOTE'], color="#153EC2", width=140, size=14, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['STOCK'], color="#153EC2", width=120, size=14, text_align=fl.TextAlign.LEFT))
                    ]
                )
            )
        fin = datetime.now()
        print("Tiempo de LLenado de Tabla:",fin - init,"\n")


    def load_data(e):
        SI_ProgressRing_Container.visible = True
        SI_CodigoProducto_TextField.value = ""
        SI_Deposito_Dropdown.value = None
        SI_Deposito_Dropdown.key = None
        SI_TipoProducto_Dropdown.value = None
        SI_TipoProducto_Dropdown.key = None
        page.update()
        result, description = connectSQL('SELECT TOP 500 PRODUCTO,DESCRIPCION_PRODUCTO,TIPO_PRODUCTO,DEPOSITO,DESCRIPCION_DEPOSITO,FECHA_VIGENCIA_LOTE,STOCK FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP WHERE STOCK > 0;')
        fill_DataTable(result, description)
        SI_ProgressRing_Container.visible = False
        page.update()
        
        
    def Dropdown_Filter(e):
        SI_ProgressRing_Container.visible = True
        SI_CodigoProducto_TextField.value = ""
        page.update()

        if(SI_TipoProducto_Dropdown.value != None):
            tipo = f"WHERE TIPO_PRODUCTO = \'{SI_TipoProducto_Dropdown.value}\'"
            if(SI_Deposito_Dropdown.value != None):
                dep = f" AND DEPOSITO = \'{SI_Deposito_Dropdown.value}\'"
            else:
                dep = ""
        else:
            tipo = ""
            if(SI_Deposito_Dropdown.value != None):
                dep = f"WHERE DEPOSITO = \'{SI_Deposito_Dropdown.value}\'"
            else:
                dep = ""
        
        result, description = connectSQL(f'SELECT TOP 500 PRODUCTO,DESCRIPCION_PRODUCTO,TIPO_PRODUCTO,DEPOSITO,DESCRIPCION_DEPOSITO,FECHA_VIGENCIA_LOTE,STOCK FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP {tipo}{dep};')
        fill_DataTable(result, description)
        SI_ProgressRing_Container.visible = False
        page.update()


    def codigoProducto_Filter(e):
            SI_ProgressRing_Container.visible = True
            SI_Deposito_Dropdown.value = None
            SI_Deposito_Dropdown.key = None
            SI_TipoProducto_Dropdown.value = None
            SI_TipoProducto_Dropdown.key = None
            page.update()
            result, description = connectSQL(f'SELECT TOP 500 PRODUCTO,DESCRIPCION_PRODUCTO,TIPO_PRODUCTO,DEPOSITO,DESCRIPCION_DEPOSITO,FECHA_VIGENCIA_LOTE,STOCK FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP WHERE PRODUCTO=\'{SI_CodigoProducto_TextField.value}\';')
            fill_DataTable(result, description)
            SI_ProgressRing_Container.visible = False
            page.update()


    SI_Header_Container = fl.Container(
        bgcolor="white",
        width=1366,
        height=86,
        border_radius=8,
        shadow=fl.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=fl.colors.BLUE_GREY_300,
            offset=fl.Offset(0, 0),
            blur_style=fl.ShadowBlurStyle.INNER,
        ),
        content=fl.Row(controls=[
            fl.Icon(fl.icons.EXIT_TO_APP, size=86, rotate=math.pi,color="#153EC2"),
            fl.Container(
                width=800,
                height=86,
                alignment=fl.alignment.center,
                bgcolor="#153EC2",
                content=fl.Text("Almacenes", color="white", size=36,weight=fl.FontWeight.BOLD,font_family="Lato")),
            fl.Container(
                width=200,
                height=86,
                alignment=fl.alignment.center,
                content=fl.Text("Bienvenido, Jairo Castillo", size=26,font_family="Lato",text_align=fl.TextAlign.CENTER)),
            fl.Container(image_src=f"/images/LogoSurgi.png", width=260, height=86, ink=True, on_click=lambda e:load_data(e))
            ]
        )    
    )

    SI_GalleryHeader_Container = fl.Container(
        offset=fl.transform.Offset(0, -0.16),
        bgcolor="#153EC2",
        width=1366,
        height=66,
        content=fl.Row(opacity=1.0,spacing=20,alignment=fl.MainAxisAlignment.CENTER,controls=[
            fl.Text("Producto", width=100, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Descripción de Producto", width=340, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Tipo de Producto", width=120, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Depósito", width=80, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Detalle de Depósito", width=340, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Fecha de Vigencia de Lote", width=140, size=18, color="white", text_align=fl.TextAlign.CENTER),
            fl.Text("Stock", width=120, size=18, color="white", text_align=fl.TextAlign.CENTER)
            ]
        )
    )

    SI_TipoProducto_Dropdown = fl.Dropdown(
        width=400,
        height=50,
        label="Tipo de Producto",
        hint_text="Busqueda por Tipo de Producto",
        on_change=Dropdown_Filter,
        options=[
            fl.dropdown.Option("CIN"),
            fl.dropdown.Option("ME2"),
            fl.dropdown.Option("MER"),
            fl.dropdown.Option("SG-IM"),
            fl.dropdown.Option("SG-IM2")
        ]
    )

    SI_Deposito_Dropdown = fl.Dropdown(
        width=400,
        height=50,
        label="Depósito",
        hint_text="Busqueda por Deposito",
        on_change=Dropdown_Filter,
        options=[
            fl.dropdown.Option("SG-APR"),
            fl.dropdown.Option("SG-BAJ"),
            fl.dropdown.Option("SG-C02"),
            fl.dropdown.Option("SG-C04-VS"),
            fl.dropdown.Option("SG-C04-C"),
            fl.dropdown.Option("SG-C06-PR"),
            fl.dropdown.Option("SG-C06-VS"),
            fl.dropdown.Option("SG-C09"),
            fl.dropdown.Option("SG-C09-PR"),
            fl.dropdown.Option("SG-C10"),
            fl.dropdown.Option("SG-C10-PR"),
            fl.dropdown.Option("SG-C14-PR"),
            fl.dropdown.Option("SG-C14-PV"),
            fl.dropdown.Option("SG-C18-PR"),
            fl.dropdown.Option("SG-C19"),
            fl.dropdown.Option("SG-C19-C"),
            fl.dropdown.Option("SG-C21-C"),
            fl.dropdown.Option("SG-C21-PR"),
            fl.dropdown.Option("SG-C21-PV"),
            fl.dropdown.Option("SG-C21-VS"),
            fl.dropdown.Option("SG-C23"),
            fl.dropdown.Option("SG-C27-PR"),
            fl.dropdown.Option("SG-C37-PR"),
            fl.dropdown.Option("SG-C37-VS"),
            fl.dropdown.Option("SG-C41-C"),
            fl.dropdown.Option("SG-C41-PV"),
            fl.dropdown.Option("SG-C41-PR"),
            fl.dropdown.Option("SG-C41-VS"),
            fl.dropdown.Option("SG-C48-PR"),
            fl.dropdown.Option("SG-C56-PR"),
            fl.dropdown.Option("SG-C57-VS"),
            fl.dropdown.Option("SG-C58-VS"),
            fl.dropdown.Option("SG-C59-VS"),
            fl.dropdown.Option("SG-C66-C"),
            fl.dropdown.Option("SG-C66-PR"),
            fl.dropdown.Option("SG-C66-PV"),
            fl.dropdown.Option("SG-C67-PR"),
            fl.dropdown.Option("SG-C83-PR"),
            fl.dropdown.Option("SG-C83-VS"),
            fl.dropdown.Option("SG-C86-C"),
            fl.dropdown.Option("SG-C86-PR"),
            fl.dropdown.Option("SG-C86-PV"),
            fl.dropdown.Option("SG-C92"),
            fl.dropdown.Option("SG-C92-PR"),
            fl.dropdown.Option("SG-C97-VS"),
            fl.dropdown.Option("SG-C97-PR"),
            fl.dropdown.Option("SG-C97-PV"),
            fl.dropdown.Option("SG-C99-PR"),
            fl.dropdown.Option("SG-C99-VS"),
            fl.dropdown.Option("SG-C100-VS"),
            fl.dropdown.Option("SG-C100-PR"),
            fl.dropdown.Option("SG-C106-PR"),
            fl.dropdown.Option("SG-C115"),
            fl.dropdown.Option("SG-C115-C"),
            fl.dropdown.Option("SG-C115-PR"),
            fl.dropdown.Option("SG-C127-PR"),
            fl.dropdown.Option("SG-C127-VS"),
            fl.dropdown.Option("SG-C130-PR"),
            fl.dropdown.Option("SG-C141-PR"),
            fl.dropdown.Option("SG-C192-VS"),
            fl.dropdown.Option("SG-C196-C"),
            fl.dropdown.Option("SG-C196-PR"),
            fl.dropdown.Option("SG-C196-VS"),
            fl.dropdown.Option("SG-C233-PR"),
            fl.dropdown.Option("SG-C233-IJ"),
            fl.dropdown.Option("SG-C237-VS"),
            fl.dropdown.Option("SG-C265-PR"),
            fl.dropdown.Option("SG-C274-PR"),
            fl.dropdown.Option("SG-C280-VS"),
            fl.dropdown.Option("SG-C295-PR"),
            fl.dropdown.Option("SG-C295-PV"),
            fl.dropdown.Option("SG-C297-C"),
            fl.dropdown.Option("SG-C314-C"),
            fl.dropdown.Option("SG-C314-PR"),
            fl.dropdown.Option("SG-C315-PR"),
            fl.dropdown.Option("SG-C610-PR"),
            fl.dropdown.Option("SG-C614-PR"),
            fl.dropdown.Option("SG-C614-PV"),
            fl.dropdown.Option("SG-C738-VS"),
            fl.dropdown.Option("SG-C803-PR"),
            fl.dropdown.Option("SG-C824-PR"),
            fl.dropdown.Option("SG-C827-PR"),
            fl.dropdown.Option("SG-C827-PV"),
            fl.dropdown.Option("SG-C833-PR"),
            fl.dropdown.Option("SG-C836-PR"),
            fl.dropdown.Option("SG-C841-PR"),
            fl.dropdown.Option("SG-C859-PR"),
            fl.dropdown.Option("SG-C883-VS"),
            fl.dropdown.Option("SG-CIN"),
            fl.dropdown.Option("SG-CSA"),
            fl.dropdown.Option("SG-CSA2"),
            fl.dropdown.Option("SG-CUA"),
            fl.dropdown.Option("SG-DEV"),
            fl.dropdown.Option("SG-REC"),
            fl.dropdown.Option("SG-VAF"),
            fl.dropdown.Option("SG-2VAF"),
            fl.dropdown.Option("RR-CIN"),
            fl.dropdown.Option("RRM-APR"),
            fl.dropdown.Option("RRM-BAJ"),
            fl.dropdown.Option("RRM-CUA"),
            fl.dropdown.Option("RRM-CSA"),
            fl.dropdown.Option("RRM-C02-C"),
            fl.dropdown.Option("RRM-C04-C"),
            fl.dropdown.Option("RRM-C04-VS"),
            fl.dropdown.Option("RRM-C02-VS"),
            fl.dropdown.Option("RRM-C07-VS"),
            fl.dropdown.Option("RRM-C09-VS"),
            fl.dropdown.Option("RRM-C10-VS"),
            fl.dropdown.Option("RRM-C18-VS"),
            fl.dropdown.Option("RRM-C21-VS"),
            fl.dropdown.Option("RRM-C23-VS"),
            fl.dropdown.Option("RRM-C33-C"),
            fl.dropdown.Option("RRM-C41-VS"),
            fl.dropdown.Option("RRM-C48-VS"),
            fl.dropdown.Option("RRM-C59-VS"),
            fl.dropdown.Option("RRM-C66-VS"),
            fl.dropdown.Option("RRM-C84-VS"),
            fl.dropdown.Option("RRM-C97-VS"),
            fl.dropdown.Option("RRM-C99-VS"),
            fl.dropdown.Option("RRM-C106-VS"),
            fl.dropdown.Option("RRM-C115-C"),
            fl.dropdown.Option("RRM-C127-VS"),
            fl.dropdown.Option("RRM-C135-VS"),
            fl.dropdown.Option("RRM-C141-VS"),
            fl.dropdown.Option("RRM-C172-VS"),
            fl.dropdown.Option("RRM-C194-VS"),
            fl.dropdown.Option("RRM-C196-VS"),
            fl.dropdown.Option("RRM-C233-IJ"),
            fl.dropdown.Option("RRM-C304-VS"),
            fl.dropdown.Option("RRM-C350-VS"),
            fl.dropdown.Option("RRM-C612-VS"),
            fl.dropdown.Option("RRM-C751-VS"),
            fl.dropdown.Option("RRM-C824-VS"),
            fl.dropdown.Option("RRM-C827-VS"),
            fl.dropdown.Option("RRM-C842-VS"),
            fl.dropdown.Option("RRM-C883-VS"),
            fl.dropdown.Option("RRM-C902-VS"),
            fl.dropdown.Option("RRM-DEV"),
            fl.dropdown.Option("RRM-REC"),
        ])

    SI_CodigoProducto_TextField = fl.TextField(
        width=400,
        height=50,
        label="Código de Producto",
        on_submit=codigoProducto_Filter
    )

    SI_Search_Container = fl.Container(
        width=1366,
        height=60,
        content=fl.Row(alignment=fl.MainAxisAlignment.CENTER, controls=[SI_CodigoProducto_TextField,SI_TipoProducto_Dropdown,SI_Deposito_Dropdown])
    )

    SI_ProgressRing_Container = fl.Container(
        width=1366,
        height=500,
        padding=fl.padding.only(left=652,right=652,top=230,bottom=230),
        bgcolor="white",
        opacity=0.8,
        content=fl.ProgressRing(color="#153EC2",stroke_width=4)
    )

    SI_Gallery = fl.Container(
        width=1366,
        height=500,
        content=fl.Column(width=1366, height=500, scroll="Auto", controls=[SI_DataTable]))

    SI_Gallery_Container = fl.Stack(
        width=1366,
        height=500,
        controls=[SI_Gallery,SI_GalleryHeader_Container,SI_ProgressRing_Container]
    )

    SI_Body_Container = fl.Container(
        bgcolor="white",
        width=1366,
        height=560,
        border_radius=8,
        shadow=fl.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=fl.colors.BLUE_GREY_300,
            offset=fl.Offset(0, 0),
            blur_style=fl.ShadowBlurStyle.INNER,
        ),
        content=fl.Column(width=1366, height=560, controls=[SI_Search_Container,SI_Gallery_Container])
    )
    page.add(fl.SafeArea(fl.Column([SI_Header_Container,SI_Body_Container])))


fl.app(target=main, assets_dir="assets")