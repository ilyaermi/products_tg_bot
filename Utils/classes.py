from dataclasses import dataclass
from time import time


@dataclass
class Expenditure:
    time: int = time()
    user_id: int = None
    product: str = None
    flow_direction: str = None
    count: float = None
    price: float = None


@dataclass
class Coming:
    time: int = time()
    user_id: int = None
    product: str = None
    count: float = None
