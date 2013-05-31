#!/usr/bin/env python
import urllib
import json

def getTweets(key, pages, verbose):
	root = "http://search.twitter.com/search.json"
	tweettList=[]
	for i in range(1,11):
		if verbose:
			print "retrieving page: ",i
		response = urllib.urlopen(root+"?q="+keyword+"&page="+str(i))
		jsonResponse= json.load(response)
		resultKey = jsonResponse.keys()
		nextPage=jsonResponse[resultKey[resultKey.index("next_page")]]
		listResults=jsonResponse[resultKey[resultKey.index("results")]]
		for x,y in enumerate(listResults):
			thisTweet=[]
			innerKeys = listResults[x].keys()
			for i in innerKeys:
				innerElement=listResults[x][i]
				thisTweet.append(innerElement)
			tweettList.append(thisTweet)
		if verbose:
			print "total tweets so far: ",len(tweettList)
	return tweettList

numPages = 10
keyword='microsoft'
myList=getTweets(keyword, numPages, True);
print len(myList)
