# Tienda de Cómics

Proyecto realizado para la evaluación Sumativa 3 de Programación Back End.

La aplicación fue desarrollada con Django y permite visualizar un catálogo de cómics, buscar por título, filtrar por editorial y realizar reservas.

También cuenta con un panel de administración para gestionar los cómics, editoriales y reservas.

## Integrantes

- Nibaldo Zepeda
- Alexandro Pantelakos

## Tecnologías utilizadas

- Python y Django
- SQLite
- HTML y CSS
- Git y GitHub

## Requisitos para Windows

- Python 3 instalado. La instalación actual fue comprobada con Python 3.14 en macOS; la configuración de ejecución de esta guía está preparada para Windows.
- Git para Windows.
- Conexión a Internet para descargar las dependencias la primera vez.

Verifica las instalaciones desde PowerShell o CMD:

```powershell
python --version
py --version
git --version
pip --version
```

Si `python` no funciona, prueba usar `py` en los comandos siguientes.

## Clonar el proyecto

Desde PowerShell o CMD:

```powershell
git clone https://github.com/Pante45/comics.git
cd comics
```

## Crear y activar el entorno virtual en Windows

PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación con un error de ejecución de scripts, permite scripts de forma temporal y vuelve a intentarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

También puedes activar el entorno desde CMD:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

Cuando el entorno esté activo, el nombre `(.venv)` debe aparecer al inicio de la línea de comandos.

## Instalar dependencias y ejecutar la aplicación

Con el entorno virtual activo:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre en el navegador:

```text
http://127.0.0.1:8000/
```

Para detener el servidor presiona `Ctrl+C`. Para salir del entorno virtual:

```powershell
deactivate
```

## Errores frecuentes en Windows

- `ModuleNotFoundError: No module named 'django'`: Django no está instalado o el entorno virtual no está activo.
- `python` no se reconoce: instala Python desde python.org y selecciona **Add Python to PATH**, o usa `py`.
- PowerShell no permite activar el entorno: usa el comando de `Set-ExecutionPolicy` indicado arriba o abre CMD.
- Error al instalar una versión: instala primero una versión compatible de Python y vuelve a crear el entorno virtual:

```powershell
deactivate
Remove-Item -Recurse -Force .venv
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```