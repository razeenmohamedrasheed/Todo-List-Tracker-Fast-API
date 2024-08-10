import psycopg2

class DButils:
    def __init__(self):
        self.conn = psycopg2.connect(
            # dbname="collegeManagement",
            database="todoApp",
            user='postgres',
            password='Admin',
            host="127.0.0.1",
            port=5432
        )

    def select_query(self, table):
        try:
            cursor = self.conn.cursor()
            query = f"""SELECT * FROM {table}"""
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            cursor.close()
            result = [dict(zip(columns, row)) for row in rows]
            return result
        except Exception as e:
            print(e)
            raise e

    def insert_query(self, table, columns, values, auto_commit=True):
        cursor = self.conn.cursor()
        try:
            columns_str = ', '.join(columns)
            placeholders = ', '.join(['%s'] * len(values))
            query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
            cursor.execute(query, values)
            if auto_commit:
                self.conn.commit()
                # Close the cursor
            cursor.close()
        except Exception as e:
            raise

    def execute_query(self, query, required=False):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            if required:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                cursor.close()
                result = [dict(zip(columns, row)) for row in rows]
                return result
            cursor.close()
        except Exception as e:
            print(e)
            raise e
