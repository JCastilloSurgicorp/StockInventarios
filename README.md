# StockInventarios
Programa de Stock de Inventarios para la empresa Surgicorp
Desarrollado en el FrameWork de Flet.
# Requerimientos
* Python Enviroment (Funciona mejor en un entorno virtual para el desarollo)
    * Comando para Crear venv: python3 -m venv <Nombre del Virtual Enviroment. Ej:myenv>
    * Instalar librerías utilizando el archivo requirements: pip install -r requirements.txt
    * Comando para crear un nuevo archivo requeriments: python3 -m pip freeze > requirements.txt
    * Instalar la librería openpyxl con el comando: pip install openpyxl
* Se necesita instalar el controlador de consultas SQL para pyodbc:
    * Nombre: msodbcsql(x64).msi
    * Enlace: https://go.microsoft.com/fwlink/?linkid=2266640
    * Enlace de Documentación: https://learn.microsoft.com/es-es/sql/connect/odbc/windows/microsoft-odbc-driver-for-sql-server-on-windows?view=sql-server-ver16
    * On ubuntu:
        * curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
        * curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
        * sudo apt-get update
        * sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
        * optional: for bcp and sqlcmd
            * sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
            * echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
            * source ~/.bashrc
        * optional: for unixODBC development headers
            * sudo apt-get install -y unixodbc-dev
# Ejecutar el Programa
* Debes estar en la carpeta donde esta guardado el archivo descargado. Ej: D:\Documentos\AppsSurgi\Scripts\FLETwithSQL
* Crear el Virtual Enviroment con el comando descrito en REQUERIMIENTOS
* Ingresar al Virtual Enviroment con el comando: <myenv>/Scripts/activate.ps1
* Instalar las librerías con el comando descrito en REQUERIMIENTOS
* Ejecutar el programa con el comando: flet run fletwithSQL.py
# Empaquetado
* En aplicación de Escritorio:
    * Instalar el paquete pyinstaller para realizar el empaquetado con el comando: pip install pyinstaller
    * Instalar el paquete de pillow para convertir imagenes png a .ico con el comando: pip install pillow
    * Comando para realizar el empaquetado en .exe: pyinstaller fletwithSQL.py --onefile --icon <Ruta del icono.Ej.:D:\Documentos\AppsSurgi\Scripts\FLETwithSQL\assets\images\LogoSurgi.png> --add-data <Ruta de los recursos.Formato:  assets;RutaRelativa.Ej.:"assets;assets"> --noconsole