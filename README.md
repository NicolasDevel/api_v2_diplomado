# Como ejecutar el proyecto

## Requerimientos

- Python
- Postgresql
- Visual Studio Code

## Clonar repositorio

Se recomienda crear una carpeta vacía en algun directorio de tu computador en mi caso yo la creare en la carpeta documentos:


```bash
cd Documents
mkdir api_products
cd api_products
```

Clonamos el repositorio
```bash
git clone https://github.com/NicolasDevel/api_v2_diplomado.git
```

Creamos y activamos un entorno virtual
```bash
python -m venv enviroment
#windows
./enviroment/Scripts/activate
#Mac / Linux
source enviroment/bin/activate
```

## Instalamos dependencias
Ahora debemos instalar las dependencias del proyecto, para esto debemos primero ir a la carpeta que contiene el proyecto de django

```bash
cd api_v2_diplomado
```

Ahora debemos ejecutar el comando para instalar las dependencias

```bash
pip install -r requirements.txt
```

## Configurar las variables de entorno
Crea un archivo .env en la raiz del proyecto de django, cosa que quede al mismo nivel que el archivo manage.py; para este archivo .env puedes tomar como referencia el archivo .env.example

```bash
touch .env
```


