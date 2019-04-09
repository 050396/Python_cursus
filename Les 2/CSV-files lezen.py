with open('gamers.csv', 'r') as file:
    scores = []
    for line in file.readlines():
        naam, datum, score = line.rstrip().split(';')
        scores.append([score, [datum, naam]])
    hoogsteScore = max(scores)
    print('De hoogste score is: {} op {} behaald door '
            '{}'.format(hoogsteScore[0], hoogsteScore[1][0], hoogsteScore[1][1]))