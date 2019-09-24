import graphene
import bitcoin.utils
from django.conf import settings


BITCOIN_URL = settings.BITCOIN_URL


class typeEnum(graphene.Enum):
    buy = 'buy'
    sell = 'sell'


class CurrentBitCoinPriceType(graphene.ObjectType):
    """Custom object model to be returned"""
    price = graphene.Float()
    success = graphene.String()
    errors = graphene.List(graphene.String)


class BitCoinQuery(graphene.ObjectType):
    """Querry to handle requests for bitcoin pricess"""
    calculate_price = graphene.Field(CurrentBitCoinPriceType,
                                     type_=graphene.Argument(
                                         typeEnum, required=True),
                                     margin=graphene.Float(required=True),
                                     exchange_rate=graphene.Float(
                                         required=True)
                                     )

    def resolve_calculate_price(self, info, **kwargs):
        """
        Resolver method for bitcoing price
        Returns:
             CurrentBitCoinPriceType(Object)
        """

        margin = kwargs.get('margin')
        type_ = kwargs.get('type_')
        exchange_rate = kwargs.get('exchange_rate')

        errors = bitcoin.utils.validate_input(margin, exchange_rate)
        if errors:
            return CurrentBitCoinPriceType(errors=errors)

        bitcoin_data = bitcoin.utils.retrieve_bitcoin_price(
            url=BITCOIN_URL)
        price = bitcoin.utils.get_dollar_price(bitcoin_data)

        if type_ == 'buy':
            computed_value = price + price * (float(margin)/100)
        elif type_ == 'sell':
            computed_value = price - price * (float(margin)/100)

        price_in_naira = computed_value * float(exchange_rate)

        return CurrentBitCoinPriceType(price=price_in_naira, success="success")
