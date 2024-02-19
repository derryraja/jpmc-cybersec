from collections import OrderedDict

class RolesCache:
    def __init__(self, k):
        self.k = k
        self.roles_dict = OrderedDict()

    def set(self, role_name, message):
        if role_name in self.roles_dict:
            del self.roles_dict[role_name]

        if len(self.roles_dict) >= self.k:
            self.roles_dict.popitem(last=False)

        self.roles_dict[role_name] = message

    def get(self):
        return list(self.roles_dict.items())

# Example usage:
# Create RolesCache instance with a limit of 3 roles
roles_cache = RolesCache(3)

# Set roles for a person
roles_cache.set("Admin", "Accessed admin panel")
roles_cache.set("User", "Viewed user data")
roles_cache.set("Moderator", "Moderated discussions")

# Get the current active roles for the person
active_roles = roles_cache.get()
print(active_roles)