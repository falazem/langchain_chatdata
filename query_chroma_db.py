import sqlite3
import pandas as pd

# Path to your Chroma database
db_path = '/Users/lamatalje/Documents/Dev/LangChain_ChatData/langchain_chatdata/docs/chroma/chroma.sqlite3'

# Connect to the database
conn = sqlite3.connect(db_path)

# Get list of all tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
print("=" * 50)
for table in tables:
    print(f"  - {table[0]}")
print("\n")

# Query each table
for table in tables:
    table_name = table[0]
    print(f"\n{'=' * 50}")
    print(f"Table: {table_name}")
    print('=' * 50)
    
    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print(f"\nColumns: {[col[1] for col in columns]}\n")
    
    # Get row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Total rows: {count}\n")
    
    # Get first 10 rows
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10", conn)
        print(f"First 10 rows:")
        print(df.to_string())
    except Exception as e:
        print(f"Error reading table: {e}")
    
    print("\n")

# If you want to see all data from a specific table, uncomment below:
# print("\n" + "=" * 50)
# print("ALL DATA FROM embeddings table:")
# print("=" * 50)
# df_all = pd.read_sql_query("SELECT * FROM embeddings", conn)
# print(df_all.to_string())

# Close connection
conn.close()
print("\nDatabase connection closed.")
