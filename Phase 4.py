import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



def print_document(document):
    print()
    for key, value in document.items():
        if key != '_id':
            print(f"{key}: {value}")
    print()

def create_collection(collection_name):
    db.create_collection(collection_name)
    print(f"Collection '{collection_name}' created successfully!")

def read_all_data(collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for document in documents:
        print_document(document)

def read_filtered_data(collection_name, filter_query):
    collection = db[collection_name]
    documents = collection.find(filter_query)
    for document in documents:
        print_document(document)

def insert_data(collection_name, data):
    collection = db[collection_name]
    collection.insert_one(data)
    print("Data inserted successfully!")

def delete_data(collection_name, filter_query):
    collection = db[collection_name]
    result = collection.delete_one(filter_query)
    print(f"Deleted {result.deleted_count} document(s)")

def update_data(collection_name, filter_query, new_values):
    collection = db[collection_name]
    result = collection.update_one(filter_query, {"$set": new_values})
    print(f"Updated {result.modified_count} document(s)")


def main():
    print("Welcome to Game Review Portal!")
    user_id = input("Please enter your user id: ")
    while True:
        
        print("Please pick the option that you want to proceed.")
        print("1 - Create a collection")
        print("2 - Read all data in a collection")
        print("3 - Read some part of the data while filtering")
        print("4 - Insert data")
        print("5 - Delete data")
        print("6 - Update data")
        print()
        option = int(input("Selected option: "))
        
        # Creating a collection
        if option == 1:
            collection_name = input("Enter the name of the collection to create: ")
            create_collection(collection_name)
        
        # Reading all data from a collection
        elif option == 2:
            print("Please select the collection you want to read from: ")
            print("1- Racing Games reviews")  
            print("2- FPS Games reviews")
            print()
            collection_option = int(input("Selected option: "))
            if collection_option == 1:
                collection_name = "Racing Games"
            elif collection_option == 2:
                collection_name = "FPS Games"
            else:
                print("Invalid option!")
                continue
            read_all_data(collection_name)
        
        # Reading some part of a collection
        elif option == 3:
            print("Please select the collection you want to read from: ")
            print("1- Racing Games reviews")  
            print("2- FPS Games reviews")
            print()
            collection_option = int(input("Selected option: "))
            if collection_option == 1:
                collection_name = "Racing Games"
            elif collection_option == 2:
                collection_name = "FPS Games"
            else:
                print("Invalid option!")
                continue

            print("Please select the category to filter by: ")
            print("1- User ID")  
            print("2- Game Name")
            print("3- Review Message")
            print("4- Given Star")
            print()
            category_option = int(input("Selected option: "))

            if category_option == 1:
                category = "user_id"
                filter_value = input(f"Enter the value to filter by User ID: ")
            elif category_option == 2:
                category = "name"
                filter_value = input(f"Enter the value to filter by Game Name: ")
            elif category_option == 3:
                category = "review_message"
                filter_value = input(f"Enter the value to filter by Review Message: ")
            elif category_option == 4:
                category = "given_star"
                filter_value = input(f"Enter the value to filter by Given Star: ")

            else:
                print("Invalid option!")
                continue
            
            if category == "given_star":
                try:
                    filter_value = int(filter_value)
                except ValueError:
                    print("Invalid star rating! Please enter a numerical value.")
                    continue
            
            filter_query = {category: filter_value}
            read_filtered_data(collection_name, filter_query)
        
        # Inserting
        elif option == 4:
            print("Please select the collection you want to insert data into:")
            print("1 - Racing Games")
            print("2 - FPS Games")
            print()
            collection_option = int(input("Selected option: "))
            if collection_option == 1:
                collection_name = "Racing Games"
            elif collection_option == 2:
                collection_name = "FPS Games"
            else:
                print("Invalid option!")
                continue
            print()
            print('Please enter the data fields: ')
            print()
            data = {}
            data['user id'] = user_id
            data['game name'] = input("Enter the name of the game: ")
            data['review message'] = input("Enter the review message: ")
            while True:
                try:
                    data['given_star'] = int(input("Enter the star rating (1-5): "))
                    if 1 <= data['given_star'] <= 5:
                        break
                    else:
                        print("Invalid star rating! Please enter a value between 1 and 5.")
                except ValueError:
                    print("Invalid input! Please enter a numerical value between 1 and 5.")
            insert_data(collection_name, data)

        # Deleting
        elif option == 5:
            print("Please select the collection you want to delete data from:")
            print("1 - Racing Games")
            print("2 - FPS Games")
            print()
            collection_option = int(input("Selected option: "))
            if collection_option == 1:
                collection_name = "Racing Games"
            elif collection_option == 2:
                collection_name = "FPS Games"
            else:
                print("Invalid option!")
                continue
            print()
            print('Please enter the data fields: ')
            print()

            filter_query = eval(input("Enter the filter query to delete data (e.g., {'name': 'Star Wars'}): "))
            delete_data(collection_name, filter_query)
        
        # Updating
        elif option == 6:
            print("Please select the collection you want to update data in:")
            print("1 - Racing Games")
            print("2 - FPS Games")
            print()
            collection_option = int(input("Selected option: "))
            if collection_option == 1:
                collection_name = "Racing Games"
            elif collection_option == 2:
                collection_name = "FPS Games"
            else:
                print("Invalid option!")
                continue
            print()
            print('Please enter the data fields: ')
            print()

            filter_query = eval(input("Enter the filter query to identify data to update (e.g., {'name': 'Star Wars'}): "))
            new_values = eval(input("Enter the new values to update (e.g., {'review_message': 'Updated review!'}): "))
            update_data(collection_name, filter_query, new_values)
        
        else:
            print("Invalid option! Please try again.")
        
        next_action = input("Would you like to perform another action? (yes/no): ")
        if next_action.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
