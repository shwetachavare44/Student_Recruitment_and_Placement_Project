import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Alpha@123",   
        database="student_placement_system" 
    )      

    if connection.is_connected():
        print("✅ Database Connected Successfully!")

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database Connection Closed")