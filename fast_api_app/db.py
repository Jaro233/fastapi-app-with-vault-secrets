import os
import hvac
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_credentials_from_vault():
    # Establish a connection with Vault
    client = hvac.Client(url=os.getenv('VAULT_ADDR'), token=os.getenv('VAULT_TOKEN'))
    
    
    # Read secrets from Vault
    read_response = client.secrets.kv.v2.read_secret_version(path='secret/db_creds', mount_point='kv')
    return read_response['data']['data']

def db_conn():
    try:
        # Fetch credentials from Vault
        credentials = get_db_credentials_from_vault()

        # Connect to an existing database
        conn = psycopg2.connect(
            host=credentials["host"],
            dbname=credentials["database"],
            user=credentials["user"],
            password=credentials["password"],
            port=credentials["port"],
            cursor_factory=RealDictCursor,
        )
        
        print("Database connected")
        return conn.cursor()
    except Exception as error:
        print("Connecting to database unsuccessful")
        print("Error:", error)
        raise
