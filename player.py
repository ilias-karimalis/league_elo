class Player:

    def __init__(self, name, initial_rating=1500., k=32):
        self.name = name
        self.rating = initial_rating
        self.k = k
        self.number_played = 0

    def set_rating(self, new_rating):
        self.rating = new_rating

    def get_rating(self):
        return self.rating

    def inc_number_played(self):
        self.number_played += 1

    def get_number_played(self):
        return self.number_played

    def expected_win(self, rating2):
        return 1. / (1 + 10**((rating2 - self.rating)/400.))

    def update_rating(self, score, rating2):
        self.rating += self.k * (score - self.expected_win(rating2))



