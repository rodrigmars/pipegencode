from crud import create, find_by_email, email
from pipegen import pipe_generator


def signature(data: list) -> None:

    response = None

    for i, output in enumerate(pipe_generator((create, find_by_email, email))):

        if i < 1:

            data.append(
                output(data[-1][0] + 1, ('lkc@452.com', True)))

            response = data[-1][0], data

            print(f"\npipe:{i}", data, "\n")

        else:
            print(f"pipe:{i}", response := output(response), "\n")


def main():

    signature([[10, 'Tke', False],
               [14, 'tk_@452.com', True],
               [18, 'e4_@155.com', False],
               [22, 'op_@785.com', True],
               [25, 'rt_@89.com', False]])


if __name__ == "__main__":

    main()
