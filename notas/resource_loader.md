# ResourceLoader, para manejar todos los archivos del directorio `resources`

En dicho directorio `resources`, se contienen todas las imagenes, iconos, videos, que usa el programa.

`ResourceLoader`, es un objeto que usa `pathlib` el cual establece el directorio `resources`, y los directorios que estan adentro de `resources`. Todos adentro de una variable.

**Esta clase estara en `utils/resource_loader.py`**. Este es así debido a que esta clase no hace ninguna logica de negocio.


## Métodos de `ResourceLoader`:  
- `get_data( self, file: str ) -> pathlib.Path`: Obtiene la ruta de las base de datos.


- `get_config( self, file: str ) -> pathlib.Path`: Obtiene la ruta de los archivos de configuracion. Pueden ser xml, json, .confg, .txt, .ini


- `get_image( self, image: str ) -> pathlib.Path`: Obtiene la ruta donde estan las imagenes.


- `get_icon( self, icon: str ) -> pathlib.Path`: Obtiene la ruta donde estan los iconos


- `exists(self) -> bool`: Determina si existe la ruta `resources`


- `get_recursive_tree(self, path: object | pathlib.Path ) -> dict`: Obtiene los directorios y archivos de manera recursiva, en un directorio establecidoen el parametro `path`.
        

- `get_image_tree( self ) -> dict`: Obtiene de manera recursiva, los directorios y archivos de la ruta `resources/images`




# ResorceController  
**Esta clase estara en `controllers/resource_controller.py`**

Esta clase manejara a prueba de errores `ResourceLoader`, tendra `self.verbose` para el debug, y condicionales if, para determinar si existen los archivos. Los metodos en este objeto tienen la intención de no dar crash.

## Establecera, imagenes; placeholder y para errores. Ejemplos:
- Para errores
    - `no_image.png`
- Para placeholder
    - `placeholder.png`