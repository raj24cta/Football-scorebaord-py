# Football-scorebaord-py
Live Football World Cup Scoreboard
This is a simple library implementation of a Live Football World Cup Scoreboard. It allows you to track ongoing matches, update scores, and retrieve a summary of the matches based on their scores.

Features
Start a new game with default scores (0-0) and add it to the scoreboard.
Update the score of a game with the home team score and away team score.
Finish a game currently in progress and remove it from the scoreboard.
Get a summary of ongoing games ordered by their total score.
Requirements
Python 3.x
Usage
Create an instance of the Scoreboard class:

python
Copy code
scoreboard = Scoreboard()
Start a new game:

python
Copy code
scoreboard.start_game("Home Team", "Away Team")
Update the score of a game:

python
Copy code
scoreboard.update_score("Home Team", "Away Team", home_score, away_score)
Finish a game:

python
Copy code
scoreboard.finish_game("Home Team", "Away Team")
Get a summary of ongoing games:

python
Copy code
summary = scoreboard.get_summary()
The summary variable will contain a list of matches in the scoreboard, ordered by their total score.

Example usage to print the summary:

python
Copy code
for index, match in enumerate(summary, start=1):
    teams = " - ".join(match[0])
    score = " - ".join(str(s) for s in match[1])
    print(f"{index}. {teams} {score}")
Testing
The code includes a set of test cases using the JUnit framework to verify the functionality of the Scoreboard class. The tests cover starting games, updating scores, finishing games, and getting the summary. You can run the tests using a testing framework such as JUnit.

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Feel free to modify and use this code according to your needs.






