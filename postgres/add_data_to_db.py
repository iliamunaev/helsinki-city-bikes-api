import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def add_data_to_db(file, t_name, engine):
    try:
        data = pd.read_csv(file)
        data.to_sql(t_name, con=engine, index=False, if_exists='replace')
        print(f'Added data from {file} to {t_name} table')
    except pd.errors.ParserError as e:
        print(f"Error reading {file}: {e}")
    except SQLAlchemyError as e:
        print(f"Error writing to database: {e}")


if __name__ == '__main__':
    csv_files = ['data/trips.csv', 'data/stations.csv']
    table_names = ['trips', 'stations']
    engine = create_engine("postgresql://postgres:postgres@localhost/helsinkibikes")

    for file, t_name in zip(csv_files, table_names):
        add_data_to_db(file, t_name, engine)
