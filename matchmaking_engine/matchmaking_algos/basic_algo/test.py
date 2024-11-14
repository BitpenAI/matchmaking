from matchmaking_engine.matchmaking_algos.basic_algo.matching import find_matches
from matchmaking_engine.matchmaking_algos.mock_user_data.user import User


user1 = User(1, "Alice", 25, "female", (37.7749, -122.4194), ["hiking", "reading", "music"])
user2 = User(2, "Bob", 27, "male", (37.8044, -122.2711), ["music", "sports", "travel"])
user3 = User(3, "Charlie", 30, "male", (37.6879, -122.4702), ["cooking", "music", "reading"])

all_users = [user1, user2, user3]

matches_for_alice = find_matches(user1, all_users)
for match, score in matches_for_alice:
    print(f"Match: {match.name}, Score: {score}")
