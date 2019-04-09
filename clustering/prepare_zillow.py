import acquire 

def unitcnt (df):
    single_unit = [
        'Condominium',
        ''
    ]

    df = df.drop(df[(df['unitcnt']> 1)].index)
    # df = df.drop(df.filter(regex=['Duplex','Triplex',
    # 'Commercial','Cooperative']).columns, axis=1)
    df = 
    return df


def lat_long_null_values(df):
    df = df[~df.longitude.isnull() | ~df.latitude.isnull()]
    return df

def dropna_fields(df):
    df = df.calculatedfinishedsquarefeet.dropna()