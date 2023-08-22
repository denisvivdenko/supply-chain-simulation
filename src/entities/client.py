import numpy as np

from src.constraints import CLIENT_MONEY_RANGE

class Client:
    def __init__(self) -> None:
        self.money = np.random.randint(*CLIENT_MONEY_RANGE)