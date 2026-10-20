from pydantic import BaseModel, Field

class SolicitudCalculoIMC(BaseModel):
    nombre: str = Field(min_length=2, max_length=50, description="Nombre del solicitante")
    edad: int = Field(ge=10, le=90, description="Edad del usuario (entre 10 y 90 años)")
    peso_persona: float = Field(gt=25, description="peso en kilogramos")
    altura_persona: float = Field(gt=80, description="Altura del usuario en centimetros (100cm = 1m)")

class ResultadoCalculoIMC(BaseModel):
    solicitante: str
    calculo_imc: float
    categoria_peso: str
    probabilidad_infarto: str  
    recomendacion: str        