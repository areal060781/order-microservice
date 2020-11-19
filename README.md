# Order Microservice
Django 3.2.10, the administration UI and the Django data model

A microservice that is responsible for receiving orders from the web application. The order microservice also provides 
other features such as the ability to update the status of orders and provide order information using different criteria

* basics on microservices
* how to create Django REST Framework to create RESTful APIs
* how to consume the services and integrate the with other applications
* how to write test
* deploy and application on AWS

### Requirements
* Python 3.8
* Pipenv

## Setup

### Installation
Install Python dependencies
```sh
pipenv install --dev
```

Install Npm dependencies
```sh
npm install
```

Run the migrations
```
(order-microservice) $ python manage.py migrate
```

Run the application as usual
```shell
(order-microservice) $ python manage.py runserver
```