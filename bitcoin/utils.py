import requests
from graphql import GraphQLError


def retrieve_bitcoin_price(url):
    """
    This function retrieves bitcoin prices from an external api

    Argument:
        url(string): url for external api

    Returns:
        bitcoin data (json object): contains prices for bitcoin
        in USD, EUR etc.

    Raises:
        GraphQL error if the server cannot connect to external api
        or status code returned is not 200
    """
    try:
        response = requests.get(url)
    except Exception as e:
        raise GraphQLError(str(e))
    if response.status_code != 200:
        raise GraphQLError(str(response.reason))
    return response.json()


def get_dollar_price(data):
    """
    This function retrieves a USD price of bitcoin from data
    returned by external api

    Arguement:
        bitcoin data(json data):

    Returns:
        bitcoin price in USD(float)
    """
    return data['bpi']['USD']['rate_float']


def validate_input(margin, exchange_rate):
    error = []
    if float(margin) < 0 or float(margin) > 1:
        error.append('margin value should be between 0 and 1')
    if float(exchange_rate) < 0:
        error.append('exchage rate cannot be negative')
    return error
