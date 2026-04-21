"""
Cliente para interactuar con la API de Tenable.

Este módulo se encarga de la autenticación y las llamadas a la API.
"""


class TenableClient:
    """Cliente base para la API de Tenable."""

    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key
        # TODO: inicializar cliente de pytenable

    def get_scan_results(self, scan_id: str):
        """Obtiene los resultados de un escaneo concreto."""
        # TODO: implementar
        raise NotImplementedError
