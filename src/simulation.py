from src.entities.sku import SKU
from src.entities.warehouse import Warehouse
from src.entities.client import Client
from src.constraints import (
    N_CLIENTS,
    N_SKU
)

class Simulation:
    def __init__(
            self,
            warehouses: list[Warehouse],
            clients: list[Client]
        ) -> None:
        self.warehouses = warehouses
        self.clients = clients

    def run(self):
        pass


if __name__ == "__main__":
    clients = [Client() for _ in range(N_CLIENTS)]
    sku_list = [SKU() for _ in range(N_SKU)]
    warehouses = [Warehouse(sku_list)]

    simulation = Simulation(
        warehouses=warehouses,
        sku_list=sku_list,
        clients=clients
    )
    
    print(sku_list)


