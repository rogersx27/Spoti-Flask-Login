# Proyecto de Integración con Spotify API

Este proyecto consiste en una aplicación web desarrollada con Flask que integra la API de Spotify para permitir a los usuarios acceder a sus playlists, información de usuario y canciones guardadas.

## Requisitos previos

- Python 3.x instalado en tu sistema.

- Flask y otras dependencias necesarias instaladas. Puedes instalarlas utilizando el archivo `requirements.txt`.

**Comando de consola:**

 	pip install -r requirements.txt

- Credenciales de la API de Spotify. Debes registrar tu aplicación en el [Panel de Desarrolladores de Spotify](https://developer.spotify.com/) para obtener las credenciales necesarias.

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar correctamente las credenciales de la API de Spotify en el archivo `Utils.py`. Reemplaza `'CLIENT_ID'` y `'CLIENT_SECRET'` con tus propias credenciales.
Además no olvides también configurar tu `'SECRET_KEY'` para que la sesión de Flask pueda configurarse correctamente, la puedas encontrar en el archivo `__init__.py`

```python
CLIENT_ID = 'TU_CLIENT_ID'
CLIENT_SECRET = 'TU_CLIENT_SECRET'
SECRET_KEY = 'TU_SECRET_KEY'
```

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el archivo `app.py`.
Esto iniciará el servidor Flask y podrás acceder a la aplicación desde tu navegador en la dirección `http://localhost:5000`.

### Uso
Una vez que la aplicación esté en funcionamiento, podrás realizar las siguientes acciones:

- Iniciar sesión con tu cuenta de Spotify.
- Obtener información de usuario.
- Obtener listas de reproducción del usuario.
- Obtener las canciones guardadas del usuario.


