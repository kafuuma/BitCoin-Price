import requests
from graphql import GraphQLError


def retrieve_bitcoin_price(url):
    try:
        response = requests.get(url)
    except Exception as e:
        raise GraphQLError(str(e))
    if response.status_code == 200:
        return response.json()


def get_dollar_price(data):
    return data['bpi']['USD']['rate_float']
