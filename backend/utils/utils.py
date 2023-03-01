import os
import logging
from typing import Union, List, Generator


def populate_file(filename: str, data: List[str]) -> None:
    with open(filename, "w") as handler:
        for content in data:
            handler.write(content + "\n")

def read_file(filename: str) -> Generator:
    with open(filename, "r") as handler:
        for line in handler:
            yield line

def read_if_exists(filename: str) -> Union[List, Generator]:
    if os.path.isfile(filename):
         yield from read_file(filename)

    return []

def get_file_logger(file_name: str, log_level: str="INFO") -> object:
    logger = logging.getLogger(file_name)
    logger.setLevel(log_level)
    logging.basicConfig(
        format="%(levelname)s %(name)s %(asctime)s %(message)s",
        datefmt="%y-%m-%d %H-%M-%S",
        filename="logs/logs.txt"
    )

    return logger

def get_console_logger(file_name: str, log_level: str="INFO") -> object:
    logger = logging.getLogger(file_name)
    logger.setLevel(log_level)

    logger.basicConfig(
        format="%(levelname)s %(name)s %(asctime)s %(message)s",
        datefmt="%y-%m-%d %H-%M-%S"
    )

    ## add stdout logger
    console = logging.StreamHandler()
    logger.addHandler(console)

    return logger