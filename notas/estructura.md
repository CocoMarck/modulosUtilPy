# Estructura de implementación de modulos

```bash
data/
    # Base de datos, o archivos con puros datos


model/
    # Entidades y modelos


controller/
    # Controladores de los modelos. Siuu!


views/
    # Programas con GUI, Qt, Gtk. O un app de consola.
    ui/
        # Archivos XML, para establecer como se vera la ventana/dialog. 
        # Archivos: .ui, .glade, .axml
    
    interface/
        # Funciones para uso general, relacionadas con el gui.
        # Dialog/Window custom, widget/custom, ya hechos. Para uso general
        qt_custom/
            widget/
            dialog/
            window/
        gtk_custom/
            widget/
            dialog/
            window/
        
        css_util.py
        interface_number.py
    __init__.py

core/
    # Funciónes para uso general
    __init__.py

    config/
        util_system_config.py

    display_number.py
    util_system.py
    util_text.py

config/
    # Archivos de configruación. xml, json, conf, txt
    runCommand.json

docs/ 
    # Documentación, pdf, md. Evitar archivos.txt pelones.

resources/
    # Archivos fijos, para usar en el programa. Imagenes, videos, iconos, etc.
    images/
    icons/
    videos/

requirements.txt # Dependencias para que jale todo.
README.md # De que se trata el proyecto.

main.py

# Otros
notas/ # Notas personales, escritos en textos.md
```