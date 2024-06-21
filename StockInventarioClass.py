import SI_Resources as re
from datetime import datetime
import pandas as pd
import flet as fl
import pyodbc as pdb

class StockInventario(fl.Container):
    def __init__(self, page):
        super().__init__()
   
        self.expand = True
        self.cursor,self.cnxn = None, None
        self.result, self.description = None, None

        self.page = page
        self.file_picker = fl.FilePicker(on_result=self.ExcelDownload)
        self.page.overlay.append(self.file_picker)

        self.SI_DataTable = fl.DataTable(
            col = 16,
            rows = [],
            column_spacing = 20,
            heading_row_height = 66,
            bgcolor = re.Colors().skyBG,
            vertical_lines=fl.BorderSide(0.2, "blue"),
            data_row_color = {fl.MaterialState.HOVERED: "0x30FF0000"},
            heading_row_color = {fl.MaterialState.DEFAULT: re.Colors().blueIntense},
            columns = [
                fl.DataColumn(fl.Text("Producto", color="white", col=1,size=14, text_align=fl.TextAlign.LEFT)),
                fl.DataColumn(fl.Text("Descripción de Producto", color="white", col=3, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Tipo de \nProducto", color="white", col=2, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Depósito", color="white", col=1, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Detalle de Depósito", color="white", col=2, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Tipo de \nAlmacen", color="white", col=2, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Línea", color="white", col=1, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Grupo", color="white", col=1, size=14, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Fecha de \nVigencia \nde Lote",color="white", col=2, size=12, text_align=fl.TextAlign.CENTER)),
                fl.DataColumn(fl.Text("Stock", color="white", col=1, size=14, text_align=fl.TextAlign.CENTER))
            ]
        )

        self.SI_ProgressRing_Container = fl.Container(
            opacity = 0.8,
            col=12,
            expand=True,
            margin = fl.margin.only(top=166),
            visible = False,
            bgcolor = "white",
            alignment=fl.alignment.center,
            content = fl.Column(
                width=40,
                height=40,
                controls = [fl.ProgressRing(
                    color="#153EC2", 
                    stroke_width=4,
                    width=40,
                    height=40
                )]
            )
        )

        self.page.overlay.append(self.SI_ProgressRing_Container)

        self.SI_Gallery = fl.Container(
            expand = True,
            content = fl.Column(
                expand = True, 
                scroll="Auto", 
                controls=[fl.ResponsiveRow([self.SI_DataTable], columns=13)]))

        self.SI_ToExcel_Icon = fl.Container(
            col = 1,
            height = 50,
            content = fl.IconButton(
                scale = 2,
                tooltip = "Descargar Reporte en Excel",
                icon = fl.icons.SAVE_ALT,
                icon_color = "#153EC2",
                on_click = lambda _: self.file_picker.save_file(
                    file_name = datetime.now().strftime("DATA %Y-%m-%d_%H-%M-%S") + ".xlsx",
                    allowed_extensions = ["xlsx"]
                )
            ),
            
        )

        self.SI_Grupo_Dropdown = re.Filter(
            resp = 3,
            label = "Grupo",
            event = self.Dropdown_Filter,
            cont = ["APOSITO","ACCESORIO ARCO C","ACCESORIO BOJIN","ACCESORIO MICROSCOPIO","ACIDO HIALURONICO","ACIFBOX","AGUJA DE VERTEBROPLASTIA","AGUJAS","ANCILLARY INLAY","ANCORIS","ALHYDRAN","ARGUS","BAPSCARCARE","BATERIA","BATERIA BOJIN","BIPOLAR FORCEPS","BOMBA GENADYNE","BOMBA LIFOTRONIC","BROCAS BOJIN","BULBO","CABEZA FEMORAL","CABLE CERCLAJE","CADERA","CARBOJET","CEMENTO","CERVICAL","CHALECO","CHIPS","CLAVO INTRAMEDULAR","CLAVO KIRCHNNER","CODMAN","CODMAN CERTAS","CODO","COFLEX","COLLARIN","COLUMNA","CONDILO","COSMAN","CRW","CRANEOTOMO","CUCHILLA BOJIN","CUSA","CUSA CLARITY","DCI","DEMO TORNIER","DERMATOMO","DERMOCARRIER","DESBRIDADOR","DOLPHIX","DREN","DT FEMUR","DT FEMUR / ENDOVIS","DT FEMUR / ENDOVIS / RONDO","DT HUMERO","DT TIBIA","DURAGEN","EBA ONE","EBA ONE INSTRUMENTAL","ENDOVIS","ENGRAMPADOR","EQUIPO BTI","ESPACIADOR DE CADERA","ESPACIADOR DE HOMBRO","ESPACIADOR DE RODILLA","EXIA","EXUFIBER","FAJA","FIBULA","FLEX","FUNDA","GAP","GEL","GLASSBONE","GONADA","GRANUDACYN","GRANULOX","GUANTES","HALL MICRO FREE","HEMOSTATICO","HEMOSUC","HLS NOETOS","HOMBRO","ILLIUM","IMPLANTE COCHLEAR","IMPLANTE SFS","IMPLANTES FIREBIRD","IMPLANTS FRACTURE REVERSE","INLAY REVERSE","INSTANT COLD","INSTRUMENTAL BOJIN","INSTRUMENTAL CITIEFFE","INSTRUMENTAL DREMEL","INSTRUMENTAL MEGASYSTEM-C","INSTRUMENTAL MONT BLANC","INSTRUMENTAL MONT BLANC MIS","INSTRUMENTAL SFS","INSTRUMENTAL SPINEWAY","INSTRUMENTAL VALVAS","INSTRUMENTAL WALDERMARM LINK","IOBAN","LENTE","LUMBAR","MAIOREGEN","MANDIL","MAQUETAS PEGA MEDICAL","MASTISOL","MAYFIELD","MEEK","MEGASYSTEM-C","MEMBRACEL","MENISCOS","MEPILEX","MEPITEL","MIDAS REX","MIDFOOT RECONSTRUCTION","MOBI C","MONT BLANC","MONT BLANC BABY","MONT BLANC MIS","NAVIENT","NAZCA","NEUROESTIMULADOR CEREBRAL DBS","NEUROPRO TORNILLOS","OJEMAN","OPHIRA","OPTIUM DBM PUTTY","ORTHOLOC ANKLE FUSION","PEDIGUARD","PERCUDYN","PERSEUS","PIEL - BICAPA (5 X 5)","PIEL - MONOCAPA (5 X 5)","PIEL - MONOCAPA (10 X 12.5)","PIEL - MONOCAPA (20 X 25)","PIEL - BICAPA (10 X 12.5)","PIEL - BICAPA (20 X 25)","PIEL HUMANA","PIEL LIQUIDA","PIEL PORCINA","PIEL SINTETICA","PINZA","PISTOLA BOJIN","PLACA EN 8","PLACAS TROCANTRICAS","PLEXUR","POSTERIOR TIBIAL TENDON","PRGF","PRODUCTOS COVID","PROTESIS PENEANA","PROTESIS TESTICULAR","PUTTY","RETRACTORES QUIRUGICOS","REVERSA DE HOMBRO","RODILLA","RONDO","SAFYRE","SELLADOR","SET ISAGRAFT","SISTEMA DE PRESION NEGATIVA","SPINCARE","SPLENTIS","STAR - 90","SUTURA","TENDON AQUILES","TOBILLO","TORNIQUETE","UNITAPE","VALOR NAIL","VANTRIS","VARIOS NEURO.","VARIOS EQ. MED.","VISUALIZADOR DE VENAS","Consumo Interno","Bienes de Uso - Instrumental Medico","OTROS"]
        ).dropdown
        
        self.SI_Linea_Dropdown = re.Filter(
            resp = 3,
            label = "Linea",
            event = self.Dropdown_Filter,
            cont = ["CIRUGÍA GENERAL","NEUROCIRUGÍA","QUEMADOS Y PLÁSTICA","EQUIPOS MÉDICOS","PRODUCTOS COVID","ORTOPEDIA","UROLOGÍA & GINECOLOG","REGENERATION","OSTEOBIOLÓGICOS","Bienes de Uso - Instrumental Medico","Consumo Interno","OTROS"]
        ).dropdown

        self.SI_TipoAlmacen_Dropdown = re.Filter(
            resp = 3,
            label = "Tipo de Almacén",
            event = self.Dropdown_Filter,
            cont = ["PRINCIPAL", "ANEXO"]
        ).dropdown

        self.SI_TipoProducto_Dropdown = re.Filter(
            resp = 3,
            label = "Tipo de Producto",
            event = self.Dropdown_Filter,
            cont = ["CIN","ME2","MER","SG-IM","SG-IM2"]
        ).dropdown

        self.SI_Deposito_Dropdown = re.Filter(
            resp = 3,
            label = "Depósito",
            event = self.Dropdown_Filter,
            cont = ["SG-BAJ","SG-APR","SG-C02","SG-C04-VS","SG-C04-C","SG-C06-PR","SG-C06-VS","SG-C09","SG-C09-PR","SG-C10","SG-C10-PR","SG-C14-PR","SG-C14-PV","SG-C18-PR","SG-C19","SG-C19-C","SG-C21-C","SG-C21-PR","SG-C21-PV","SG-C21-VS","SG-C23","SG-C27-PR","SG-C37-PR","SG-C37-VS","SG-C41-C","SG-C41-PV","SG-C41-PR","SG-C41-VS","SG-C48-PR","SG-C56-PR","SG-C57-VS","SG-C58-VS","SG-C59-VS","SG-C66-C","SG-C66-PR","SG-C66-PV","SG-C67-PR","SG-C83-PR","SG-C83-VS","SG-C86-C","SG-C86-PR","SG-C86-PV","SG-C92","SG-C92-PR","SG-C97-VS","SG-C97-PR","SG-C97-PV","SG-C99-PR","SG-C99-VS","SG-C100-VS","SG-C100-PR","SG-C106-PR","SG-C115","SG-C115-C","SG-C115-PR","SG-C127-PR","SG-C127-VS","SG-C130-PR","SG-C141-PR","SG-C192-VS","SG-C196-C","SG-C196-PR","SG-C196-VS","SG-C233-PR","SG-C233-IJ","SG-C237-VS","SG-C265-PR","SG-C274-PR","SG-C280-VS","SG-C295-PR","SG-C295-PV","SG-C297-C","SG-C314-C","SG-C314-PR","SG-C315-PR","SG-C610-PR","SG-C614-PR","SG-C614-PV","SG-C738-VS","SG-C803-PR","SG-C824-PR","SG-C827-PR","SG-C827-PV","SG-C833-PR","SG-C836-PR","SG-C841-PR","SG-C859-PR","SG-C883-VS","SG-CIN","SG-CSA","SG-CSA2","SG-CUA","SG-DEV","SG-REC","SG-VAF","SG-2VAF","RR-CIN","RRM-APR","RRM-BAJ","RRM-CUA","RRM-CSA","RRM-C02-C","RRM-C04-C","RRM-C04-VS","RRM-C02-VS","RRM-C07-VS","RRM-C09-VS","RRM-C10-VS","RRM-C18-VS","RRM-C21-VS","RRM-C23-VS","RRM-C33-C","RRM-C41-VS","RRM-C48-VS","RRM-C59-VS","RRM-C66-VS","RRM-C84-VS","RRM-C97-VS","RRM-C99-VS","RRM-C106-VS","RRM-C115-C","RRM-C127-VS","RRM-C135-VS","RRM-C141-VS","RRM-C172-VS","RRM-C194-VS","RRM-C196-VS","RRM-C233-IJ","RRM-C304-VS","RRM-C350-VS","RRM-C612-VS","RRM-C751-VS","RRM-C824-VS","RRM-C827-VS","RRM-C842-VS","RRM-C883-VS","RRM-C902-VS","RRM-DEV","RRM-REC"]
        ).dropdown

        self.SI_CodigoProducto_TextField = re.Filter(
            resp = 3,
            data = 'PRODUCTO',
            label = "Código de Producto",
            event = self.codigoProducto_Filter
        ).txtField

        self.SI_DescripcionProducto_TextField = re.Filter(
            resp = 3,
            data = 'DESCRIPCION_PRODUCTO',
            label = "Descripcion de Producto",
            event = self.codigoProducto_Filter
        ).txtField

        self.SI_Filter_Container = fl.Container(
            height = 60,
            content = fl.ResponsiveRow(
                columns = 22,
                expand = True,
                alignment = fl.MainAxisAlignment.CENTER,
                vertical_alignment = fl.CrossAxisAlignment.CENTER,
                controls = [
                    self.SI_CodigoProducto_TextField,
                    self.SI_DescripcionProducto_TextField,
                    self.SI_TipoProducto_Dropdown,
                    self.SI_Deposito_Dropdown, 
                    self.SI_TipoAlmacen_Dropdown, 
                    self.SI_Linea_Dropdown, 
                    self.SI_Grupo_Dropdown,
                    self.SI_ToExcel_Icon
                ]
            )
        )

        self.SI_Body_Container = re.Containers([
            self.SI_Filter_Container,
            self.SI_Gallery  
        ]).body

        self.SI_Header_Container = re.Containers(
            fl.ResponsiveRow(
                expand = True,
                controls = [
                    re.Icons(lambda e:re.Functions(self.page).window_event(e.control)).exit_Icon,
                    re.Header_Title("Stock Inventario").title,
                    re.Header_Title("Bienvenido, <UserFullName>", self.clearFilters).bienvenida,
                    re.Icons(lambda _:self.load_data(None)).logo_Icon,
                ]
            ) 
        ).header

        self.SI_Screen_Container = fl.SafeArea(fl.Column([self.SI_Header_Container,self.SI_Body_Container]))

        self.content = self.SI_Screen_Container  


    def ExcelDownload(self, e: fl.FilePickerResultEvent):
        fileName = e.path
        if fileName is not None:
            fileName.replace("\\","/")
            columns = [column[0] for column in self.description]
            rows = [dict(zip(columns,row)) for row in self.result]
            prod, descProd, tipProd, dep, detDep, tipAlm, linea, grupo, fecha, stock = [],[],[],[],[],[],[],[],[],[]
            for row in rows:
                prod.append(row['PRODUCTO'])
                descProd.append(row['DESCRIPCION_PRODUCTO'])
                tipProd.append(row['TIPO_PRODUCTO'])
                dep.append(row['DEPOSITO'])
                detDep.append(row['DESCRIPCION_DEPOSITO'])
                tipAlm.append(row['TIPO_ALMACEN'])
                linea.append(row['LINEA'])
                grupo.append(row['GRUPO'])
                fecha.append(row['FECHA_VIGENCIA_LOTE'])
                stock.append(row['STOCK'])
            
            dataFrame = pd.DataFrame({
                "Producto":prod,
                "Descripción de Producto":descProd,
                "Tipo de Producto":tipProd,
                "Deposito":dep,
                "Detalle de Depósito":detDep,
                "Tipo de Almacen":tipAlm,
                "Línea":linea,
                "Grupo":grupo,
                "Fecha de Vigencia de Lote":fecha,
                "Stock":stock
            })
            dataFrame.to_excel(fileName)

    def connectSQL(self, sqlQuery):
        if self.cursor is not None:
            print("Closing Cursor..")
            try:
                self.cursor.close()
            except:
                print("Cursor Closed")
        init = datetime.now()
        #driver, trust = '{ODBC Driver 18 for SQL Server}', '; TrustServerCertificate=yes'
        driver = '{SQL Server}'
        self.cnxn = pdb.connect(f'DRIVER={driver}; SERVER=SVRSURGI\\SVRBIOPRO; DATABASE=SURGICORP_POWERAPPS; UID=powerapps;PWD=*Surgi007; Trusted_connection=no')
        self.cursor = self.cnxn.cursor()
        self.cursor.execute(sqlQuery)
        result = self.cursor.fetchall()
        description = self.cursor.description
        self.cursor.close()
        self.cursor = None
        fin = datetime.now()
        print("Tiempo de Conexión con SQL:",fin - init)
        return result,description

    def fill_DataTable(self, result, description):
        init= datetime.now()
        self.SI_DataTable.rows.clear()
        self.append_DataTable(result, description)
        fin = datetime.now()
        print("Tiempo de LLenado de Tabla:",fin - init,"\n")

    def append_DataTable(self, result, description):
        columns = [column[0] for column in description]
        rows = [dict(zip(columns, row)) for row in result]
        for row in rows:
            self.SI_DataTable.rows.append(
                fl.DataRow(
                    data=row,
                    selected=False,
                    color={fl.MaterialState.HOVERED: "0x30FF0000"},
                    on_select_changed=lambda e: re.Functions(self.page).parse_Data(e, "/detalle"),
                    cells=[
                        fl.DataCell(fl.Text(row['PRODUCTO'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['DESCRIPCION_PRODUCTO'], color="#153EC2", col=2, size=12, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['TIPO_PRODUCTO'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['DEPOSITO'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['DESCRIPCION_DEPOSITO'], color="#153EC2", col=3, size=12, text_align=fl.TextAlign.CENTER)),
                        fl.DataCell(fl.Text(row['TIPO_ALMACEN'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['LINEA'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['GRUPO'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(row['FECHA_VIGENCIA_LOTE'], color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT)),
                        fl.DataCell(fl.Text(int(row['STOCK']), color="#153EC2", col=1, size=12, text_align=fl.TextAlign.LEFT))
                    ]
                )
            )

    def load_data(self, e):
        self.SI_ProgressRing_Container.visible = True
        self.SI_CodigoProducto_TextField.value = ""
        self.SI_DescripcionProducto_TextField.value = ""
        self.clearDropdowns()
        if e is not None:
            print(f"loadData: {e.control.route}")
        self.page.update()
        self.result, self.description = self.connectSQL('SELECT TOP 500 * FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP WHERE STOCK!=0 ORDER BY STOCK DESC;')
        self.fill_DataTable(self.result, self.description)
        self.SI_ProgressRing_Container.visible = False
        self.page.update()

    def Dropdown_Filter(self, e):
        self.SI_ProgressRing_Container.visible = True
        self.SI_CodigoProducto_TextField.value = ""
        print(f"DropdownFilter: {e.control.label}={e.control.value}")
        self.page.update()
        tipo, dep, tipoalm, linea, grupo = "","","","",""
        if(self.SI_TipoProducto_Dropdown.value != None and self.SI_TipoProducto_Dropdown.value != ""):
            tipo = f" AND TIPO_PRODUCTO = \'{self.SI_TipoProducto_Dropdown.value}\'"
        else:
            tipo = ""
        if(self.SI_Deposito_Dropdown.value != None and self.SI_Deposito_Dropdown.value != ""):
            dep = f" AND DEPOSITO = \'{self.SI_Deposito_Dropdown.value}\'"
        else:
            dep = ""
        if(self.SI_TipoAlmacen_Dropdown.value != None and self.SI_TipoAlmacen_Dropdown.value != ""):
            tipoalm = f" AND TIPO_ALMACEN = \'{self.SI_TipoAlmacen_Dropdown.value}\'"
        else:
            tipoalm = ""
        if(self.SI_Linea_Dropdown.value != None and self.SI_Linea_Dropdown.value != ""):
            linea = f" AND LINEA = \'{self.SI_Linea_Dropdown.value}\'"
        else:
            linea = ""
        if(self.SI_Grupo_Dropdown.value != None and self.SI_Grupo_Dropdown.value != ""):
            grupo = f" AND GRUPO = \'{self.SI_Grupo_Dropdown.value}\'"
        else:
            grupo = ""
        self.result, self.description = self.connectSQL(f'SELECT TOP 500 * FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP WHERE STOCK!=0 {tipo}{dep}{tipoalm}{linea}{grupo} ORDER BY STOCK DESC;')
        self.fill_DataTable(self.result, self.description)
        self.SI_ProgressRing_Container.visible = False
        self.page.update()

    def codigoProducto_Filter(self, e):
        self.SI_ProgressRing_Container.visible = True
        self.clearDropdowns()
        print(f"CodProdFilter: {e.control.label}={e.control.value}")
        self.page.update()
        self.result, self.description = self.connectSQL(f'SELECT TOP 80 * FROM SURGICORP_POWERAPPS.dbo.STOCKS_PWRAPP WHERE STOCK!=0 AND {e.control.data} LIKE \'%{e.control.value}%\' ORDER BY STOCK DESC;')
        self.fill_DataTable(self.result, self.description)
        self.SI_ProgressRing_Container.visible = False
        self.page.update()

    def clearFilters(self, e):
        self.SI_CodigoProducto_TextField.value = ""
        self.SI_DescripcionProducto_TextField.value = ""
        print(f"clearFilters: {e.control}")
        self.clearDropdowns()
        self.page.update()

    def clearDropdowns(self):
        self.SI_Deposito_Dropdown.value = None
        self.SI_TipoProducto_Dropdown.value = None
        self.SI_TipoAlmacen_Dropdown.value = None
        self.SI_Linea_Dropdown.value = None
        self.SI_Grupo_Dropdown.value = None
        self.page.update()