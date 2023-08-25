from inventory_report.product import Product


def test_product_report() -> None:
    product = Product("1", "Arroz", "KG", "5", "1", "0", "cool dry place")
    assert str(product) == (
        "The product 1 - Arroz with serial number 0 manufactured on 5 by the "
        "company KG valid until 1 must be stored according to the following "
        "instructions: cool dry place."
    )
