# Obtener salida de comando

[stack tuto](https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output#4760517)

## Dos formas de hacerlo.

### Método try, except:  
```python
try: 
    return subprocess.check_output( command, shell=True, text=True )
except:
    return "[ERROR]"
```

### Método mas legacy, pero sin el try except, devuelve puro string:
```python
return subprocess.getoutput( command )
```