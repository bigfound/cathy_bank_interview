def revert_scores(scores: list):
    reverted_scores = []
    for score in scores:
        reverted_scores.append(int(str(score)[::-1]))
    return reverted_scores


if __name__ == '__main__':
    input_scores = [35, 46, 57, 91, 29]
    print('The input scores: {}'.format(input_scores))
    scores = revert_scores(input_scores)
    print('Correct the scores: {}'.format(scores))




