"""Handlers for HTTP resources for the actions service."""

import json

import falcon
import inventory_sdk

import actions.model as model


class OrdersResource(object):
    """Orders resouce"""

    def __init__(self, id_validator, order_creation_request_validator, orders_response_validator, inventory_client, model):
        self._id_validator = id_validator
        self._order_creation_request_validator = order_creation_request_validator
        self._orders_response_validator = orders_response_validator
        self._inventory_client = inventory_client
        self._model = model

    def on_post(self, req, resp, org_id_raw, restaurant_id_raw):
        """Create a new order."""

        # Parse and process direct input from the request.
        try:
            org_id = self._id_validator.validate(org_id_raw)
            restaurant_id = self._id_validator.validate(restaurant_id_raw)
            order_creation_request_raw = req.stream().read().decode('utf-8')
            order_creation_request = \
                self._order_creation_request_validator.validate(order_creation_request_raw)
        except validation.Error as e:
            raise falcon.HTTPBadRequest(
                title='Invalid order creation data',
                description='Invalid order creation data') from e

        # Retrieve information about the restaurant for which the order is placed.
        try:
            org, restaurant = self._inventory_client.get_org_and_restaurant(org_id, restaurant_id)
        except inventory_sdk.Error as e:
            raise falcon.HTTPBadGateway(
                title='Cannot retrieve data from inventory service',
                description='Could not retrieve data from inventory service') from e

        # Retrieve information about the user which has placed the order, if any.
        # TODO(horia141)

        try:
            order = self._model.create_order(org, restaurant, order_creation_request['items'],
                order_creation_request['delivery_address'], order_creation_request['delivery_notes'])
        except model.Error as e:
            raise falcon.HTTPInternalServerError(
                title='Error while inserting the order',
                description='Error while inserting the order') from e

        response = {'orders': [order]}

        self._orders_response_validator.validate(response)
                
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(response)

    def on_get(self, req, resp, restaurant_id):
        """Retrieve all the orders."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'


class OrderResource(object):
    """Temporary check-if-everything-works resource."""

    def __init__(self, model):
        self._model = model

    def on_get(self, req, resp, org_id, restaurant_id, order_id):
        """Retrieve all the orders."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'

    def on_put(self, req, resp, org_id, restaurant_id, order_id):
        """Create a new order."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'
