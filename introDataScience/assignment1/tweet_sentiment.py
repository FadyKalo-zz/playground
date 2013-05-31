import sys

def hw():
	print 'Hello, world!'
	afinnFile = open("AFINN-111.txt")
	scores={}
	for line in afinnFile:
		term, score = line.split("\t")
		scores[term]=int(score)
	print len(scores)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
