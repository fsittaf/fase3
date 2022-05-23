from lib2to3.pgen2.pgen import generate_grammar
from uuid import uuid4


def generate_id():
    """
    Willl generate a identifier to be used as ID in the users
    """
    return uuid4().hex
