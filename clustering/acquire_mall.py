import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_mall_customers():
    return pd.read_sql('SELECT * FROM customers', 
    get_connection('mall_customers'))