import graphene
import bitcoin.utils


class CurrentBitCoinPriceType(graphene.ObjectType):
    price = graphene.Float()
    success = graphene.String()
    error = graphene.String()


class BitCoinQuery(graphene.ObjectType):
    calculate_price = graphene.Field(CurrentBitCoinPriceType,
                                     type_=graphene.String(required=True),
                                     margin=graphene.Float(required=True),
                                     exchange_rate=graphene.Float(
                                         required=True)
                                     )

    def resolve_calculate_price(self, info, **kwargs):

        margin = kwargs.get('margin')
        type_ = kwargs.get('type_')
        exchange_rate = kwargs.get('exchange_rate')

        bitcoin_data = bitcoin.utils.retrieve_bitcoin_price(
            url='https://api.coindesk.com/v1/bpi/currentprice.json')
        price = bitcoin.utils.get_dollar_price(bitcoin_data)

        if type_ == 'buy':
            computed_value = price + price * (float(margin)/100)

        elif type_ == 'sell':
            computed_value = price - price * (float(margin)/100)

        price_in_naira = computed_value * float(exchange_rate)

        return CurrentBitCoinPriceType(price=price_in_naira, success="could not connect to server")
