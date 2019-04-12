##########################################
## WILL NEED TO PIPE ALL THESE FUNCTIONS##
##########################################

import acquire
import pandas as pd

## Function By Orion
def unitcnt (df):
    single_unit = [
        'Condominium',
        'Single Family Residential',
        'Mobile Home',
        'Townhouse',
        'Residential General',
        'Manufactured, Modular, Prefabricated Homes'
    ]
    df = df[df.propertylandusedesc.isin(single_unit)]

    df = df.drop(df[(df['unitcnt']> 1)].index)
    df = df.drop(df[(df['regionidzip']> 99999)].index)
    # df = df.drop(df.filter(regex=['Duplex','Triplex',
    # 'Commercial','Cooperative']).columns, axis=1)
    
    return df

## Function By Orion
def lat_long_null_values(df):
    df = df[~df.longitude.isnull() | ~df.latitude.isnull()]
    return df

def dropna_fields(df):
    df = df.dropna(subset=['calculatedfinishedsquarefeet','unitcnt'])
    return df


def field_temp_drop(df):
    df = df.drop(columns=([
        ## almost 100% nulls
        'garagecarcnt',
        'garagetotalsqft',
        'basementsqft',
        'finishedfloor1squarefeet',
        'finishedsquarefeet12',
        'finishedsquarefeet13',
        'finishedsquarefeet15',
        'finishedsquarefeet50',
        'finishedsquarefeet6',
        'fireplacecnt',
        'hashottuborspa',
        'poolcnt',
        'poolsizesum',
        'pooltypeid10',
        'pooltypeid2',
        'pooltypeid7',
        'threequarterbathnbr',
        'yardbuildingsqft17',
        'yardbuildingsqft26',
        'numberofstories',
        'fireplaceflag',
        'taxdelinquencyflag',
        'taxdelinquencyyear',
        'architecturalstyledesc',
        'buildingclassdesc',
        'storydesc',
        'typeconstructiondesc',

        ## around 50k nulls
        'regionidneighborhood',
        'airconditioningdesc',
        
        ## contains strings 
        'unitcnt',
        'propertylandusedesc',
        'propertycountylandusecode', 
        'propertyzoningdesc', 
        'heatingorsystemdesc',

        ## erroneous
        'roomcnt',
        'calculatedbathnbr',
        'fullbathcnt',
        'fips',

        ## made erroneous by previous data prep when removing null values from unitcnt
        'regionidcounty'
    ]))
    
    return df

def drop_null (df):
    df = df.dropna(subset=[
        'calculatedfinishedsquarefeet'])
    df = df.drop(df[
        (df['calculatedfinishedsquarefeet']<= 200)].index)
    df = df.drop(df[
        (df['bedroomcnt']<= 0)].index)
    df = df.drop(df[
        (df['bathroomcnt']<= 0)].index)

    return df

def convert_col_type(df):
    obj_fields = list(df.select_dtypes(include='object'))
    df[obj_fields] = df[obj_fields].convert_objects(convert_numeric=True)

    return df


##Function By DD
def check_missing_values_col(df):
    '''
    Write or use a previously written function to return the
    total missing values and the percent missing values by column.
    '''
    null_count = df.isnull().sum()
    null_percentage = (null_count / df.shape[0]) * 100
    empty_count = pd.Series(((df == ' ') | (df == '')).sum())
    empty_percentage = (empty_count / df.shape[0]) * 100
    nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
    nan_percentage = (nan_count / df.shape[0]) * 100
    return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
                         'num_empty': empty_count, 'empty_percentage': empty_percentage,
                         'nan_count': nan_count, 'nan_percentage': nan_percentage})



###Function By Michael
def numeric_to_categorical(df: pd.DataFrame, cols: tuple) -> pd.DataFrame:
    to_coerce = {col: "category" for col in cols}
    return df.astype(to_coerce)



######################
##WORK ON THIS LATER##
######################
# col = ['bathroomcnt','bedroomcnt',
#        'calculatedfinishedsquarefeet',
#        'lotsizesquarefeet','taxvaluedollarcnt',
#        'landtaxvaluedollarcnt', 'taxamount',
#       ]

# q = df[col].quantile(0.99)
# pdf = df[df[col] < q]
# pdf.T

# # from scipy import stats
# # pdf = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]