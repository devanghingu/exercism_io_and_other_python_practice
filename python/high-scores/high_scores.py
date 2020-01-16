def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores,reverse=True)[0]


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
