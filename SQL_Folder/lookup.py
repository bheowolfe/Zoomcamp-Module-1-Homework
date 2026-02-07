import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click


def ingest_csv_data(
        engine,
        target_table: str,
) -> pd.DataFrame:
    df = pd.read_csv(
        "/data/taxi_zone_lookup.csv",
    )

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="replace"
    )

    print(f"Table {target_table} created")


def ingest_parquet_data(
        engine,
        target_table: str,
) -> pd.DataFrame:
    df = pd.read_parquet(
        "/data/green_tripdata_2025-11.parquet"
    )

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="replace"
    )

    print(f"Table {target_table} created")


@click.command()
@click.option('--pg-user', default='root', show_default=True, help='Postgres user')
@click.option('--pg-pass', default='root', show_default=True, help='Postgres password')
@click.option('--pg-host', default='localhost', show_default=True, help='Postgres host')
@click.option('--pg-port', default=5432, show_default=True, type=int, help='Postgres port')
@click.option('--pg-db', default='ny_taxi', show_default=True, help='Postgres database')
@click.option('--target-csv-table', default='taxi_zone', show_default=True, help='Target DB table')
@click.option('--target-parquet-table', default='tripdata', show_default=True, help='Target DB table')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, target_csv_table, target_parquet_table):
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    ingest_csv_data(
        engine=engine,
        target_table=target_csv_table,
    )

    ingest_parquet_data(
        engine=engine,
        target_table=target_parquet_table,
    )

if __name__ == '__main__':
    main()