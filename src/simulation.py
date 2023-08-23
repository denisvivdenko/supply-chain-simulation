from src.entities.sku import SKU
from src.entities.warehouse import Warehouse
from src.entities.client import Client
from src.entities.truck import Truck
from src.constraints import (
    N_CLIENTS,
    N_SKU
)

import numpy as np


class Simulation:
    def __init__(
            self,
            warehouses: list[Warehouse],
        ) -> None:
        self.warehouses: list[Warehouse] = warehouses
        self.days_counter = 0
        self.revenue = 0.0

    def run(self, clients: list[Client]):
        self.days_counter += 1

        revenue_before = self.revenue
        finished = False
        while not finished:
            finished = True
            for client in clients:
                for warehouse in self.warehouses:
                    transaction_revenue = warehouse.sell_to_client(client, self.days_counter)
                    self.revenue += transaction_revenue
                    if transaction_revenue: finished = False
        print("Made revenue {:.2f} on day {}".format(self.revenue - revenue_before, self.days_counter))

if __name__ == "__main__":
    sku_list = [SKU() for _ in range(N_SKU)]
    warehouses = [Warehouse(sku_list)]

    simulation = Simulation(warehouses=warehouses)

    for _ in range(365):
        clients = [Client() for _ in range(N_CLIENTS)]
        random_truck = Truck(
            sku_vs_qty={sku: np.random.randint(1, 10) for sku in sku_list}
        )
        np.random.choice(simulation.warehouses).accept_truck(random_truck)

        simulation.run(clients)
    # print(sku_list)


