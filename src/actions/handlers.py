"""Handlers for HTTP resources for the actions service."""

import json

import falcon

import actions.model as model


class HelloResource(object):
    """Temporary check-if-everything-works resource."""

    def __init__(self, model):
        self._model = model

    def on_get(self, req, resp):
        """Printout a nice message."""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world'
