from matchmaking_engine.matchmaking_algos.basic_algo.distance import calculate_distance


def calculate_match_score(user1, user2):
    # Check gender preferences
    if (user1.preferences['gender'] and user1.preferences['gender'] != user2.gender) or \
       (user2.preferences['gender'] and user2.preferences['gender'] != user1.gender):
        return 0  # No match based on gender preference

    # Calculate age difference
    age_diff = abs(user1.age - user2.age)
    if age_diff < user1.preferences['age_range'][0] or age_diff > user1.preferences['age_range'][1]:
        return 0  # Outside preferred age range

    # Calculate distance
    distance = calculate_distance(user1.location, user2.location)
    if distance > user1.preferences['distance']:
        return 0  # Outside distance preference

    # Calculate interest similarity
    common_interests = set(user1.interests).intersection(set(user2.interests))
    interest_score = len(common_interests) / max(len(user1.interests), len(user2.interests))

    # Final score (you can tweak weights as needed)
    score = 0.5 * (1 - age_diff / 100) + 0.3 * interest_score + 0.2 * (1 - distance / 100)
    return score
