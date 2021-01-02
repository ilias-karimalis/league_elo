from player import Player

class Game:

    # teams are sets of Players
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def eloChange(self, winner):

        team1 = self.team1
        team2 = self.team2

        # Get Teams average Ratings
        team1_rating = sum([p.get_rating() for p in team1])/len(team1)
        team2_rating = sum([p.get_rating() for p in team2])/len(team2)

        if (winner == "team1"):
            for p in team1:
                p.update_rating(1.0, team2_rating)
                p.inc_number_played()

            for p in team2:
                p.update_rating(0.0, team1_rating)
                p.inc_number_played()
        elif (winner == "team2"):
            for p in team2:
                p.update_rating(1.0, team1_rating)
                p.inc_number_played()

            for p in team1:
                p.update_rating(0.0, team2_rating)
                p.inc_number_played()
