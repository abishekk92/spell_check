import dictionary

words = open('british/brit-a-z.txt','r').readlines()

words = map(lambda word: word.strip('\r\n'), words)

dictionary.add_words(words)

print "All the words added to the dictionary"
