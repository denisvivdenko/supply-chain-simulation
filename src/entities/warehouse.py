from src.constraints import WAREHOUSE_STORAGE_CAPACITY
from src.entities.sku import SKU
from src.entities.client import Client


class Warehouse:
    def __init__(self, sku_list: list[SKU]) -> None:
        self.warehouse_storage_capacity = WAREHOUSE_STORAGE_CAPACITY
        self.sku_list = sku_list


    def process_client(self, client: Client, day: int) -> None:
        pass