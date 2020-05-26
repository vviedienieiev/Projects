import psycopg2
import pandas as pd

CONFIG = {"credentials_path": "PATH_TO_CREDENTIALS"}


class redshift():
    def __init__(self):
        with open(CONFIG["credentials_path"], "r") as f:
            credentials = [x.strip().split(':') for x in f.readlines()]
        self.conn = psycopg2.connect(dbname=credentials[4][1],
                                     host=credentials[2][1],
                                     port=credentials[3][1],
                                     user=credentials[0][1],
                                     password=credentials[1][1])
        self.query = None

    def __del__(self):
        self.conn.close()

    def run_select(self, query):
        self.query = None
        if len(query) == 0:
            raise ValueError("Query shouldn't be empty")
        else:
            try:
                self.query = query
                cur = self.conn.cursor()
                cur.execute(self.query)
                result = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                result = pd.DataFrame(result, columns=colnames)
                return result
            except Exception as e:
                print(e)

    def run_etl(self, query):
        self.query = None
        if len(query) == 0:
            raise ValueError("Query shouldn't be empty")
        else:
            try:
                self.query = query
                cur = self.conn.cursor()
                cur.execute(self.query)
                self.conn.commit()
            except Exception as e:
                print(e)

    def run_insert(self, df, table):
        self.query = None
        if len(df) == 0:
            raise ValueError("DataFrame shouldn't be empty")
        elif len(table) == 0:
            raise ValueError("Please specify table")
        else:
            try:
                self._df_to_into_query(df, table)
                cur = self.conn.cursor()
                cur.execute(self.query)
                self.conn.commit()
            except Exception as e:
                print(e)

    def _df_to_into_query(self, df, table):
        self.query = """Insert into {}  
           Values \n""".format(table)
        for row in range(len(df)):
            self.query += "('{}'),".format("','".join([str(elem) for elem in df.iloc[row, :].to_list()]))
        self.query = self.query[:-1]




