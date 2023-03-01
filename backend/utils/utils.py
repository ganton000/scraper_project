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