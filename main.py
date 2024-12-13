import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # Read connection parameters
        params = config()
        print(f"Connection parameters: {params}")  # Debugging line

        # Ensure password is present
        if "password" not in params or not params["password"]:
            raise ValueError("Database password is missing in the configuration.")

        # Connect to the PostgreSQL server
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**params)
        print("Connection established.")
        return connection
    except Exception as error:
        print(f"Error: {error}")
        raise  # Reraise the exception to handle it in the calling code
