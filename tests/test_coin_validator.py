from src.coin_validator import CoinValidator
from src.model.coin import Coin
from src.model.dime import Dime
from src.model.nickel import Nickel
from src.model.penny import Penny
from src.model.quarter import Quarter


class TestCoinValidator(object):

    def test_coin_validate_can_identify_weight_of_a_quarter(self):
        coin = Coin(5.670, 0.955)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert isinstance(actual_value, Quarter)

    def test_coin_validate_can_measure_diameter_of_quarter(self):
        coin = Coin(5.670, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"

    def test_coin_validate_can_identify_weight_of_a_dime(self):
        coin = Coin(2.268, 0.705)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert isinstance(actual_value, Dime)

    def test_coin_validate_can_identify_diameter_of_a_dime(self):
        coin = Coin(2.268, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"

    def test_coin_validate_can_identify_weight_of_a_nickle(self):
        coin = Coin(5.000, .835)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert isinstance(actual_value, Nickel)

    def test_coin_validate_can_identify_diameter_of_a_nickle(self):
        coin = Coin(5.000, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"

    def test_coin_validate_can_identify_weight_of_a_penny(self):
        coin = Coin(2.5, .75)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert isinstance(actual_value, Penny)

    def test_coin_validate_can_identify_diameter_a_penny(self):
        coin = Coin(2.5, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"

    def test_coin_validate_an_unidentified_coin(self):
        coin = Coin(0.0, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"