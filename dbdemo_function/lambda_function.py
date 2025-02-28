import psycopg2
import json
import logging
import os
 
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
 
def lambda_handler(event, context):
    # Database connection parameters
    conn_params = {
        "dbname": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": os.environ.get("DB_HOST"),
        "port": os.environ.get("DB_PORT"),
    }
 
    try:
        # Fetch data from the database
        data = get_database_data(conn_params)
        return {
            "statusCode": 200,
            "body": json.dumps(data)
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
 
def get_database_data(conn_params):
    """Fetch data from the database and return it as a JSON-serializable list."""
    try:
        # Convert dictionary to connection string
        dsn = " ".join([f"{key}={value}" for key, value in conn_params.items()])
        # SQL query to execute
        query = "SELECT * FROM Person;"
 
        # Connect to the database
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
 
        # Execute the query
        cur.execute(query)
 
        # Fetch all the results
        rows = cur.fetchall()
 
        # Convert query results to a list of dictionaries
        result = [
            {
                "id": row[0],
                "firstname": row[1],
                "lastname": row[2],
                "email": row[3],
                "phone_number": row[4]
            }
            for row in rows
        ]
 
        # Close the database connection
        cur.close()
        conn.close()
 
        return result
 
    except Exception as e:
        logger.error(f"Database error: {e}")
        return []
 
if __name__ == "_main_":
    test_event = {}  # Populate this with your test event data
    print(lambda_handler(test_event, None))