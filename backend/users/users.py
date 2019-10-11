import string
import random
import argon2
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

    def hash_password(self, salt):
        return argon2.argon2_hash(self.password, salt=salt, argon_type=0)

    def create_insert_tuple(self, salt, password):
        if self.slack:
            return (self.user, self.email, salt, password, self.slack)
        return (self.user, self.email, salt, password, None)
