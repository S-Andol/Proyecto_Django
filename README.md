# Proyecto_Django
En los readme colocamos los pasos o explicaciones del proyecto.


Abro terminal y colocamos pwd

# Clonamos los archivos del GitHub
    git clone https://github.com/S-Andol/Proyecto_Django.git

21:26

# Creamos un entorno virtual

python -m venv venv
    Al tener en .gitignore de las extenciones el formato .venv. Significa que no le va a dar bola a nuestra carpeta. No las va a tener en cuenta ni las va a subir a la nube.

Si hay alguna carpeta que queres que se ignore o no se suba. HAY QUE IGNORARLO ANTES DE "CREARLO" AL ARCHIVO!!!

# Activamos el entorno virtual

. venv/Scripts/activate

pip = manejador de paquetes en python

# Mostrar los paquetes que tengo instalado en el entorno virtual que se creo

pip freeze

# Instalamos los paquetes

pip install Django

# Revisamos nuevamente los paquetes instalados

pip freeze

# Para poder utilizar los paquetes que voy agregando a venv, hay que utlizar un archivo aparte. "requirements.txt

pip freezee > requirements.txt
Crea el archivo y agrega todos los paquetes instalados...

# Habilitamos un comando de Django

3django-admin startproject "nombre del proyecto"(no utulizar "-"Pero si se puede "_")
django-admin startproject proyecto_django

# Ahora tenemos que colocar al mismo nivel que los .gitingore, README y requiments.

Cambiamos el nombre de la carpeta de afuera "proyecto_django" por "proyecto_django2"
Sacamos tanto la carpeta interna "proyecto_django" y "manage.py"

Estructura:
    proyecto_django
    venv
    .gitignore
    manage.py
    README.md
    requirements.txt

# Probamos el archivo manage.py, ejecutando el server

python manage.py runserver

Nos lanza una URL, donde por medio de esa direccion se puede acceder al proyecto. http://127.0.0.1:8000/

Al correr el runserve se crea un archivo: 
db.sqlite3, es un archivo de base de datos. (el cual me lo ignora)

asgi.py y wsgi.py son archivos que indican la forma en que se van a conectar la gente con el proyecto.

settings.py tiene casi todas las config del proyecto

urls.py tiene las direcciones por donde nos vamos a dirigir a nuestras paginas

# Migrar a la base de datos archivos, para que ande correctamente.

python manage.py migrate
Si entramos en db.sqlite3 podemos observar las 18 migraciones...

# git status

# git add .

# git commit -m "Primeros pasos"

# git status

# git push (lo subimos)
