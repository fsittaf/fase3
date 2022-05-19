from lib2to3.pgen2.pgen import generate_grammar
from uuid import uuid4


def generate_id():
    return uuid4().hex
