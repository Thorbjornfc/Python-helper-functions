"""
This module provides a logging utility for the genetic algorithm (GA) and non-dominated sorting genetic algorithm (NSGA) implementations.
"""

from dataclasses import dataclass
import logging
import os
import datetime



LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")

class FrontLogger(logging.Logger):
    @classmethod
    def from_logger(cls,parent:logging.Logger):
        obj = cls.__new__(cls)
        obj.__dict__ = parent.__dict__
        obj.__class__ = cls
        return obj


    def log_fronts(self, fronts: list[list], *args, **kwargs) -> None:
        self.info("[")
        for j, front in enumerate(fronts):
            self.info("[")
            for g in front:
                self.info(str(g) + ",")
            self.info("],")
        self.info("],")

def get_logger(name:str,filepath:str,format=LOG_FORMAT)->logging.Logger:
    if logging.getLogger(name).hasHandlers():
        return logging.getLogger(name)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)


    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    logger_file_handler = logging.FileHandler(filepath) # default 'append' mode
    logger_file_handler.setLevel(LOG_LEVEL)
    logger_file_handler.setFormatter(logging.Formatter(format))
    logger.addHandler(logger_file_handler)
    logger.propagate = False
    return logger



@dataclass(frozen=True)
class Loggers:
    _date = datetime.datetime.now().strftime("%Y_%m_%d")
    _time = datetime.datetime.now().strftime("%H_%M_%S")

    ga_main: logging.Logger = get_logger("ga.ga", os.path.join(LOGS_DIR, "ga_ga",_date+".log"))
    ga_genome: logging.Logger = get_logger("ga.genome", os.path.join(LOGS_DIR, "ga_genome",_date+".log"))
    nsga_main: logging.Logger = get_logger("nsga.nsga", os.path.join(LOGS_DIR, "nsga_nsga",_date+".log"))
    nsga_genome: logging.Logger = get_logger("nsga.genome", os.path.join(LOGS_DIR, "nsga_genome",_date+".log"))
    _nsga_fronts: logging.Logger = get_logger("nsga.fronts", os.path.join(LOGS_DIR, "nsga_fronts",_date+".txt"), format="%(message)s")
    nsga_fronts: FrontLogger = FrontLogger.from_logger(_nsga_fronts)
