
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

def get_zillow_data() -> pd.DataFrame:
    idb = "zillow"
    query = ("SELECT * "
             "FROM properties_2016 "
             "JOIN properties_2017 USING(parcelid);")
    url = get_db_url(host, user, password, idb)
    return df_from_sql(query, url)


def get_2016_zillow():
    idb = "zillow"
    query = ('\
    SELECT p16.*, pred16.logerror, act.airconditioningdesc, ast.architecturalstyledesc, \
        bct.buildingclassdesc, hst.heatingorsystemdesc, plut.propertylandusedesc, \
        st.storydesc, tct.typeconstructiondesc FROM properties_2016 p16 \
    JOIN predictions_2016 pred16 \
                       ON pred16.parcelid = p16.parcelid \
    LEFT JOIN airconditioningtype act \
                       ON p16.airconditioningtypeid = act.airconditioningtypeid\
    LEFT JOIN architecturalstyletype ast \
                       ON p16.architecturalstyletypeid = ast.architecturalstyletypeid\
    LEFT JOIN buildingclasstype bct \
                       ON p16.buildingclasstypeid = bct.buildingclasstypeid\
    LEFT JOIN heatingorsystemtype hst \
                       ON p16.heatingorsystemtypeid = hst.heatingorsystemtypeid\
    LEFT JOIN propertylandusetype plut \
                       ON p16.propertylandusetypeid = plut.propertylandusetypeid\
    LEFT JOIN storytype st \
                       ON p16.storytypeid = st.storytypeid\
    LEFT JOIN typeconstructiontype tct \
                       ON p16.typeconstructiontypeid = tct.typeconstructiontypeid;')

    url = get_db_url(host, user, password, idb)
    return df_from_sql(query, url)