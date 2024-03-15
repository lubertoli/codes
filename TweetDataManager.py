"""
TweetDataManager.py integrates functionalities for managing and interacting with tweet data stored in MongoDB. It includes features to:
- Load tweet data from a JSON file into MongoDB, leveraging the 'loadjson' module.
- Search for tweets based on keywords, utilizing MongoDB's powerful querying capabilities.
- Search for users by keywords in their display names or locations.
- List top tweets and users based on metrics like retweet counts, like counts, and follower counts.
- Allow users to compose and insert new tweets into the database.
- Provide a user-friendly command-line interface for easy navigation and operation.
This script serves as a comprehensive tool for social media data analysis and interaction, designed for data analysts, marketers, and researchers.
"""

import pymongo
import loadjson
from pymongo import MongoClient
from os import system, name
from datetime import datetime
import time

def clear(): 
    """
    Clears the console screen based on the operating system. This utility function enhances the user interface by maintaining a clean screen.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class ContinueLoop(Exception): pass
def search_tweets(collection, keywords):
    """
    Searches and displays tweets that match the given keywords. It supports paginated display and interactive selection for detailed viewing.
    - collection: MongoDB collection from which tweets are queried.
    - keywords: List of keywords to search for within tweet content.
    """
    # Use the '\b' assertion to match word boundaries
    query = {'$and': [{'content': {'$regex': f"\\b{keyword}\\b", '$options': 'i'}} for keyword in keywords]}
    tweets = list(collection.find(query))
    
    if not tweets:
        print("No tweets found with the matching keywords.")
        time.sleep(2)
        return

    i = 0
    while i < len(tweets):
        # Display 5 tweets at a time
        for j in range(i, min(i + 5, len(tweets))):
            tweet = tweets[j]
            print(f"{j+1}. ID: {tweet['id']}\nDate: {tweet['date']}\nContent: {tweet['content']}\nUsername: {tweet['user']['username']}\n")
        
        try:
            while True:
                print()
                print("Enter a number between 1-5 to select a tweet, 'n' for next page, 'p' for previous page, or 'b' to go back to the main menu.")
                choice = input("Enter your choice: ")
                if choice.isdigit() and i < int(choice) <= min(i + 5, len(tweets)):
                    # Display all fields of the selected tweet
                    clear()
                    print(tweets[int(choice) - 1])
                    while True:
                        print()
                        print("Press 'b' to go back to the main menu or 'r' to return to the list of tweets.")
                        choice = input("Enter your choice: ")
                        if choice.lower() == 'b':
                            return
                        elif choice.lower() == 'r':
                            raise ContinueLoop
                        else:
                            print("Invalid choice, please try again.")
                elif choice.lower() == 'n':
                    if i + 5 < len(tweets):
                        i += 5
                        clear()
                        break
                    else:
                        clear()
                        print("There are no more tweets to view.")
                elif choice.lower() == 'p':
                    if i - 5 >= 0:
                        i -= 5
                        clear()
                        break
                    else:
                        print("You're at the first page of tweets.")
                elif choice.lower() == 'b':
                    return
                else:
                    print("Invalid choice, please try again.")
        except ContinueLoop:
            continue


class ContinueLoop(Exception):
    pass

def search_users(collection, keyword):
    """
    Searches and displays users based on a keyword match in their display name or location. Supports interactive selection for detailed information.
    - collection: MongoDB collection from which user data is queried.
    - keyword: Single keyword used for searching user profiles.
    """

    # Use the '\b' assertion to match word boundaries
    query = {'$or': [{'user.displayname': {'$regex': f"\\b{keyword}\\b", '$options': 'i'}}, {'user.location': {'$regex': f"\\b{keyword}\\b", '$options': 'i'}}]}
    results = collection.find(query)

    # Create a dictionary to store unique users
    unique_users = {}

    for result in results:
        user = result['user']
        username = user['username']
        # If the user is already in the dictionary, update the 'followersCount' field if the new count is higher
        if username in unique_users and user['followersCount'] > unique_users[username]['followersCount']:
            unique_users[username]['followersCount'] = user['followersCount']
        # If the user is not in the dictionary, add them
        elif username not in unique_users:
            unique_users[username] = user
    
    # Convert the dictionary to a list
    users = list(unique_users.values())

    # Check if any users were found
    if not users:
        print("No users found.")
        time.sleep(2)
        return

    i = 0
    while i < len(users):
        # Display 5 users at a time
        for j in range(i, min(i + 5, len(users))):
            user = users[j]
            print(f"{j+1}. Username: {user['username']}\nDisplay Name: {user['displayname']}\nLocation: {user['location']}\n")
        
        try:
            while True:
                print()
                print("Enter a number between 1-5 to select a user, 'n' for next page, 'p' for previous page, or 'b' to go back to the main menu.")
                choice = input("Enter your choice: ")
                if choice.isdigit() and i < int(choice) <= min(i + 5, len(users)):
                    # Display all fields of the selected user
                    clear()
                    user = users[int(choice) - 1]
                    print(user)
                    while True:
                        print()
                        print("Press 'b' to go back to the main menu or 'r' to return to the list of users.")
                        choice = input("Enter your choice: ")
                        if choice.lower() == 'b':
                            return
                        elif choice.lower() == 'r':
                            raise ContinueLoop
                        else:
                            print("Invalid choice, please try again.")
                elif choice.lower() == 'n':
                    if i + 5 < len(users):
                        i += 5
                        clear()
                        break
                    else:
                        clear()
                        print("There are no more users to view.")
                elif choice.lower() == 'p':
                    if i - 5 >= 0:
                        i -= 5
                        clear()
                        break
                    else:
                        print("You're at the first page of users.")
                elif choice.lower() == 'b':
                    return
                else:
                    print("Invalid choice, please try again.")
        except ContinueLoop:
            continue

class ContinueLoop(Exception): pass

def list_top_tweets(collection, field, n):
    """
    Lists top 'n' tweets based on a specified metric (e.g., retweetCount, likeCount). Supports interactive selection for detailed tweet information.
    - collection: MongoDB collection containing tweet data.
    - field: Metric used for ranking tweets.
    - n: Number of top tweets to display.
    """

    fields = ['retweetCount', 'likeCount', 'quoteCount']
    if field not in fields:
        print("Invalid field. Please choose from 'retweetCount', 'likeCount', or 'quoteCount'.")
        return

    tweets = list(collection.find().sort(field, pymongo.DESCENDING).limit(n))
    
    i = 0
    while i < len(tweets):
        # Display 5 tweets at a time
        for j in range(i, min(i + 5, len(tweets))):
            tweet = tweets[j]
            print(f"{j+1}. ID: {tweet['id']}\nDate: {tweet['date']}\nContent: {tweet['content']}\nUsername: {tweet['user']['username']}\n")
        
        try:
            while True:
                print()
                print("Enter a number between 1 and n to select a tweet, or 'b' to go back to the main menu.")
                choice = input("Enter your choice: ")
                if choice.isdigit() and 1 <= int(choice) <= n:
                    # Display all fields of the selected tweet
                    clear()
                    print(tweets[int(choice) - 1])
                    while True:
                        print()
                        print("Press 'b' to go back to the main menu or 'r' to return to the list of tweets.")
                        choice = input("Enter your choice: ")
                        if choice.lower() == 'b':
                            return
                        elif choice.lower() == 'r':
                            clear()
                            raise ContinueLoop
                        else:
                            print("Invalid choice, please try again.")
                elif choice.lower() == 'b':
                    return
                else:
                    print("Invalid choice, please try again.")
        except ContinueLoop:
            continue

class ContinueLoop(Exception): pass

def list_top_users(collection, n):
    """
    Lists top 'n' users based on their follower count, displaying each user's profile information in a ranked order.
    - collection: MongoDB collection containing user data.
    - n: Number of top users to display.
    """
    while True:
        try:
            pipeline = [
                {"$group": {"_id": "$user.username", "displayname": {"$first": "$user.displayname"}, "followersCount": {"$max": "$user.followersCount"}}},
                {"$sort": {"followersCount": pymongo.DESCENDING}},
                {"$limit": n}
            ]
            users = list(collection.aggregate(pipeline))
            
            # Display all n users at once
            for i, user in enumerate(users):
                print(f"{i+1}. Username: {user['_id']}\nDisplay Name: {user['displayname']}\nFollowers Count: {user['followersCount']}\n")
            print()
            print("Enter a number between 1 and n to select a user, or 'b' to go back to the main menu.")
            choice = input("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= n:
                # Display all fields of the selected user
                clear()
                user = collection.find_one({'user.username': users[int(choice) - 1]['_id']})
                print(user)
                while True:
                    print()
                    print("Press 'b' to go back to the main menu or 'r' to return to the list of users.")
                    choice = input("Enter your choice: ")
                    if choice.lower() == 'b':
                        return
                    elif choice.lower() == 'r':
                        raise ContinueLoop
                    else:
                        print("Invalid choice, please try again.")
            elif choice.lower() == 'b':
                return
            else:
                print("Invalid choice, please try again.")
        except ContinueLoop:
            continue

def compose_tweet(collection):
    """
    Prompts the user to compose a new tweet and inserts it into the MongoDB collection, confirming successful posting.
    - collection: MongoDB collection where the new tweet will be inserted.
    """
    
    # Ask the user to enter the content of the tweet
    content = input("Enter the content of your tweet: ")

    # Create a new tweet document
    tweet = {
        "content": content,
        "date": datetime.now(),  # Set the date to the current system date
        "username": "291user",  # Set the username to "291user"
        # Set all other fields to None
        "retweetCount": None,
        "likeCount": None,
        "quoteCount": None,
        "user": None
    }
    # Insert the new tweet into the collection
    collection.insert_one(tweet)

def main(): 
    """
    Main function to initialize the script's functionality. It integrates the 'loadjson' module for data loading and provides a menu-driven interface for users to interact with tweet data in MongoDB.
    """
    # Load the JSON file into MongoDB
    json_file_name = input("Enter the JSON file name: ")
    mongodb_port_number = input("Enter the MongoDB port number: ")
    loadjson.main(json_file_name, mongodb_port_number)

    # Establish a connection to MongoDB
    client = MongoClient("mongodb://localhost:{}/".format(mongodb_port_number)) 
    db = client['291db']
    collection = db['tweets']

    while True:
        # Present the menu options to the user
        clear()
        print()
        print("1. Search for tweets")
        print("2. Search for users")
        print("3. List top tweets")
        print("4. List top users")
        print("5. Compose a tweet")
        print("6. Exit")
        print()
        choice = input("Choose an option: ")
        
        if choice == '1':
            clear()
            keywords = input("Enter keywords separated by space: ").split()
            print()
            search_tweets(collection, keywords)
        elif choice == '2':
            clear()
            keyword = input("Search for user: ")
            print()
            search_users(collection, keyword)
            print()
        elif choice == '3':
            clear()
            category_options = {1: 'retweetCount', 2: 'likeCount', 3: 'quoteCount'}
            category = int(input("What category of top tweets would you like to see? \n 1. Retweet Count. \n 2. Like Count. \n 3. Quote Count. \n \n Enter your choice: "))
            num_tweets = int(input("Enter the number of top tweets to list: "))
            print()
            list_top_tweets(collection, category_options[category], num_tweets)
        elif choice == '4':
            clear()
            num_users = int(input("Enter the number of top users to list: "))
            list_top_users(collection, num_users)
        elif choice == '5':
            clear()
            compose_tweet(collection)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()
    
