from inventory_report.product import Product


def test_create_product() -> None:
    product = Product("1", "Arroz", "KG", "5", "1", "0", "cool dry place")
    assert product.id == "1"
    assert product.product_name == "Arroz"
    assert product.company_name == "KG"
    assert product.manufacturing_date == "5"
    assert product.expiration_date == "1"
    assert product.serial_number == "0"
    assert product.storage_instructions == "cool dry place"
