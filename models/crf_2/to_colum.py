from os.path import join, dirname


def to_column(sentence):
    words = []
    result = []
    path = join(dirname(__file__), "punctuation.txt")
    punctuations = open(path, "r").read().split("\n")
    for punctuation in punctuations:
        punctuation = unicode(punctuations)
    for word in sentence.split(" "):
        words.append(word)
    if words[0] == "":
        words.pop(0)
    for word in words:
        tokens = []
        if word in punctuations:
            result.append((word, "O"))
        else:
            for token in word.split("_"):
                tokens.append(token)
            for i in range(len(tokens)):
                if i == 0:
                    if tokens[i] != "":
                        result.append((tokens[i], "BW"))
                else:
                    result.append((tokens[i], "IW"))
    return result
