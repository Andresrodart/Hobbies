from collections import Counter

def evenArtist(zipTrpup, numArtist):
	acro = clwns = 0
	arrRes = []
	pairsCounted = Counter(zipTrpup)
	players = numArtist//2
	print(pairsCounted)


if __name__ == '__main__':
	numArtist 	= int(input())
	zipTrpup 	= zip(input(), input())
	result		= evenArtist(zipTrpup, numArtist)
