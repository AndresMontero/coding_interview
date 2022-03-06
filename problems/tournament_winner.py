def tournamentWinner(competitions, results):
    # Write your code here.
    # Time O(n) -> n is hte number of competitions
    # Space O(k) -> k is the number of teams for the dict
    scores = {}

    for t1, t2 in competitions:
        if t1 not in scores:
            scores[t1] = 0
        if t2 not in scores:
            scores[t2] = 0

    for i in range(len(results)):
        if results[i] == 0:
            scores[competitions[i][1]] += 3
            scores[competitions[i][0]] += 0

        else:
            scores[competitions[i][0]] += 3
            scores[competitions[i][1]] += 0

    winner = max(scores, key=scores.get)
    return winner


if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]

    print(tournamentWinner(competitions, results))
