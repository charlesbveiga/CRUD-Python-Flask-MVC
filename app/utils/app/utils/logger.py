""" Módulo de utilitários para log.
Ajuda a manter consistência e evita repetição de código."""
import logging

def get_logger(name: str):
    """Cria e retorna um logger configurado."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger
