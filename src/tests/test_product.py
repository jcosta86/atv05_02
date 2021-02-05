import pytest

from src.models.product import Product, BaseModel


class TestProduct:
    @pytest.fixture
    def my_product(self):
        product = Product("nome valido", "description valida", 10.32)
        return product

    def test_product_instance(self, my_product):
        product = my_product
        assert isinstance(product, BaseModel)
        assert isinstance(product, Product)
    
    @pytest.mark.parametrize("name", [10, 52.76, float('inf'), True])
    def test_name_must_be_string(self, name):
        with pytest.raises(TypeError) as e:
            product = Product(name, "description", 10)

    @pytest.mark.parametrize("description", [10, 52.76, float('inf'), True])
    def test_description_must_be_string(self, description):
        with pytest.raises(TypeError) as e:
            product = Product("name ", description, 10)

    @pytest.mark.parametrize("price", [10, "banana", True])
    def test_price_must_be_float(self, price):
        with pytest.raises(TypeError) as e:
            product = Product("name ", "description", price)


    def test_name_too_large(self):
        with pytest.raises(ValueError):
            product = Product("b"*100, "description", 10.2)

    def test_description_too_large(self):
        with pytest.raises(ValueError):
            product = Product("name", "b"*600, 10.3)



    def test_product_description(self):
        pass

    def test_product_price(self):
        pass
