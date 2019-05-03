# import pandas as pd
# import env

# def get_connection(db, user=env.user, host=env.host, password=env.password):
#     return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# def get_titanic_data():
#     return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

# def get_iris_data():
#     return pd.read_sql('''SELECT sp.species_name, ms.* FROM species sp
# 	    JOIN measurements ms
#         ON sp.species_id = ms.species_id;''', get_connection('iris_db'))


# Getting data from SQL databases
from env import host, user, password
import pandas as pd
from sqlalchemy import create_engine

def get_db_url(
    host: str, user: str, password: str, db_name: str
) -> str:
    """
    return url for accessing a mysql database
    """
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"


def get_sql_conn(host: str, user: str, password: str, db_name: str):
    """
    return a mysql connection object
    """
    return create_engine(get_db_url(host, user, password, db_name))


def df_from_sql(query: str, url: str) -> pd.DataFrame:
    """
    return a Pandas DataFrame resulting from a sql query
    """
    return pd.read_sql(query, url)

def get_titanic_data() -> pd.DataFrame:
    tdb = "titanic_db"
    query = ("SELECT * "
             "FROM passengers;")
    url = get_db_url(host, user, password, tdb)
    return df_from_sql(query, url)

def get_iris_data() -> pd.DataFrame:
    idb = "iris_db"
    query = ("SELECT * "
             "FROM measurements "
             "JOIN species USING(species_id);")
    url = get_db_url(host, user, password, idb)
    return df_from_sql(query, url)