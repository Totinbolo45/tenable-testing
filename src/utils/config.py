"""
Carga de configuración y variables de entorno.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Configuración del proyecto cargada desde variables de entorno."""

    tenable_access_key: str
    tenable_secret_key: str
    openai_api_key: str

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            tenable_access_key=os.getenv("TENABLE_ACCESS_KEY", ""),
            tenable_secret_key=os.getenv("TENABLE_SECRET_KEY", ""),
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        )
