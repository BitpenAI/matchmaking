from matchmaking_engine.matchmaking_algos.basic_algo.scoring import calculate_match_score


def find_matches(user, all_users):
    potential_matches = []
    for potential_user in all_users:
        if potential_user.user_id != user.user_id:  # Exclude self
            score = calculate_match_score(user, potential_user)
            if score > 0:  # Only consider non-zero scores
                potential_matches.append((potential_user, score))
    
    # Sort matches by score in descending order
    potential_matches.sort(key=lambda x: x[1], reverse=True)
    return potential_matches
