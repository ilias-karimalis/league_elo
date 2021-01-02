import pickle
import argparse
from game import Game
from player import Player

def loadTeam(player_names):
    team = set()

    for name in player_names:
        try:
            f = open('./players/' + name + '.obj', 'br')
            team.add(pickle.load(f))
        except IOError:
            print(name, "data DNE")
            team.add(Player(name))

    return team

def saveTeam(team):

    for p in team:
        f = open('./players/' + p.name + '.obj', 'bw+')
        pickle.dump(p, f)
        f.close()

if __name__ == "__main__":

    # Argument Parser
    CLI = argparse.ArgumentParser()
    CLI.add_argument("--team1", nargs=5, type=str)
    CLI.add_argument("--team2", nargs=5, type=str)
    CLI.add_argument("--result", type=str)

    args = CLI.parse_args()

    # Parse Teams and Winner
    team1 = loadTeam(args.team1)
    team2 = loadTeam(args.team2)
    winner = args.result

    # Run Game
    # Execute Elo Change
    g = Game(team1, team2)
    g.eloChange(winner)

    # Save Players ELOs
    saveTeam(team1)
    saveTeam(team2)

    # Print ELO Results
    for (i,p) in enumerate(team1):
        print('Player', p.name, 'has ELO:', p.get_rating())
    for (i,p) in enumerate(team2):
        print('Player', p.name, 'has ELO:', p.get_rating())

