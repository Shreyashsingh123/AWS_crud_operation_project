import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

def connection():   
    try:
        conn = psycopg2.connect(
            host=os.getenv('host'),
            port=os.getenv('port'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')  
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        print("RDS Connection Successful!")
        # print("PostgreSQL Version:", result)
        return conn

    except Exception as e:
        print("Connection Failed!")
        print(e)
connection()