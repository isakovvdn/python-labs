import random
import itertools
from datetime import datetime, timedelta

teams = [
    "Team1", "Team2", "Team3", "Team4",
    "Team5", "Team6", "Team7", "Team8",
    "Team9", "Team10", "Team11", "Team12",
    "Team13", "Team14", "Team15", "Team16"
]

random.shuffle(teams)

groups = []
for i in range(0, 16, 4):
    groups.append(teams[i:i + 4])

for i in range(len(groups)):
    print(f"Группа {i + 1}:")
    for team in groups[i]:
        print(team)
    print()

year = datetime.now().year
game_date = datetime(year, 9, 14, 22, 45)

print("Календарь игр:")

for i in range(len(groups)):
    print(f"\nГруппа {i + 1}:")
    matches = list(itertools.combinations(groups[i], 2))

    for team1, team2 in matches:
        print(f"{team1} - {team2} | {game_date.strftime('%d/%m/%Y, %H:%M')}")
        game_date += timedelta(days=14)