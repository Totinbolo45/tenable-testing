"""
Script para probar el escaneo en local sin tener que lanzar GitHub Actions.
"""

from src.utils.config import Config
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger(__name__)
    config = Config.from_env()

    logger.info("Iniciando escaneo en local...")
    # TODO: encadenar scanner -> ai -> report
    logger.info("Escaneo finalizado.")


if __name__ == "__main__":
    main()
