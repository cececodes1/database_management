import mysql.connector

def add_member(id, name, age):
   
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="hym_admin",
        password="password123",
        database="gym_managment"
    )
    cursor = db.cursor()

    # SQL query to add a new member
    query = """
        INSERT INTO Members (id, name, age)
        VALUES (%s, %s, %s)
    """

    try:
        # Execute the SQL query
        cursor.execute(query, (id, name, age))
        db.commit()
        print(f"Member {name} added successfully!")
    except mysql.connector.Error as e:
        # Handle duplicate IDs or other constraints
        print(f"Error: {e}")
    finally:
        # Close the database connection
        cursor.close()
        db.close()
