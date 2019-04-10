##########################################
## WILL NEED TO PIPE ALL THESE FUNCTIONS##
##########################################

import acquire 

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
    # df = df.drop(df.filter(regex=['Duplex','Triplex',
    # 'Commercial','Cooperative']).columns, axis=1)
    
    return df


def lat_long_null_values(df):
    df = df[~df.longitude.isnull() | ~df.latitude.isnull()]
    return df

def dropna_fields(df):
    df = df.dropna(subset=['calculatedfinishedsquarefeet','unitcnt'])
    return df


def field_temp_drop(df):
    df = df.drop(columns=([
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
        'typeconstructiondesc'
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