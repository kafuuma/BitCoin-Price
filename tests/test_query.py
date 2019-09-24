import json

from django.test import TestCase
from graphene.test import Client

from unittest.mock import patch
from schema import schema
from .fixtures import query_string, api_data


class BitCoinTestCase(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.sell_data = {
            'margin': 0.2,
            'type_': 'sell',
            'exchange_rate': 10
        }

        self.buy_data = {
            'margin': 0.2,
            'type_': 'buy',
            'exchange_rate': 10
        }

        self.ivalid_data = {
            'margin': -0.2,
            'type_': 'buy',
            'exchange_rate': -10
        }

    def test_query_sell(self):
        response = self.client.execute(
            query_string.format(**self.sell_data)
        )
        self.assertIn('price', json.dumps(response['data']))
        self.assertEqual(
            'success', response['data']['calculatePrice']['success'])

    def test_query_buy(self):
        response = self.client.execute(
            query_string.format(**self.buy_data)
        )
        self.assertIn('price', json.dumps(response['data']))
        self.assertEqual(
            'success', response['data']['calculatePrice']['success'])

    def test_invalid_input(self):
        response = self.client.execute(
            query_string.format(**self.ivalid_data)
        )
        self.assertIn(
            'margin value should be between 0 and 1',
            response['data']['calculatePrice']['errors'])
        self.assertIn(
            'exchage rate cannot be negative',
            response['data']['calculatePrice']['errors'])

    def test_retrieve_bitcoin_price(self):
        api_response = json.dumps(api_data)
        with patch(
                'bitcoin.utils.retrieve_bitcoin_price'
        ) as mock_retrieve_bitcoin_price:
            mock_retrieve_bitcoin_price('fake_url')
            mock_retrieve_bitcoin_price.return_value = api_response
            self.assertTrue(mock_retrieve_bitcoin_price)
