from inventory_report.product import Product
from typing import List


class Inventory:
    def __init__(self, data: List[Product] | None = None):
        self._data = [] if data is None else data

    @property
    def data(self) -> List[Product]:
        return self._data.copy()

    def add_data(self, data: List[Product]) -> None:
        self._data.extend(data)
