

query_string = '''
    query{{
        calculatePrice(
            margin:{margin}, type_:{type_},
            exchangeRate:{exchange_rate}){{
            price
            success
            errors
        }}
    }}
'''


api_data = {
    "time": {
        "updated": "Sep 24, 2019 11:12:00 UTC",
        "updatedISO": "2019-09-24T11:12:00+00:00",
        "updateduk": "Sep 24, 2019 at 12:12 BST"
    },
    "disclaimer": "This data was produced from the CoinDesk",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "9,755.1917",
            "description": "United States Dollar",
            "rate_float": 9755.1917
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "7,839.0574",
            "description": "British Pound Sterling",
            "rate_float": 7839.0574
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "8,877.9268",
            "description": "Euro",
            "rate_float": 8877.9268
        }
    }
}
