import string
import random
class Users:
    def __init__(self, username, email, password, slack_user=None):
        self.user = username
        self.email  = email
        self.password = password
        self.slack = slack_user
        self.salt = string.ascii_letters + string.digits
        random.seed(1421)

    def build_salt(self):
        return ''.join(random.choice(self.salt) for i in range(30))