from typing import Generator
from random import randint
from time import sleep


def main(mock_data: list):

    def create(data: list) -> int:
        mock_data.append([code := mock_data[-1][0] + 1, data[0], data[1]])
        return code

    def find_by_email(id: int) -> tuple:
        return list(filter(lambda x: x[0] == id, mock_data))[0],

    def email(_) -> set:
        return {1, "Email disparado"}

    def pipe_generator(fns: tuple) -> Generator:

        for fn in fns:

            sleep(randint(2, 5))

            yield fn

    data = ('lkc@452.com', True)

    for output in pipe_generator((create, find_by_email, email)):

        print(data := output(data))

    print("\n", mock_data)

if __name__ == "__main__":

    main([[10, 'Tke', False],
          [14, 'tk_@452.com', True],
          [18, 'e4_@155.com', False],
          [22, 'op_@785.com', True],
          [25, 'rt_@89.com', False]])
