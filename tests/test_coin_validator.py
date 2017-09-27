from src.coin import Coin
from src.coin_validator import CoinValidator


class TestCoinValidator(object):

    def test_coin_validate_can_identify_a_quarter(self):
        expected_value = .25
        coin = Coin(5.670)
        validator = CoinValidator()
        actual_value = validator.determine_coin(coin)
        assert actual_value == expected_value
