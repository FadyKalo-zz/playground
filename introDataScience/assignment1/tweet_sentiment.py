#!/usr/bin/env python
import sys
import json
import urllib

def hw(sentF, tweetF):
	print 'Hello, world!'
	sent_file = open(sentF,"r")
	scores={}
	for line in sent_file:
		term, score = line.split("\t")
		scores[term]=int(score)
	print "word in the dictionary: ", len(scores)
	tweet_file = open(tweetF,"r")
	tweetList=[]
	for line in tweet_file:
		jResponse =	json.loads(line)
		if jResponse.keys()[0]!='delete':
			firstKeys=jResponse.keys()
			text=jResponse[firstKeys[firstKeys.index("text")]]
			tweetList.append(text)
	index=0
	infos=[]
	for tweet in tweetList:
		words=processTweet(tweet)
		# words=tweet.split(' ')
		# print words, unicode(words)
		points=0
		words=[w.lower() for w in words]
		for w in words:
			if w.encode('utf-8') not in scores.keys():
				points += 0;
			else:
				points +=scores[w]

		# print len(tweetList), index, points
		index += 1
		infos.append((index,points))
	toPrint= [first[1] for first in infos]
	for x in toPrint:
		print x
	# just some more infos
	# totalPoints= sum(abs(s[1]) for s in infos)
	# print totalPoints, "avg= ", float(totalPoints)/index, index

def processTweet(raw):
	from string import punctuation
	import re
	#lower case
	processed=raw.lower()
	#elminate punctuation, can compromise urls or others
	for x in punctuation:
		#substitution by space not to merge words
		processed=processed.replace(x," ")
	#compacting spaces, skip last one?
	processed=re.sub(' +',' ', processed)
	#splitting tweet into single words.
	processed=processed.split(" ")
	return processed

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1],"r")
    tweet_file = open(sys.argv[2],"r")
    hw(sys.argv[1],sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
