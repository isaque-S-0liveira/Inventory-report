import json
from typing import Dict, Type, List
from inventory_report.product import Product
from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            conteudo = file.read()
            dados = json.loads(conteudo)
            lista_produtos = []
            for produto in dados:
                produto = Product(
                    produto["id"],
                    produto["product_name"],
                    produto["company_name"],
                    produto["manufacturing_date"],
                    produto["expiration_date"],
                    produto["serial_number"],
                    produto["storage_instructions"],
                )
                lista_produtos.append(produto)
            return lista_produtos


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
