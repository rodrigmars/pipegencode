from typing import Tuple

def create(code, data: list) -> list:

    return [code, data[0], data[1]]


def find_by_email(data: Tuple[int, list]) -> tuple:

    id, mock_data = data

    return list(filter(lambda x: x[0] == id, mock_data))[0],


def email(_) -> set:
    return {1, "Email disparado"}

