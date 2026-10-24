from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import model as model

#2. Servidor FastAPI
app = FastAPI(
    title="API de IMC de Carlos Pacheco",
    description="Servicio web para calcular el IMC del usuario",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=FileResponse)
def inicio():
    return FileResponse("index.html")
@app.get("/api/estado")
def estado():
    """
    Direccion de la api que devuelve el estado actual de la misma y sus detalles
    """
    return {
        "estado": "Operativo",
        "servicio": "API de Cálculo de IMC y Riesgo de Infarto",
        "version": "1.0.0",
        "modelos_activos": ["CalculoIMC"],
        "autor": "Carlos Pacheco Belzunces"
    }

@app.post("/api/calcular-imc", response_model=model.ResultadoCalculoIMC)
def calcular_imc(solicitud: model.SolicitudCalculoIMC):
    """
    A través de la altura, la edad y el peso del usuario nos permite calcular su IMC y devolvemos el porcentaje de riesgo de infarto y un consejo de salud personalizado
    """
    categoria_peso = "Peso normal";
    resultado_imc = (solicitud.peso_persona / ((solicitud.altura_persona/100) * (solicitud.altura_persona/100)));
    
    if resultado_imc < 18.5:
        categoria_peso = "Peso bajo";
    elif resultado_imc >= 18.5 and resultado_imc < 24.9:
        categoria_peso = "Peso adecuado";
    elif resultado_imc >= 25 and resultado_imc < 29.9:
        categoria_peso = "sobrepeso";
    elif resultado_imc >=30 and resultado_imc < 34.9:
        categoria_peso = "obesidad grado 1";
    elif resultado_imc >= 35 and resultado_imc < 39.9:
        categoria_peso = "obesidad grado 2";
    elif resultado_imc >= 40:
        categoria_peso = "obesidad grado 3"

# Bonificaciones y penalizaciones segun la edad
    if solicitud.edad < 40:
        boni_edad = 1
    elif solicitud.edad >= 40 and solicitud.edad <= 60:
        boni_edad = 2
    else:
        boni_edad = 3

    if categoria_peso == "Peso bajo" or categoria_peso == "Peso adecuado":
        boni_peso = 1
    elif categoria_peso == "sobrepeso" or categoria_peso == "obesidad grado 1":
        boni_peso = 2
    else:
        boni_peso = 3

# Bonificaciones y penalizaciones segun la el deporte que se haga
    if solicitud.deporte == "No hago nada":
        boni_deporte = 2 
    elif solicitud.deporte == "1 vez a la semana":
        boni_deporte = 1 
    elif solicitud.deporte == "2-3 veces a la semana":
        boni_deporte = 0 
    else: 
        boni_deporte = -1 


    calcular_riesgo_infarto = (boni_edad * boni_peso) + boni_deporte
    if solicitud.fumador == True:
        calcular_riesgo_infarto = calcular_riesgo_infarto + 1

# Resultados finales
    if calcular_riesgo_infarto <= 2:
        probabilidad_infarto = "0-10%"
        recomendacion = "Estas como un roble, sigue así lo estas haciendo muy bien"
    elif calcular_riesgo_infarto > 2 and calcular_riesgo_infarto <= 4:
        probabilidad_infarto = "15-25%"
        recomendacion = "Estas bien, mantente activo y cuida tu alimentación"
    elif calcular_riesgo_infarto > 4 and calcular_riesgo_infarto <= 6:
        probabilidad_infarto = "30-40%"
        recomendacion = "Riesgo moderado. Sería muy recomendable mejorar tu alimentación o hacer algo más de deporte."
    elif calcular_riesgo_infarto > 6 and calcular_riesgo_infarto <= 8:
        probabilidad_infarto = "50-60%"
        recomendacion = "Si no cambias tu estilo de vida, tu riesgo de infarto es alto, deberias bajar tu peso y hacer ejercicio"
    elif calcular_riesgo_infarto > 8 and calcular_riesgo_infarto <= 10:
        probabilidad_infarto = "70-80%"
        recomendacion = "Tienes mucho riesgo, deberías bajar tu peso urgentemente y establecer una rutina de ejercicios."
    else:
        probabilidad_infarto = "90-100%"
        recomendacion = "Tienes mucha suerte, si no cambias tu estilo de vida, tu riesgo de infarto es inminente, deberias bajar tu peso y hacer ejercicio"


    return {
        "solicitante": solicitud.nombre,
        "calculo_imc": resultado_imc,
        "categoria_peso": categoria_peso,
        "probabilidad_infarto": probabilidad_infarto,
        "recomendacion": recomendacion
    }
