import psycopg

def get_connection():
    return psycopg.connect(
        host="172.22.96.1",
        port=5432,
        dbname="ml_database",
        user="postgres",
        password="mohsinkazimohsin"
    )
