class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
    
    def update_score(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score

class Scoreboard:
    def __init__(self):
        self.matches = []
    
    def start_match(self, home_team, away_team):
        match = Match(home_team, away_team)
        self.matches.append(match)
    
    def update_score(self, home_team, away_team, home_score, away_score):
        for match in self.matches:
            if match.home_team == home_team and match.away_team == away_team:
                match.update_score(home_score, away_score)
    
    def finish_match(self, home_team, away_team):
        self.matches = [match for match in self.matches if match.home_team != home_team or match.away_team != away_team]
    
    def get_summary(self):
        sorted_matches = sorted(self.matches, key=lambda match: match.home_score + match.away_score, reverse=True)
        return sorted_matches


# Example usage
scoreboard = Scoreboard()

scoreboard.start_match("Mexico", "Canada")
scoreboard.start_match("Spain", "Brazil")
scoreboard.start_match("Germany", "France")

scoreboard.update_score("Mexico", "Canada", 0, 5)
scoreboard.update_score("Spain", "Brazil", 10, 2)
scoreboard.update_score("Germany", "France", 2, 2)

summary = scoreboard.get_summary()
for match in summary:
    print(f"{match.home_team} {match.home_score} - {match.away_team} {match.away_score}")

