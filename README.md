# :card_index_dividers: temp-python

Template de Python 3 para proyectos base, utliza las librerias del repo de [este link](https://github.com/brianwolf/repo-python-libs)

![docs](docs/img/python.png)

## :tada: Uso

Solo es necesario entrar en `src` y ejecutar el archivo `app.py` con python.

### Estructura

- La carpeta *consume* corresponde a todo lo que la aplicacion necesita para funcionar

- La carpeta *produce* es para todo lo generado por la misma como los logs por ejemplo

- La carpeta *logic* contiene el codigo de la aplicacion

## :books: Levantar un ambiente de desarrollo

Es necesario ejecutar los siguientes comandos en linux:

```bash
# pararse dentro de la carpeta src
cd src

# crear el ambiente virtual
virtualenv -p python3.8 env

# dentro del virtualenv instalar las dependencias con pip
pip install -r requirements.txt

# ejecutar con flask
python app.py
```

## :grin: Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
