ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

people = {}

# Function to find winner
def winner(ballots):
    for ballot in ballots:
        # Assign number of points to each place
        for place, person in ballot.items():
            points = 0
            if place == 'gold':
                points = 3
            elif place == 'silver':
                points = 2
            elif place == 'bronze':
                points = 1

            # Tally up points for each person
            if person in people:
                people[person] += points
            else:
                people[person] = points

    # Compare scores to max score to find person with highest score
    max_score = 0
    winner = ''
    for person, score in people.items():
        if score > max_score:
            max_score = score
            winner = person
    return winner

winner = winner(ballots)
print(winner)
