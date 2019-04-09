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

def null_values(df):
        df = df[~df.longitude.isnull() | ~df.latitude.isnull()]
        return df