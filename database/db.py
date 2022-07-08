import os
import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        #DATABASE_URL = os.environ['DATABASE_URL']
        #return psycopg2.connect(DATABASE_URL, sslmode='require')
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex