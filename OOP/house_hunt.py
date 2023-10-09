class User:
    def __init__(self, username, email, user_type):
        self.username = username
        self.email = email
        self.user_type = user_type

    def __str__(self):
        return f"User: {self.username} ({self.user_type})"

class Buyer(User):
    def __init__(self, username, email):
        super().__init__(username, email, "Buyer")
    def search_properties(self):

# Add code to search for properties based on location and budget
class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email, "Seller")
    def list_property(self, property_info):

# Add code to list a property for sale with property_info
class Agent(User):

    def __init__(self, username, email):
        super().__init__(username, email, "Agent")

    def assist_buyer(self, buyer, location, property_type):

# Example usage:

buyer1 = Buyer("JohnDoe", "john@example.com")

seller1 = Seller("JaneSmith", "jane@example.com")

agent1 = Agent("AgentSmith", "agent@example.com")

print(buyer1)

print(seller1)

print(agent1)

buyer1.search_properties("New York", 200000)

seller1.list_property({"location": "Los Angeles", "price": 300000})

agent1.assist_buyer(buyer1, "San Francisco", "Condo")