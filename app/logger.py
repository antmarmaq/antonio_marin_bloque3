import logging
from logging.config import dictConfig

cfg = {
    "version": 1,
    "formatters": {
        "consola": {"format": "%(message)s"},
        "fichero": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "consola": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "consola",
            "stream": "ext://sys.stdout",
        },
        "fichero": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "fichero",
            "filename": "logs.log",
            "encoding": "utf-8",
        },
    },
    "loggers": {"alquiler": {"handlers": ["consola", "fichero"], "level": "DEBUG"}},
}

dictConfig(cfg)
logger = logging.getLogger("alquiler")
