from __future__ import with_statement
import time
class Point(object):

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def distance(self,p):
		return (((self.x-p.x)**2) + ((self.y-p.y)**2))**0.5

	def x(self):
		return self.__x

	def y(self):
		return self.__y

	def __repr__(self):
		return 'Point(%d,%d)' % (self.x, self.y)


def findMinDistance(arr):
	if len(arr) < 2:
		return 0,[(None,None),(None,None)]
	else:
		d1 = arr[0].distance(arr[1])
		if len(arr) == 2:
			return d1,[arr[0],arr[1]]
		else:
			d2 = arr[1].distance(arr[2])
			d3 = arr[0].distance(arr[2])
			minimumDistance = min(d1,d2,d3)
			if minimumDistance == d1:
				return d1,[arr[0],arr[1]]
			elif minimumDistance == d2:
				return d2,[arr[1],arr[2]]
			else:
				return d3,[arr[0],arr[2]]


def closestPair(pX,pY):
	delta = 0
	pairminimum = []
	yPrime = []
	pl,pr,pyl,pry = [],[],[],[]
	numberOfPoints = len(pX)
	medianPoint = (numberOfPoints/2)
	if numberOfPoints <= 3:
		return findMinDistance(pX)
	pl = pX[:medianPoint]
	pr = pX[medianPoint:]
	pmedian = pl[medianPoint-1].x
	for k in pY:
		if k.x <= pmedian:
			pyl.append(k)
		else:
			pry.append(k)
	deltal,pairl = closestPair(pl,pyl)
	deltar,pairr = closestPair(pr,pry)
	if deltal<deltar:
		delta = deltal
		pairminimum = pairl
	else:
		delta = deltar
		pairminimum = pairr
	for k in pY:
		if (((k.x-pmedian) <= delta) or ((pmedian-k.x) <= delta)):
			yPrime.append(k)
	for i in range(len(yPrime)-1):
		for j in range(i+1,min(i+8,len(yPrime))):
			if yPrime[i].distance(yPrime[j]) < delta:
				delta = yPrime[i].distance(yPrime[j])
				pairminimum = [yPrime[i],yPrime[j]]
	return delta,pairminimum

if __name__ == '__main__':
	filex = "PX.txt"
	filey = "PY.txt"
	x,y,p = [],[],[]
	pXsorted ,pYsorted = [],[]
	xfilestimer = time.clock()
	with open(r"PX.txt") as f: 
		x = f.readline().strip().lstrip("[").rstrip("]").split(", ")
	x = [int(s) for s in x]
	with open(r"PY.txt") as f: 
		y = f.readline().strip().lstrip("[").rstrip("]").split(", ")
	y = [int(s) for s in y]
	p = [Point(a,b) for a,b in zip(x,y)]
	pXsorted = sorted(p,key=lambda point: point.x)
	pYsorted = sorted(p,key=lambda point: point.y)
	countingsorttimer1 = time.clock() #Timer start
	print closestPair(pXsorted,pYsorted)
	countingsorttimer2 = time.clock() #Timer end
	print '%0.10f seconds elapsed' % (countingsorttimer2-countingsorttimer1)

