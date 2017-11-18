from src.coin import Coin
from src.coin_validator import CoinValidator
from src.model.product import Product
from src.vending_machine import VendingMachine


def main():
    coke = Product('Coke', 1.00)
    validator = CoinValidator()
    vending_machine = VendingMachine(coke, validator, coke.price)

    coin = Coin(5.670)

    vending_machine.insert_coins(coin)
    print(vending_machine.DISPLAY)
    vending_machine.insert_coins(coin)
    vending_machine.insert_coins(coin)
    print(vending_machine.DISPLAY)
    vending_machine.insert_coins(coin)
    print(vending_machine.DISPLAY)

if __name__ == '__main__':
    main()
