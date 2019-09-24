# BitCoin-Price App

[![Build Status](https://travis-ci.org/kafuuma/BitCoin-Price.svg?branch=master)](https://travis-ci.org/kafuuma/BitCoin-Price)

BitCoin-Price App is an application for buying and selling bitcoin

The application is hosted on AWS here [Go](http://ec2-54-80-13-219.compute-1.amazonaws.com/graphiql/)

How the application works

- Request to buy

```
query {
  calculatePrice(margin:0.2, type_:buy, exchangeRate:10){
    price
    success
    errors
  }
}

```

- Request to sell

```
query {
  calculatePrice(margin:0.2, type_:sell, exchangeRate:10){
    price
    success
    errors
  }
}

```

- Inputs

```
- margin is a percentage used in calculation
- type_ : This can either be buy or cell
- exchangeRate :This is a custom USD/NGN exchange rate that will be used in the          calculation detailed below
```

# Project requirements

- Django
- python
- graphene-python
- graphene-django
- Docker
- Docker-compose

## PROJECT SETUP

```
- I have included the requirements file, there is nothing to hide per now

```

- Clone the repository

```
- Create virtualenvironment
python3 -m venv venv

- Install requirements
pip install -r requirements.txt

- Activate environment
source venv/bin/activate

- Make scripts executable
chmode a+x scripts/start.sh
chmode a+x scripts/test.sh

- Start the server
srcipts/start.sh

- Run tests
scripts/test.sh

```

## PROJECT SETUP WITH DOCKER

```
- Install Docker and Docker-compose
- Run Server
  docker-compose -f docker/docker-compose.yml up --build -d
- Run tests
  docker-compose -f docker/docker-compose.yml exec bitcoin scripts/test.sh
```
