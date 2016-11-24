"""Model actions for the actions service."""

import datetime


import sqlalchemy as sql
import sqlalchemy.dialects.postgresql as postgresql


_metadata = sql.MetaData(schema='actions')


class Error(Exception):
    pass


class Model(object):
    def __init__(self, the_clock, sql_engine):
        self._the_clock = the_clock
        self._sql_engine = sql_engine
