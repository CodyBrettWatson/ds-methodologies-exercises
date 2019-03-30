# import aquire
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler


# ###Titanic_DB
# def handle_missing_values_titanic(df):
#     return df.assign(
#         embark_town = df.embark_town.fillna('Other'),
#         embarked = df.embarked.fillna('O'))

# def drop_columns_titanic(df):
#     return df.drop(columns='deck')

# def encode_embarked_titanic(df):
#     encoder = LabelEncoder()
#     encoder.fit(df.embarked)
#     return df.assign(embarked_encode = encoder.transform(df.embarked))

# def prep_titanic_data(df):
#     return df.pipe(handle_missing_values_titanic)\
#         .pipe(drop_columns_titanic)\
#         .pipe(encode_embarked_titanic)

# def split_titanic (df):
#     train, test = train_test_split(df, test_size=.30, random_state=123, stratify=df[['survived']])
#     return train, test


# def scale_min_max_titanic(df):
#     scaler = MinMaxScaler()
#     scaler.fit(train[['fare','age']])
#     df[['age','fare']]=scaler.transform(train[['age','fare']])
#     return df, scaler

# def prep_titanic(df):
#     train,test = prep_titanic_data(df)
#     train, scaler = scale_min_max_titanic(train)
#     train[['fare','age']] = scaler.transform(train[['fare','age']])
#     test[['fare','age']] = scaler.transform(test[['fare','age']])
#     return train, test


# ###Iris_DB
# def drop_columns_iris(idf):
#     return idf.drop(['species_id','measurement_id'], axis=1)

# def encode_species_iris(idf):
#     encoder = LabelEncoder()
#     encoder.fit(idf.species)
#     return idf.assign(species_encode = encoder.transform(idf.species))

# def prep_iris_data(idf):
#     return idf.pipe(drop_columns_iris)\
#         .pipe(encode_species_iris)

# def split_iris (idf):
#     train, test = train_test_split(idf, test_size=.30, random_state=123)
#     return train, test


# def scale_min_max_iris(idf):
#     scaler = MinMaxScaler()
#     scaler.fit(train[['sepal_length','sepal_width']])
#     idf[['sepal_width','sepal_length']]=scaler.transform(train[['sepal_width','sepal_length']])
#     return idf, scaler

# def prep_iris(idf):
#     train,test = prep_iris_data(idf)
#     train, scaler = scale_min_max_iris(train)
#     train[['sepal_length','sepal_width']] = scaler.transform(train[['sepal_length','sepal_width']])
#     test[['sepal_length','sepal_width']] = scaler.transform(test[['sepal_length','sepal_width']])
#     return train, test


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def prep_iris(df_iris):
    df = df_iris.copy()
    
    df = df.drop(columns=["species_id", "measurement_id"])
    
    df = df.rename(index=str, columns={"species_name": "species"})
    
    encoder = LabelEncoder()
    encoder.fit(df.species)
    df = df.assign(species_encode=encoder.transform(df.species))

    return df

# def split (df_iris):
#         train, test = train_test_split(df_iris, train_size=0.7, random_state=123, stratify=df_iris[["species"]])
#         return train, test



def prep_titanic(df_titanic):
    df = df_titanic.copy()
    
    df.embarked = df.embarked.fillna("U")
    df.embark_town = df.embark_town.fillna("Unknown")
    
    df = df.drop(columns="deck")
    
    encoder = LabelEncoder()
    encoder.fit(df.embarked)
    df = df.assign(embarked_encode=encoder.transform(df.embarked))
    
    df = df.dropna()
    
    # the scaling should be done after the train/test split
    scaler = MinMaxScaler()
    df[["age", "fare"]] = scaler.fit_transform(df[["age", "fare"]])
    
    train, test = train_test_split(df, train_size=0.7, random_state=123, stratify=df[["survived"]])
    
    return df