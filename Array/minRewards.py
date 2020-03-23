'''
    From a list of score distribute rewards following the rules
    1 - all score must receive at least one reward
    2 - any given score must receive more rewards than the adjacent one
        with a lower score and must receive less rewards than the adjacent
        one with higher score
    3 - all scores are unique
'''
def minRewards(score):
    rewards  = [1 for _ in score]
    for i in range(1, len(score)):
        if score[i] > score[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed((range(len(score) - 1))):
        if score[i] > score[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
    return (sum(rewards), rewards)

print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))