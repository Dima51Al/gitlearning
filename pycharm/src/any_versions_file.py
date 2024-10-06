"""Тут будут разные красивые функции"""


def is_simple(noun: int) -> bool:
    if noun == 1:
        return False
    for i in range(2, int(noun ** 0.5+1)):
        if noun % i == 0:
            return False
    return True

