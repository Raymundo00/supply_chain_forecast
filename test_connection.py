from src.db_connection import connect_to_db

connection = connect_to_db()

if connection:
    connection.close()
    print("✅ Connection closed.")
else:
    print("❌ Could not establish connection.")