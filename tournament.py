from prettytable import PrettyTable
filename = "matches.txt"


class Team:
    def __init__(self, teamName, matchesPlayed, matchesWon, matchesDraw, matchesLost, points):
        self.teamName = teamName
        self.matchesPlayed = matchesPlayed
        self.matchesWon = matchesWon
        self.matchesDraw = matchesDraw
        self.matchesLost = matchesLost
        self.points = points


class Match:
    def __init__(self, firstTeam, secondTeam, result):
        self.firstTeam = firstTeam
        self.secondTeam = secondTeam
        self.result = result


def register_matches(filename):
    matches = []
    teams= []

    with open(filename, 'r') as file:
        for line in file:
            match = [l.strip() for l in line.split(';')]
            firstTeam = register_team(match[0], teams)
            secondTeam = register_team(match[1], teams)
            match = Match(firstTeam, secondTeam, match[2])
            matches.append(match)
            compute_result(match)
        return teams


def register_team(teamName, teams):
    team = next((x for x in teams if x.teamName == teamName), None)
    if(team is not None):
        return team

    team = Team(teamName, 0, 0, 0, 0, 0)
    teams.append(team)
    return team


def compute_result(match):
    if match.result == 'win':
        match.firstTeam.matchesPlayed += 1
        match.firstTeam.matchesWon += 1
        match.firstTeam.points += 3

        match.secondTeam.matchesPlayed += 1
        match.secondTeam.matchesLost += 1
    elif match.result == 'loss':
        match.firstTeam.matchesPlayed += 1
        match.firstTeam.matchesLost += 1

        match.secondTeam.matchesPlayed += 1
        match.secondTeam.matchesWon += 1
        match.secondTeam.points += 3
    elif match.result == 'drawn':
        match.firstTeam.matchesPlayed += 1
        match.firstTeam.matchesDraw += 1
        match.firstTeam.points += 1

        match.secondTeam.matchesPlayed += 1
        match.secondTeam.matchesDraw += 1
        match.secondTeam.points += 1


def main():

    try:
        teams = register_matches(filename)
        teams.sort(key=lambda x: x.points, reverse=True)

        x = PrettyTable()
        x.field_names = ["Team", "MP", "Won", "Drawn", "Lost", "Points"]
        for team in teams:
            x.add_row([team.teamName, team.matchesPlayed, team.matchesWon,
                       team.matchesDraw, team.matchesLost, team.points])

        print(x)

    except FileNotFoundError:
        print('File does not exist')

    except IndexError:
        print('Invalid Input')


if __name__ == '__main__':
    main()
