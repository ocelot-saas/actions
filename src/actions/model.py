"""Model actions for the actions service."""

import datetime


import sqlalchemy as sql
import sqlalchemy.dialects.postgresql as postgresql


_metadata = sql.MetaData(schema='actions')

_order = sql.Table(
    'order', _metadata,
    sql.Column('id', sql.Integer, primary_key=True, info={'export': True}),
    sql.Column('time_ordered', sql.DateTime(timezone=True), info={'export': True}),
    sql.Column('org_ext_id', sql.Integer, info={'export': True}),
    sql.Column('user_ext_id', sql.Integer, nullable=True, info={'export': True}),
    sql.Column('items', postgresql.JSON(), info={'export': True}),
    sql.Column('delivery_address', sql.Text(), info={'export': True}),
    sql.Column('delivery_notes', sql.Text(), info={'export': True}))


def _ec(t):
    return [c for c in t.c if 'export' in c.info and c.info['export']]


_order_columns = _ec(_order)


class Error(Exception):
    pass


class Model(object):
    def __init__(self, the_clock, sql_engine):
        self._the_clock = the_clock
        self._sql_engine = sql_engine

    def create_order(self, items, delivery_address, delivery_notes):
        pass

    def get_orders(self):
        pass

    def get_order(self, order_id):
        pass

    def update_order(self, order_id, **kwargs):
        pass
