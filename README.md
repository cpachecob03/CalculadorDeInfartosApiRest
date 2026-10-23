
### AS1. API Rest + Despliegue
# Calculadora de IMC y Riesgo Cardiovascular (API REST)

Primero de todo deberemos clonar el repositorio del proyecto: 
```js
git clone https://github.com/cpachecob03/CalculadorDeInfartosApiRest.git
```

### Descripción del proyecto

En este proyecto se implementa una API Rest desarrollada con FastAPI, que calcula el IMC del usuario y segun la edad del usuario devuelve una estimación del riesgo de infarto y un consejo de salud personalizado.

### URL del proyecto desplegado
Puedes probar la aplicación en la siguiente URL:
```js
https://calculadordeinfartosapirest.vercel.app/
```
### Plataforma de despliegue
La plataforma de despliegue que utilizare es Vercel

### Descripción detallada del proceso de despliegue

Para desplegar esta aplicación en vercel, tendremos que adaptar ciertos archivos al entorno de vercel. 
A continuación se detallan los pasos para realizar este despliegue:

# Preparación de las dependencias
Vercel necesita saber qué paquetes de Python instalar. Para ello, es obligatorio crear un archivo llamado `requirements.txt` en la raíz del proyecto que contenga las librerías principales:
```js
fastapi
uvicorn
pydantic
```
Creación del archivo de configuración de vercel ( vercel.json )
Para que vercel sepa como ejecutar nuestra aplicacion FastAPI, creamos en la raiz un archivo llamado "vercel.json". Este archivo indica a vercel que debe usar el entorno de Python y redirifir todo el tráfico a "app.py".
```js
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "destination": "app.py"
    }
  ]
}
```
# 4. Despliegue desde la plataforma de Vercel
Con el código preparado y subido a un repositorio de GitHub:
 1.- Accedemos a Vercel e iniciamos sesión con nuestra cuenta de GitHub.
 2.- Hacemos clic en Add New Project.
 3.- Importamos el repositorio de nuestro código.
 4.- Pulsamos en Deploy.

Vercel leerá el vercel.json, instalará el requirements.txt y generará las rutas de nuestra API automáticamente. Tras unos segundos, nos proporcionará la URL pública.