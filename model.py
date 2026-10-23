from pydantic import BaseModel, Field

class SolicitudCalculoIMC(BaseModel):
    nombre: str = Field(min_length=2, max_length=50, description="Nombre del solicitante")
    edad: int = Field(ge=10, le=90,  description="Edad del usuario (entre 10 y 90 años)")
    peso_persona: float = Field(gt=25, le=300, description="peso en kilogramos")
    altura_persona: float = Field(gt=50, le=250, description="Altura del usuario en centimetros (100cm = 1m)")

class ResultadoCalculoIMC(BaseModel):
    solicitante: str = Field(description="Nombre del usuario que hace la consulta")
    calculo_imc: float = Field(description="IMC del usuario")
    categoria_peso: str = Field(description="Clasificación del peso (peso adecuado, sobrepeso)")
    probabilidad_infarto: str = Field(description="Porcentaje estimado de riesgo de infarto")
    recomendacion: str = Field(description="Consejos de salud personalizados según los resultados") 