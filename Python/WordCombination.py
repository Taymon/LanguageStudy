def process(originals, point_words, results):
    without_pw = [w for w in originals if w not in point_words]
    
    for wp in without_pw:
        clone_pw = point_words[:]
        clone_pw.append(wp)
        results.append(clone_pw)
        process(originals, clone_pw, results)

def start(words):
    results = []

    for w in words:
        process(words, [w], results)

    for r in results:
        print (r)


start(['A','B','C'])

