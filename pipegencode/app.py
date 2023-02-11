from typing import Generator, Tuple
from random import randint
from time import sleep

def create(code, data: list) -> list:

    return [code, data[0], data[1]]


def find_by_email(data: Tuple[int, list]) -> tuple:

    id, mock_data = data

    return list(filter(lambda x: x[0] == id, mock_data))[0],


def email(_) -> set:
    return {1, "Email disparado"}

def pipe_generator(fns: tuple) -> Generator:

    for fn in fns:

        sleep(randint(2, 5))

        yield fn


def main():

    mock_data = [[10, 'Tke', False],
          [14, 'tk_@452.com', True],
          [18, 'e4_@155.com', False],
          [22, 'op_@785.com', True],
          [25, 'rt_@89.com', False]]

    data = ('lkc@452.com', True)

    for i, output in enumerate(pipe_generator((create, find_by_email, email))):

        if i < 1:
            mock_data.append(output(mock_data[-1][0] + 1, data))
            
            data = mock_data[-1][0], mock_data
            
            print(f"\npipe:{i}", data, "\n")

        else:
            print(f"pipe:{i}", data := output(data), "\n")

if __name__ == "__main__":

    main()
