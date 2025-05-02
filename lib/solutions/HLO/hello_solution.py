
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if not isinstance(friend_name, str):
            raise TypeError("friend_name must be a string")
        return f"Hello {friend_name}"
