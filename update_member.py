
import mysql.connector

def update_member_age(member_id, new_age):

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="gym_admin",
        password="password123",
        database="gym_management"
    )
    cursor = db.cursor()

    # SQL query to check if member exists
    query_check_member = """
        SELECT * FROM Members
        WHERE id = %s
    """

    # SQL query to update age
    query_update_age = """
        UPDATE Members
        SET age = %s
        WHERE id = %s
    """

    try:
        # Check if member exists
        cursor.execute(query_check_member, (member_id,))
        member_data = cursor.fetchone()

        if member_data is None:
            print(f"Member {member_id} does not exist.")
            return

        # Update age
        cursor.execute(query_update_age, (new_age, member_id))
        db.commit()
        print(f"Age updated successfully for member {member_id}!")
    except mysql.connector.Error as e:
        # Handle errors
        print(f"Error: {e}")
    finally:
        # Close the database connection
        cursor.close()
        db.close()
