# File: delete_workout_session.py

import mysql.connector

def delete_workout_session(session_id):
 
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="gym_admin",
        password="password123",
        database="gym_management"
    )
    cursor = db.cursor()

    # SQL query to check if session exists
    query_check_session = """
        SELECT * FROM WorkoutSessions
        WHERE id = %s
    """

    # SQL query to delete a session
    query_delete_session = """
        DELETE FROM WorkoutSessions
        WHERE id = %s
    """

    try:
        # Check if session exists
        cursor.execute(query_check_session, (session_id,))
        session_data = cursor.fetchone()

        if session_data is None:
            print(f"Workout session {session_id} does not exist.")
            return

        # Delete session
        cursor.execute(query_delete_session, (session_id,))
        db.commit()
        print(f"Workout session {session_id} deleted successfully!")
    except mysql.connector.Error as e:
        # Handle errors
        print(f"Error: {e}")
    finally:
        # Close the database connection
        cursor.close()
        db.close()

