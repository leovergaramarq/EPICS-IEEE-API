from typing import List, Any, Callable, Optional

# calcula un puntaje en base a un número de aciertos y un número de fallos
def calcScore(numAciertos, numFallos):
    numPreguntas = numAciertos + numFallos
    if numPreguntas == 0:
        return 0
    else:
        return (numAciertos / numPreguntas) * 100

def find(lst: List[Any], key: Callable[[Any], bool]) -> int:
    """
    Find the index of the first element in a list that satisfies a given condition.
    
    :param lst: The list to search.
    :param key: The condition to satisfy.

    :return: The index of the first element that satisfies the condition, or -1 if no element satisfies the condition.
    """
    for i, x in enumerate(lst):
        if key(x):
            return i
    return -1

def get_user_from_token(token: str) -> Optional[str]:
    """
    Get the user from a token.
    """
    raise NotImplementedError