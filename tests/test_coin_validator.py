from src.coin_validator import CoinValidator
from src.model.coin import Coin
from src.model.quarter import Quarter


class TestCoinValidator(object):

    def test_coin_validate_can_identify_a_quarter(self):
        coin = Coin(5.670, 0.955)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert isinstance(actual_value, Quarter)

    def test_coin_validate_can_measure_diameter_of_quarter(self):
        coin = Coin(5.670, 0.0)
        validator = CoinValidator()
        actual_value = validator.calculate_coin(coin)
        assert actual_value == "UnIdentified Coin"

    def test_coin_validate_can_identify_a_dime(self):
        expected_value = .10
        coin = Coin(2.268)
        validator = CoinValidator()
        actual_value = validator.determine_coin(coin)
        assert actual_value == expected_value

    def test_coin_validate_can_identify_a_nickle(self):
        expected_value = .05
        coin = Coin(5.000)
        validator = CoinValidator()
        actual_value = validator.determine_coin(coin)
        assert actual_value == expected_value

    def test_coin_validate_can_identify_a_penny(self):
        expected_response = .01
        coin = Coin(2.5)
        validator = CoinValidator()
        actual_value = validator.determine_coin(coin)
        assert actual_value == expected_response
