##########################################
## WILL NEED TO PIPE ALL THESE FUNCTIONS##
##########################################

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

def get_2017_zillow():
    idb = "zillow"
    query = ('\
    SELECT p17.*, pred17.logerror, act.airconditioningdesc, ast.architecturalstyledesc, \
        bct.buildingclassdesc, hst.heatingorsystemdesc, plut.propertylandusedesc, \
        st.storydesc, tct.typeconstructiondesc FROM properties_2017 p17 \
    JOIN predictions_2017 pred17 \
                       ON pred17.parcelid = p17.parcelid \
    LEFT JOIN airconditioningtype act \
                       ON p17.airconditioningtypeid = act.airconditioningtypeid\
    LEFT JOIN architecturalstyletype ast \
                       ON p17.architecturalstyletypeid = ast.architecturalstyletypeid\
    LEFT JOIN buildingclasstype bct \
                       ON p17.buildingclasstypeid = bct.buildingclasstypeid\
    LEFT JOIN heatingorsystemtype hst \
                       ON p17.heatingorsystemtypeid = hst.heatingorsystemtypeid\
    LEFT JOIN propertylandusetype plut \
                       ON p17.propertylandusetypeid = plut.propertylandusetypeid\
    LEFT JOIN storytype st \
                       ON p17.storytypeid = st.storytypeid\
    LEFT JOIN typeconstructiontype tct \
                       ON p17.typeconstructiontypeid = tct.typeconstructiontypeid;')

    url = get_db_url(host, user, password, idb)
    return df_from_sql(query, url)

def merge_dfs():
    df16 = get_2016_zillow()
    df17 = get_2017_zillow()
    df = pd.concat([df16, df17])
    return df

def turn_to_csv():
    df = merge_dfs()
    df.to_csv('zillow_16_17.csv', sep='\t', index=False)

def drop_columns(df):
    df = df.drop(columns=(['id',
        'airconditioningtypeid',  
        'architecturalstyletypeid',
        'buildingclasstypeid', 
        'buildingqualitytypeid',
        'decktypeid', 
        'heatingorsystemtypeid', 
        'propertylandusetypeid',
        'storytypeid', 
        'typeconstructiontypeid']))
    
    return df

def reindex_df (df):
    df = df.reindex(columns=[
        'parcelid','logerror',
        'bathroomcnt','bedroomcnt','calculatedbathnbr','fullbathcnt','roomcnt',
        'calculatedfinishedsquarefeet','lotsizesquarefeet',  
        'unitcnt','propertylandusedesc','propertycountylandusecode','propertyzoningdesc',
        'latitude','longitude','regionidcity','regionidcounty','fips','regionidneighborhood','regionidzip',
        'yearbuilt',
        'structuretaxvaluedollarcnt','taxvaluedollarcnt','landtaxvaluedollarcnt','taxamount','assessmentyear',
        'rawcensustractandblock','censustractandblock',
        'airconditioningdesc','heatingorsystemdesc',
        'garagecarcnt','garagetotalsqft',
        'basementsqft',
        'finishedfloor1squarefeet','finishedsquarefeet12','finishedsquarefeet13',
        'finishedsquarefeet15','finishedsquarefeet50','finishedsquarefeet6',
        'fireplacecnt','hashottuborspa',
        'poolcnt','poolsizesum','pooltypeid10','pooltypeid2','pooltypeid7',
        'threequarterbathnbr',
        'yardbuildingsqft17','yardbuildingsqft26',
        'fireplaceflag',
        'taxdelinquencyflag','taxdelinquencyyear',
        'architecturalstyledesc',
        'buildingclassdesc',
        'numberofstories',
        'storydesc',
        'typeconstructiondesc',
    ])
    return df

