"""Handlers for HTTP resources for the actions service."""

import json

import falcon

import actions.model as model


class OrdersResource(object):
    """Temporary check-if-everything-works resource."""

    def __init__(self, model):
        self._model = model

    def on_post(self, req, resp, restaurant_id):
        """Create a new order."""
        resp.status = falcon.HTTP_201
        resp.body = 'Hello world'

    def on_get(self, req, resp, restaurant_id):
        """Retrieve all the orders."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'


class OrderResource(object):
    """Temporary check-if-everything-works resource."""

    def __init__(self, model):
        self._model = model

    def on_get(self, req, resp, restaurant_id, order_id):
        """Retrieve all the orders."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'

    def on_put(self, req, resp, restaurant_id, order_id):
        """Create a new order."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'
