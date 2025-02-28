import psycopg2
import json
 
 
def lambda_handler(event, context):
    # Database connection parameters
 
    data = get_database_data()
 
    # Return the results
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
 
def get_database_data():
    # Database connection parameters
    conn_params = {
        "dbname": "neondb",
        "user": "neondb_owner",
        "password": "npg_t5GjDv8rJmax",
        "host": "ep-floral-dawn-a7hjneqv-pooler.ap-southeast-2.aws.neon.tech",
        "port": "5432",
        "sslmode": "require"

    }
   
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
   
    # Convert query results to a list of dictionaries to serialize them as JSON
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "firstname": row[1],
            "lastname": row[2],
            "email": row[3],
            "phone_number": row[4]
        })
   
    # Close the database connection
    cur.close()
    conn.close()
   
    return result
 
if __name__ == "__main__":
    test_event = {}  # Populate this with your test event data
    print(lambda_handler(test_event, None))