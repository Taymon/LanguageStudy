def process(originals, point_words, result):
    without_pw = [w for w in originals if w not in point_words]
    
    for wp in without_pw:
        clone_pw = point_words[:]
        clone_pw.append(wp)
        result.append(clone_pw)
        process(originals, clone_pw, result)

def start(words):
    result = []

    for w in words:
        process(words, [w], result)

    for r in result:
        print (r)


start(['A','B','C'])

