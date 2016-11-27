"""Create the orders table."""

from yoyo import step


__depends__ = ['0001.actions.create_schema']


step("""
CREATE TABLE actions.orders (
    id SERIAL,
    time_ordered TIMESTAMP NOT NULL,
    org_ext_id INTEGER NOT NULL,
    user_ext_id INTEGER NULL,
    items JSON NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_notes TEXT NULL,
    PRIMARY KEY (id)
);""", """
DROP TABLE IF EXISTS actions.orders;
""")
