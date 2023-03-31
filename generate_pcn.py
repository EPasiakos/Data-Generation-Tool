#This python script generates a csv file with 80000 rows of data for the PCN data set for the project "PCN Data Analysis"
#The data is generated randomly and is not based on any real data set or any real world scenario.
#The data is generated using the following assumptions: 
#1. The CEO ID is randomly selected from a list of CEO IDs that are valid for the city of London.
#2. The CEO ID is used to determine the district of the CEO.
#3. The district is used to determine the zone of the CEO.
#4. The PCN number is randomly generated between 10000 and 99999.
#5. The date of issue is randomly generated between 1st January 2022 and 31st February 2023.
#6. The time of issue is randomly generated between 7:00 AM and 10:00 PM.
#7. The PCN status is randomly selected from the list of PCN statuses with a 80% chance of being "paid" and 20% chance of being "cancelled".
#8. The data is saved to a csv file named "pcn_data.csv" in the same directory as the python script.
#9. The csv file has the following columns: CEO ID, PCN Number, Date of Issue, Time of Issue, Zone, PCN Status.
#10. The csv file has a header row with the column names.
#11. The csv file is saved in the same directory as the python script.
#12. The csv file is saved with the following encoding: utf-8-sig.
#13. The csv file is saved with the following delimiter: ",".


import csv
import random
from datetime import datetime, timedelta

# Constants
ceo_ids = [
    13, 48, 63, 74, 100, 111, 115, 139, 164, 168, 198, 213, 228, 237,
    249, 262, 264, 287, 310, 316, 330, 344, 362, 369, 374, 406, 410, 412, 418,
    446, 447, 452, 472, 506, 518, 558, 627, 654, 683, 685, 704, 746, 756,
    768, 772, 789, 826, 827, 832, 843, 901, 953, 989, 998
]

ceo_districts = {
    13: "North", 48: "Central", 63: "South", 74: "North", 100: "Central", 111: "North", 115: "Central", 139: "South",
    164: "North", 168: "Central", 198: "North", 213: "Central", 228: "South", 237: "North", 249: "Central",
    262: "South", 264: "North", 287: "Central", 310: "South", 316: "North", 330: "Central", 344: "South",
    362: "North", 369: "Central", 374: "South", 406: "North", 410: "Central", 412: "South", 418: "North",
    446: "Central", 447: "South", 452: "North", 472: "Central", 506: "South", 518: "North", 558: "Central",
    627: "South", 654: "North", 683: "Central", 685: "South", 704: "North", 746: "Central", 756: "South",
    768: "Central", 772: "South", 789: "North", 826: "South", 827: "North", 832: "Central", 843: "South",
    901: "North", 953: "South", 989: "Central", 998: "South"
}

district_zones = {
    "North": ["G", "M", "R", "T", "U", "S"],
    "Central": ["C", "D", "J", "K", "L", "N", "P"],
    "South": ["A", "B", "E", "F", "H", "Q"]
}

team_leaders = {
    "Patrick": [139, 262, 374, 506, 756, 843],
    "Andrew": [228, 344, 447, 685, 826, 998],
    "Sandra": [63, 310, 412, 627, 772, 953],
    "Emiru": [115, 249, 369, 472, 746, 832],
    "Paul": [13, 164, 264, 406, 518, 901],
    "Naz": [74, 198, 316, 418, 654, 789],
    "Michael": [111, 237, 362, 452, 704, 827],
    "Anna": [48, 168, 287, 410, 558, 768],
    "Nick": [100, 213, 330, 446, 683, 989],
}


start_date = datetime.now() - timedelta(days=365)

# Helper functions
# Generate a random time between 7:00 AM and 11:00 PM
# The time is returned as a string in the format "HH:MM"
def random_time():
    return "{:02d}:{:02d}".format(random.randint(7, 23), random.randint(0, 59))

# Generate a random date between 1st January 2022 and 20st March 2023
def random_date():
    return (start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")

# Generate a random zone for a given district using the district_zones dictionary above as a lookup table.
def random_zone(district):
    return random.choice(district_zones[district])

# Generate a random PCN status using a 80% chance of being "paid" and 20% chance of being "cancelled"
# The PCN status is returned as a string
def random_pcn_status():
    return "paid" if random.random() < 0.8 else "cancelled"


# Get the team leader for a given CEO ID using the team_leaders dictionary above as a lookup table.
def get_team_leader(number, team_leaders):
    for leader, numbers in team_leaders.items():
        if number in numbers:
            return leader
    return None

# Generate data.
data = []
for _ in range(80000):  # Generate 80000 rows of data
    ceo_id = random.choice(ceo_ids)
    pcn_number = random.randint(10000, 99999)
    date_of_issue = random_date()
    time_of_issue = random_time()
    district = ceo_districts[ceo_id]
    zone = random_zone(district)
    team_leader = get_team_leader(ceo_id, team_leaders)
    pcn_status = random_pcn_status()

    data.append([ceo_id, pcn_number, date_of_issue, time_of_issue, district, zone, get_team_leader(ceo_id, team_leaders), pcn_status])

# Save data to a CSV file
with open("pcn_data.csv", mode="w", newline='') as csv_file:
    fieldnames = ["CEO ID", "PCN Number", "Date of Issue", "Time of Issue", "District", "Zone", "Team Leader", "PCN Status"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow({"CEO ID": row[0], "PCN Number": row[1], "Date of Issue": row[2],
                     "Time of Issue": row[3], "District": row[4], "Zone": row[5], "Team Leader": row[6], "PCN Status": row[7]})


