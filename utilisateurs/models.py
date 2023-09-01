class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class AccessControl:
    def __init__(self):
        self.users = []

    def add_user(self, username, role):
        user = User(username, role)
        self.users.append(user)

    def check_access(self, user, required_roles):
        if user.role in required_roles:
            return True
        else:
            return False

# Création d'une instance de AccessControl
access_control = AccessControl()

# Ajout des utilisateurs
access_control.add_user("public_user", "public")
access_control.add_user("tl_user", "tl")
access_control.add_user("ctrl_user", "ctrl")
access_control.add_user("admin_user", "admin")

# Exemples de vérification d'accès
user1 = access_control.users[0]
print(access_control.check_access(user1, ["public"]))  # True
print(access_control.check_access(user1, ["tl", "ctrl", "admin"]))  # False

user2 = access_control.users[1]
print(access_control.check_access(user2, ["tl"]))  # True
print(access_control.check_access(user2, ["ctrl", "admin"]))  # False

user3 = access_control.users[2]
print(access_control.check_access(user3, ["ctrl"]))  # True
print(access_control.check_access(user3, ["tl", "admin"]))  # False

user4 = access_control.users[3]
print(access_control.check_access(user4, ["admin"]))  # True
print(access_control.check_access(user4, ["public", "tl", "ctrl"]))  # False
