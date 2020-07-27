import time
import random


class GenInfo:
    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.gender = None
        self.birth_year = None
        self.one_adj_describe_yourself = None
        self.two_adj_describe_yourself = None
        self.location = None
        self.occupation = None
        self.something_you_like = None
        self.username = None
        self.password = None

    def gen_random_person(self):
        self.gen_full_name()
        self.gen_gender()
        self.gen_birth_year()
        self.gen_username()
        self.gen_password()

        return {'first_name': self.first_name,
                'middle_name': self.middle_name,
                'last_name': self.last_name,
                'gender': self.gender,
                'birth_year': self.birth_year,
                'username': self.username,
                'password': self.password}

    def gen_gender(self):
        self.gender = random.choice(['male', 'female'])

    def gen_full_name(self):
        with open('names.txt', 'r') as file:
            lis_of_names = file.readlines()
            self.first_name = random.choice(lis_of_names).split()[0]
            self.last_name = random.choice(lis_of_names).split()[1]
            if self.first_name.find('-') != -1:
                self.middle_name = self.first_name[self.first_name.find('-') + 1:]
                self.first_name = self.first_name[:self.first_name.find('-')]

    def gen_birth_year(self, min_age_group=0, max_age_group=65):
        current_year = int(time.ctime().split()[-1])
        self.birth_year = current_year - random.randint(min_age_group, max_age_group)

    def gen_username(self):
        pass

    def gen_password(self):
        pass


if __name__ == "__main__":
    test = GenInfo()
    test.gen_full_name()
    test.gen_gender()
    test.gen_birth_year(15)

    print(test.first_name, test.middle_name, test.last_name)
    print(test.gender, test.birth_year)
