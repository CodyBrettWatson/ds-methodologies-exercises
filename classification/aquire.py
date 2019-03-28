import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    return pd.read_sql('''SELECT sp.species_name, ms.* FROM species sp
	    JOIN measurements ms
        ON sp.species_id = ms.species_id;''', get_connection('iris_db'))
