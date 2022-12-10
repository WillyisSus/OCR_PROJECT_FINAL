import yake

with open ('output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

if len(text) > 100:
    max_ngram_size = 5
    deduplication_threshold = 0.4
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)

    f = open('webSearch.bat', 'w', encoding="utf-8")

    writeString = "https://www.google.com/search?q="
    for kw in keywords:
        writeString += str(kw[0]) + ' '
    writeString = "start " + writeString.replace(' ', '+')
    f.write(writeString)
else:
    f = open('webSearch.bat', 'w', encoding="utf-8")
    writeString = "https://www.google.com/search?q=" + text
    writeString = "start " + writeString.replace(' ', '+')
    f.write(writeString)