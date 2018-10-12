# learning-python
Some personal files in order to learn python

1. Bajarse la última versión de Python. 
2. Seguir estos pasos desde una termina en la carpeta de python (https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul): 

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
sudo apt-get install libffi-dev
./configure
make
sudo make altinstall

3. Al final, si ejecutamos python3.7 se lanzará el intérprete de python y podremos escribir un hola mundo tal que así:
message = "hello world"
print(message)

4. Ahora nos vamos a instalar visual studio code. 
5. Después su extension. (Codigo de https://marketplace.visualstudio.com/items?itemName=ms-python.python) PAra ello, desde VsCode hacemos ctrp p y ejecutamos lo siguiente;
ext install ms-python.python
6.Ahora vamos a instalar un linter(más info: https://code.visualstudio.com/docs/python/linting). To enable linters other than the default PyLint, open the Command Palette (Ctrl+Shift+P) and select the Python: Select Linter. Selecciones pylint
7. Para ejecutarlo, dos opciones:
    Linting runs automatically when you save a file.
    Open the Command Palette (Ctrl+Shift+P), then enter and select Python: Run Linting.
8. Puedes elegir el intérprete usando ctrl+shift+p choose interperster. Por defecto una el 2.7, que no sé si es el que tiene vscode instlaador o yo que sé. He seleccionado el 3.7 . Es fácil, directamente te los lista.  Para asegurarse de la versión:
import sys
print(sys.version)

9. Hay que elegir un famework para pruebas también desde la paleta de comandos (ctrl+shift+p). He escogido Pytest (http://pythontesting.net/transcripts/2-pytest-vs-unittest-vs-nose/)

10. VS Code te avisa de que el linter o el pytest no se han podido instalar.Será por tema de permisos. Para ello, ver el comando que está intentando ejecutar y ejecutarlo igual desde la misma terminal de VS Code anteponiendo sudo. 

Más información:
https://code.visualstudio.com/docs/languages/python

Para instalar smartgit
==========================
http://www.kvcodes.com/2016/03/install-uninstall-smartgit-ubuntu/


Y no va...hay que seguir estos pasos:
Yo sólo hice los dos primeros:
$ sudo apt-get update
$ sudo apt-get install openjdk-8-jdk

Si no,ver:
https://stackoverflow.com/questions/30101420/smartgit-not-opening

====================
Cosas de Linux. 

1. Para crear un fichero, abrir una terminarl y poner:
touch nombreDeFichero.txt



