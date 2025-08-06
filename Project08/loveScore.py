def calculate_love_score(name1, name2):
    trueScore = 0
    loveScore = 0
    bigger = max(len(name1), len(name2))
    for i in range(bigger):
        if i < len(name1):
            if name1[i].lower() in 'true':
                trueScore += 1
            if name1[i].lower() in 'love':
                loveScore += 1
        if i < len(name2):
            if name2[i].lower() in 'true':
                trueScore += 1
            if name2[i].lower() in 'love':
                loveScore += 1
    print(f'{(str(trueScore))}{(str(loveScore))}')

calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("love", "")
