import mysql.connector
from mysql.connector import errorcode


def create_connection(host, username, password, database):
    try:
        cnx = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("Connection established with the database")
        return cnx
    except Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
# Read Operation
def read_has(connection):
    query = "SELECT * FROM HAS"
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def read_ticket(connection):
    query = "SELECT * FROM ticket"
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to execute a query
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
# Insert Operation
def insert_ticket(connection, data):
    query = "INSERT INTO ticket (ticket_id,price,class) VALUES (%s,%s, %s)"
    execute_query(connection, query, data)



# Update Operation
def update_ticket(connection, ticket_id, new_class):
    query = "UPDATE ticket SET class = %s WHERE ticket_id = %s"
    data = (new_class, ticket_id)
    execute_query(connection, query, data)


# Delete Operation
def delete_ticket(connection, ticket_id):
    query = "DELETE FROM ticket WHERE ticket_id = %s"
    data = (ticket_id),
    execute_query(connection, query, data)


# Insert Operation
def insert_has(connection, data):
    query = "INSERT INTO has (ticket_id,seat_id,seat_number) VALUES (%s,%s, %s)"
    execute_query(connection, query, data)



# Update Operation
def update_has(connection, ticket_id, new_seat_number):
    query = "UPDATE has SET seat_number = %s WHERE ticket_id = %s"
    data = (new_seat_number, ticket_id)
    execute_query(connection, query, data)


# Delete Operation
def delete_has(connection, seat_number):
    query = "DELETE FROM has WHERE seat_number = %s"
    data = (seat_number),
    execute_query(connection, query, data)







cnx = create_connection(host, username, password, database)
cursor = cnx.cursor()





data_ticket = ("T124", "124.00", "economy")
insert_ticket(cnx, data_ticket)

#Insert data into tables
data_has = ("T124", "C6", "5C")
insert_has(cnx, data_has)






# Delete ticket with ID "T123"
delete_ticket(cnx, "T123")

# Delete seat information for seat "3A"
delete_has(cnx, "3A")


# Update seat information for ticket "T456" to seat "2C"
update_has(cnx, "T456", "2C")

# Update ticket class for ticket "T110" to "business"
update_ticket(cnx, "T124", "Business")


