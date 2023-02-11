from typing import Generator
from random import randint
from time import sleep

def pipe_generator(fns: tuple) -> Generator:

    for fn in fns:

        sleep(randint(2, 5))

        yield fn
