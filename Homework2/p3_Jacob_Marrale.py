# Homework 2
import os # for tests
# Question 3a:

def add_user(sn: dict , username: str ,fullname: str) -> bool: # sn is a dict where the key is the username and the value is a tuple with their full name and a list of their friends
    try:
        if username in sn:
            print(f"User '{username}' already in system")
            return False
        else:
            sn[username] = (fullname,[])
            print(f"User '{username}' added to system")
            return True
            

    except Exception as e:
        print(f"Function Failure, add_user: {e}")
        raise

# Question 3b:

def add_friend(sn: dict , user1: str , user2: str) -> bool: # sn is a dict where the key is the username and the value is a tuple with their full name and a list of their friends
    try:
        if user1 == user2:
            print(f"you cannot friend yourself")
            return False
        if user1 not in sn or user2 not in sn:
            print(f"user '{user1}' or '{user2}' not found")
            return False
        if user2 in sn[user1][1] or user1 in sn[user2][1]:
            print(f"you already have this person friended")
            return False
        # These conditions should be able to handle most issues so no need for an else
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        print(f"mutual friend link created between {user1} and {user2}")
        return True
    
    except Exception as e:
        print(f"Function Failure, add_friend: {e}")
        raise

# Question 3c:
def get_friends(sn: dict , user1: str , distance: int) -> list: # pathing through friends when distance increases to append their friends
    try:
        if type(distance) is not int or distance < 0 :
            print("please provide a positive integer for distance")
            return []
        if user1 not in sn:
            print("user not found")
            return []
        found = []
        seen = {user1}
        cur_lvl = [user1]
        for lvl in range(distance):
            next_lvl = []
            for user in cur_lvl:
                for friend in sn[user][1]:
                    if friend not in seen:
                        seen.add(friend)
                        found.append(friend)
                        next_lvl.append(friend)
                cur_lvl = next_lvl
        print(found)
        return found
            
    except Exception as e:
        print(f"Function Failure, get_friends: {e}")
        raise

# Question 3d:
def save_network(filename: str , sn: dict) -> csv: # Question says "Let your function throw relevant exceptions, e.g. FileNotFoundError." I'm gonna assume exception block with a focus on a file not found error
    try:
        # the csv isn't pretty and is just commas between each data because the question didn't specific ask for it plus it'll be easy for the next function to load
        with open(filename, 'w') as file:
            for username in sn:
                fullname = sn[username][0]
                friends = sn[username][1]
                rows = [username, fullname] + friends # friends are a list so have to add them to the back
                file.write(','.join(rows) + '\n')
    except FileNotFoundError as error: # relevent exception
        print(f"File not found: {e}")
        raise

# Question 3e:
def load_network(filename: str) -> dict: # transfer file data back to dict
    try:
        loaded_net = {}
        with open (filename, 'r') as file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                username = fields[0]
                fullname = fields[1]
                friends = fields[2:]
                loaded_net[username] = (fullname, friends)
        return loaded_net

    except FileNotFoundError as error: # relevent exception
        print(f"File not found: {e}")
        raise

def main():
    #   Question 3a test:
    user = "jake"
    full = "Jacob Marrale"
    sn = {}
    add_user(sn, user, full)
    add_user(sn, user, full)
    print(sn)

    #   Question 3b test:
    sn = {'jake': ('Jacob Marrale', []), 'james': ('James Warshaw', [])}
    sn = {}
    add_friend(sn , "jake" , "james")
    print(sn)
    add_friend(sn , "jake" , "james")
    print(sn)

    # Question 3c test:
    sn = {'alice': ('Alice Smith', ['maria']),
          'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
          'joe': ('Joseph Adams', ['maria', 'eve']),
          'eve': ('Evelyn Cooper', ['joe']),
          'david': ('David Benson', ['maria'])}
    get_friends(sn, "alice", 1)
    get_friends(sn, "alice", 2)
    get_friends(sn, "james", 1.89)
    get_friends(sn, "alice", 1.89)

    # Question 3d test:
    path = os.path.join(os.path.dirname(__file__), 'network.csv')
    save_network(path , sn)

    # Question 3e test:
    loaded = load_network(path)
    print(loaded)


if __name__ == "__main__":
    main()