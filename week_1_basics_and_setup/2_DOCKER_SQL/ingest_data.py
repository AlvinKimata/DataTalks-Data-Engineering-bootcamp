#!/usr/bin/env python
# coding: utf-8

import os
import argparse 
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    host = params.host
    user = params.user
    url = params.parquet_url
    password = params.password
    table_name = params.table_name
    port_number = params.port_number
    database_name = params.database_name

    parquet_name = 'yellow_tripdata_2021-01.parquet'
    os.system(f'wget {url} -O {parquet_name}')
    
    df = pd.read_parquet(parquet_name)

    #Convert object dtypes to datetime dtypes.
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    #Create a connection to postgres database.
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port_number}/{database_name}')


    #Create table.
    df.head(n = 0).to_sql(name = table_name, con = engine, if_exists = 'replace')


    #Write records to the created tables.
    df.to_sql(name = table_name, con = engine, if_exists = 'append')



if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Ingest CSV data to postgres database.')
    '''
    Parameters passed to argument parser are:
    1. User
    2. Password
    3. Host
    4. Port number
    5. Database name
    6. Table name
    7. URL of the CSV file.
    '''
    parser.add_argument('--user', help = 'Username for postgres')
    parser.add_argument('--password', help='Password for postgres database')
    parser.add_argument('--host', help='Host name for postgres database')
    parser.add_argument('--database_name', help = 'Database name for postgres')
    parser.add_argument('--table_name', help = 'Name of table where we will write the results to.')
    parser.add_argument('--port_number', help = 'Port number of the database')
    parser.add_argument('--parquet_url', help='URL for the parquet file.')

    args = parser.parse_args()

    main(args)





