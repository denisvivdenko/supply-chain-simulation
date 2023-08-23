from src.constraints import WAREHOUSE_STORAGE_CAPACITY
from src.entities.sku import SKU
from src.entities.client import Client

import numpy as np


class Warehouse:
    def __init__(self, sku_list: list[SKU]) -> None:
        self.warehouse_storage_capacity = WAREHOUSE_STORAGE_CAPACITY
        self.sku_list = sku_list
        self.warehouse_storage = {sku: 0 for sku in sku_list}
        self.sku_seasonality = np.array([sku.seasonality for sku in sku_list])
        self.sku_normalized_seasonality = self.sku_seasonality / self.sku_seasonality.sum(axis=0)

    def sell_to_client(self, client: Client, current_day: int) -> float:
        sku_daily_normalized_seasonality = self.sku_normalized_seasonality[:, current_day % 365]
        random_sku = np.random.choice(self.sku_list, p=sku_daily_normalized_seasonality)

        if client.money >= random_sku.price and self.warehouse_storage[random_sku] > 0:
            client.money -= random_sku.price
            self.warehouse_storage[random_sku] -= 1
            return random_sku.price
        
        return 0.0
    
    def accept_truck(self, truck):
        for sku, qty in truck.sku_vs_qty.items():
            self.warehouse_storage[sku] += qty