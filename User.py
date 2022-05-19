from dataclasses import dataclass  # , replace
from Role import Role

# Model

# Criar atributo de senha temporária?


@dataclass(init=True)
class User:
    user_id: str = None
    name: str = None
    last_name: str = None
    email: str = None
    age: str = None
    role: Role = None
    created_at: str = None
    updated_at: str = None
