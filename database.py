import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            user, password, created = line.strip().split(";")
            self.users[user] = (password, created)

        self.file.close()

    def get_user(self, user):
        if user in self.users:
            return self.users[user]
        else:
            return -1

    def add_user(self, user, password):
        if email.strip() not in self.users:
            self.users[user.strip()] = (password.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("ID exists already")
            return -1

    def validate(self, user, password):
        if self.get_user(user) != -1:
            return self.users[user][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]