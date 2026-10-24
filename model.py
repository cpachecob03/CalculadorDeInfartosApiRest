from pydantic import BaseModel, Field
from typing import Literal

class SolicitudCalculoIMC(BaseModel):
    nombre: str = Field(min_length=2, max_length=50, description="Nombre del solicitante")
    edad: int = Field(ge=10, le=90,  description="Edad del usuario (entre 10 y 90 años)")
    peso_persona: float = Field(gt=25, le=300, description="peso en kilogramos")
    altura_persona: float = Field(gt=50, le=250, description="Altura del usuario en centimetros (100cm = 1m)")
    deporte: Literal["No hago nada", "1 vez a la semana", "2-3 veces a la semana", "Más de 4 días"] = Field(description="Frecuencia de actividad física")
    #se usa Literal cuando quieres limitar las opciones de un campo con x valores
    fumador: bool = Field(default=False, description="Indica si el usuario fuma habitualmente, por defecto diremos que no fuma")

class ResultadoCalculoIMC(BaseModel):
    solicitante: str = Field(description="Nombre del usuario que hace la consulta")
    calculo_imc: float = Field(description="IMC del usuario")
    categoria_peso: str = Field(description="Clasificación del peso (peso adecuado, sobrepeso)")
    probabilidad_infarto: str = Field(description="Porcentaje estimado de riesgo de infarto")
    recomendacion: str = Field(description="Consejos de salud personalizados según los resultados") 