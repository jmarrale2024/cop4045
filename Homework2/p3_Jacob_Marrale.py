# Homework 2

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

def main():
    # Question 3a test:
    user = "jake"
    full = "Jacob Marrale"
    sn = {}
    add_user(sn, user, full)
    add_user(sn, user, full)
    print(sn)
    # Question 3b test:
    
if __name__ == "__main__":
    main()