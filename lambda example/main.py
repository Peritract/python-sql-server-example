"""A small example of connecting to a SQL server database using pyodbc."""

from os import environ as ENV

from dotenv import load_dotenv
import pyodbc


def handler(event=None, context=None):
    conn_str = (f"DRIVER={{{ENV['DB_DRIVER']}}};SERVER={ENV['DB_HOST']};"
                f"PORT={ENV['DB_PORT']};DATABASE={ENV['DB_NAME']};"
                f"UID={ENV['DB_USERNAME']};PWD={ENV['DB_PASSWORD']};Encrypt=no;")

    conn = pyodbc.connect(conn_str)

    with conn.cursor() as cur:
        q = "SELECT table_name, table_schema FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';"
        cur.execute(q)
        data = cur.fetchone()

    conn.close()

    return list(data)


if __name__ == "__main__":
    load_dotenv()
    print(handler())