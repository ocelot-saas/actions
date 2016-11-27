"""Actions service main module."""

from wsgiref import simple_server

import clock
import falcon
import falcon_cors
import sqlalchemy
import startup_migrations

import actions.config as config
import actions.handlers as handlers
import actions.model as model


def debug_error_handler(ex, req, resp, params):
    print(ex)
    raise ex


startup_migrations.migrate(config.DATABASE_URL, config.MIGRATIONS_PATH)


the_clock = clock.Clock()
sql_engine = sqlalchemy.create_engine(config.DATABASE_URL, echo=True)
model = model.Model(the_clock, sql_engine)

orders_resource = handlers.OrdersResource(model)
order_resource = handlers.OrderResource(model)

cors_middleware = falcon_cors.CORS(
    allow_origins_list=config.CLIENTS,
    allow_headers_list=['Authorization', 'Content-Type'],
    allow_all_methods=True).middleware

app = falcon.API(middleware=[cors_middleware])

if config.ENV != 'PROD':
    app.add_error_handler(Exception, handler=debug_error_handler)


app.add_route('/org/{restaurant_id}/orders', orders_resource)
app.add_route('/org/{restaurant_id}/orders/{order_id}', order_resource)


def main():
    """Server entry point."""
    httpd = simple_server.make_server(config.ADDRESS, config.PORT, app)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
