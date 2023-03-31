import pandas as pd
import random

ceo_ids = [
    13, 48, 63, 74, 100, 101, 111, 115, 139, 164, 168, 198, 213, 228, 237,
    249, 262, 264, 287, 310, 316, 330, 344, 362, 369, 374, 406, 410, 412, 418,
    446, 447, 452, 472, 506, 518, 558, 627, 654, 683, 685, 704, 746, 756,
    768, 772, 789, 826, 827, 832, 843, 901, 911, 953, 989, 998
]

# Assign districts, teams, and team leaders
districts = ["North", "Central", "South"]
teams = [1, 2, 3, 4, 5, 6, 7, 8, 9]
team_leaders = ["Paul", "Naz", "Michael", "Anna", "Nick", "Andrew", "Sandra", "Emiru", "Patrick"]

# Distribute CEOs equally among districts and teams
assigned_districts = []
assigned_teams = []
assigned_team_leaders = []

for i, ceo_id in enumerate(ceo_ids):
    assigned_districts.append(districts[i % len(districts)])
    assigned_teams.append(teams[i % len(teams)])
    assigned_team_leaders.append(team_leaders[i % len(team_leaders)])

# Assign "Mobile" or "On foot" attribute
ceos_with_mobile = random.sample(ceo_ids, 12)
attributes = ["Mobile" if ceo_id in ceos_with_mobile else "On foot" for ceo_id in ceo_ids]

# Create a DataFrame to store the data
data = {
    "CEO_ID": ceo_ids,
    "District": assigned_districts,
    "Team": assigned_teams,
    "Team_Leader": assigned_team_leaders,
    "Attribute": attributes
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("ceo_data.csv", index=False)