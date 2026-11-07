import mysql.connector

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="#heyyouthere#",
        database="supply_chain",
        port=3305
    )

    if connection.is_connected():
        print("MySQL Database Connected Successfully!")

except mysql.connector.Error as e:
    print("MySQL Connection Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL Connection Closed.")