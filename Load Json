# This script facilitates the importation of tweet data from a JSON file into a MongoDB database.
# It establishes a connection to a specified MongoDB instance, creates or replaces the 'tweets' collection,
# and efficiently inserts tweet documents in batches. Additionally, it creates a text index on the 'content' field
# to enable efficient text search operations within the collection. This script is ideal for initializing or
# updating tweet datasets in MongoDB for data analysis or application development purposes.

import pymongo
from pymongo import MongoClient
import json

def main(filename, port):
    '''
    The main function that orchestrates the importation process.
    It takes a filename and a port number as inputs, establishes a connection to MongoDB,
    manages the collection creation, performs batch insertions of tweet data, and sets up text indexing.

    Parameters:
    - filename: The name of the JSON file containing tweet data.
    - port: The port number on which the MongoDB server is running.
    '''
    
    # Establish a connection to MongoDB
    client = MongoClient("mongodb://localhost:{}/".format(port)) 
    db = client['291db']
    
    # Drop the existing 'tweets' collection if it exists and create a new one
    if 'tweets' in db.list_collection_names():
        db['tweets'].drop()
    tweets_collection = db['tweets']
    
    try:
        # Open the JSON file and insert documents in batches
        with open(filename, 'r') as file:
            tweets_batch = []
            batch_size = 1000  # Define your batch size here
            for line in file:
                tweet = json.loads(line)
                tweets_batch.append(tweet)
                if len(tweets_batch) >= batch_size: 
                    tweets_collection.insert_many(tweets_batch)
                    tweets_batch = []
            # Insert any remaining tweets
            if tweets_batch:
                tweets_collection.insert_many(tweets_batch)
        
        # Create a text index on the 'content' field
        tweets_collection.create_index([("content", pymongo.TEXT)], default_language='english')
    except Exception as e:
        print("An error occurred.")
    finally:
        # Close the connection to MongoDB
        client.close()

if __name__ == "__main__":
    # User inputs for the JSON file name and MongoDB port number
    json_file_name = input("Enter the JSON file name: ")
    mongodb_port_number = input("Enter the MongoDB port number: ")
    
    main(json_file_name, mongodb_port_number)
