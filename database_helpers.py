import os
import sqlalchemy
import pymysql
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top for .env handling
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

def init_connection_engine(): 
    """db connection returns sqlalchemy engine"""
    db_config = {
        "pool_size": 3,
        "max_overflow": 2,
        "pool_timeout": 30,  # 30 seconds
        "pool_recycle": 1800,  # 30 minutes
    }

    if os.environ.get("DB_HOST"):
        return init_tcp_connection_engine(db_config)
    else:
        return init_unix_connection_engine(db_config)


def init_tcp_connection_engine(db_config): 
    """db connection for local network."""

    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")


    # Extract host and port from db_host
    host_args = db_host.split(":")
    db_hostname, db_port = host_args[0], int(host_args[1])

    engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_hostname,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 3306
            database=db_name,  # e.g. "my-database-name"
        ),
        **db_config
    )

    try:
        return engine

    except:
        print("Error while initiating database")


def init_unix_connection_engine(db_config):
    """db connection try for cloudsql, couldnt make it work!!!"""

    db_user = os.getenv["DB_USER"]
    db_pass = os.getenv["DB_PASS"]
    db_name = os.getenv["DB_NAME"]
    db_socket_dir = os.getenv("DB_SOCKET_DIR", "/cloudsql")
    cloud_sql_connection_name = os.getenv["CLOUD_SQL_CONNECTION_NAME"]

    engine = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_socket": "{}/{}".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        ),
        **db_config
    )
    
    try:
        return engine

    except:
        print("Error while initiating database")



def connect(message):
    """Connection to mysql database. returns a sqlalchemy CursorResult object"""
    global engine
    try:
        connection = engine.connect()
   
        result = connection.execute(message)
        


        return result
    
    except:
        engine = init_connection_engine()
        
        return engine.execute(message)

def count(result):
    """return the number of rows in result as integer"""

    return result.rowcount
