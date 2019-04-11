filename = "matches.txt"


class Team:
    def __init__(self, teamName, matchesPlayed, matchesWon, matchesDraw, matchesLost):
        self.teamName = teamName
        self.matchesPlayed = matchesPlayed
        self.matchesWon = matchesWon
        self.matchesDraw = matchesDraw
        self.matchesLost = matchesLost


class Match:
    def __init__(self, firstTeam, secondTeam, result):
        self.firstTeam = firstTeam
        self.secondTeam = secondTeam
        self.result = result


def registerMatches(filename):
    matches = []
    with open(filename, 'r') as file:
        for line in file:
            match = [l.strip() for l in line.split(';')]
            matches.append(Match(match[0], match[1], match[2]))
        return matches

        # TODO: Validate match


def registerTeams(matches):
    teams = []
    for match in matches:
        if len(teams) == 0:
            teams.append(Team(match.firstTeam, 0, 0, 0, 0))
        if not any(x for x in teams if x.teamName == match.firstTeam):
            teams.append(Team(match.firstTeam, 0, 0, 0, 0))
        if not any(x for x in teams if x.teamName == match.secondTeam):
            teams.append(Team(match.secondTeam, 0, 0, 0, 0))
    return teams


def scoresTeams(teams, matches):
    for match in matches:
        if(match.result == 'win'):
            for team in teams:
                if team.teamName == match.firstTeam:
                    team.matchesPlayed = team.matchesPlayed + 1
                    team.matchesWon = team.matchesWon + 1
                if team.teamName == match.secondTeam:
                    team.matchesPlayed = team.matchesPlayed + 1
                    team.matchesLost = team.matchesLost + 1

        if(match.result == 'drawn'):
            for team in teams:
                if team.teamName == match.firstTeam:
                    team.matchesPlayed = team.matchesPlayed + 1
                if team.teamName == match.secondTeam:
                    team.matchesPlayed = team.matchesPlayed + 1

        if(match.result == 'loss'):
            for team in teams:
                if team.teamName == match.firstTeam:
                    team.matchesPlayed = team.matchesPlayed + 1
                if team.teamName == match.secondTeam:
                    team.matchesPlayed = team.matchesPlayed + 1
    return teams


def main():

    try:
        matches = registerMatches(filename)
        teams = registerTeams(matches)
        scores = scoresTeams(teams, matches)

        for team in teams:
            print(team.teamName)

        for score in scores:
            print("-------------------------------------")
            print("Team Name: " + str(score.teamName))
            print("Matches Played: " + str(score.matchesPlayed))

    except FileNotFoundError:
        print('File does not exist')


main()
