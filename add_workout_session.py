import mysql.connector
from datetime import datetime

def add_workout_session(member_id, date, duration_minutes, calories_burned):
  
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="gym_admin",
        password="password123",
        database="gym_management"
    )
    cursor = db.cursor()

    # SQL query to add a new workout session
    query = """
        INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)
    """

    try:
        # Convert date string to datetime object
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()

        # Execute the SQL query
        cursor.execute(query, (member_id, date_obj, duration_minutes, calories_burned))
        db.commit()
        print(f"Workout session added successfully for member {member_id}!")
    except mysql.connector.Error as e:
        # Handle invalid member ID or other constraints
        print(f"Error: {e}")
    finally:
        # Close the database connection
        cursor.close()
        db.close()

