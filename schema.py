import graphene
from bitcoin.schema import BitCoinQuery


class Query(BitCoinQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
