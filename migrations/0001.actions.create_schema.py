"""Create the schema for the actions service."""

from yoyo import step


step("""
CREATE SCHEMA actions;
""", """
DROP SCHEMA IF EXISTS actions;
""")
