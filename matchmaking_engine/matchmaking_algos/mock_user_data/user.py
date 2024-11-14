class User:
    def __init__(self, user_id, name, age, gender, location, interests):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location  # location as a tuple (latitude, longitude)
        self.interests = interests  # list of interests
        self.preferences = {
            'age_range': (18, 35),
            'distance': 50,  # in kilometers
            'gender': None  # gender preference
        }
        self.activity_log = []  # to store swipe history, matches, etc.
