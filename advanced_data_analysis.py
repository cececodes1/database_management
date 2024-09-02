
import sqlite3
# Define a function to get members in a specific age range
def get_members_in_age_range(start_age, end_age):
   
    try:
        # Establish a connection to the SQLite database
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()

        # SQL query using BETWEEN to get members in the specific age range
        query = """
            SELECT *
            FROM Members
            WHERE age BETWEEN ? AND ?
        """

        # Execute the query with the provided age range
        cursor.execute(query, (start_age, end_age))

        # Fetch all the rows from the query result
        members_in_age_range = cursor.fetchall()

        # Close the database connection
        conn.close()

        return members_in_age_range

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
