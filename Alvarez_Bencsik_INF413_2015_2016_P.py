# -*- coding: utf-8 -*-
#
#
# Date: 
#
#
_author_="Alvarez Paulina, Bencsik Andrei"
_version_="1.0"

 
import random
import sys
import os
import io
###############################################################################
##################### Define the constants ####################################
MaxK = 10
MAX_ITERS = 3000
MaxN = 1000
flag = False
flag_count = 0
###############################################################################
####################### Classes ###############################################
###############################################################################
class Cluster:
	"""
		A cluster is a group of points 
		it has a center and a list of points,
		as well as an ID
		
		The center and points list are using the
		@CLASS Point
		
	"""
	def __init__(self, center = None, points = []):
		"""
		@CONSTRUCTOR
		@params: 	center = a Point (default: None)
					points = List of Point (default [])
		"""
		self.points = list(points)
		self.center = center
		# at creation all centroids have id -1
		self.cid = -1
		
	def set_id(self, cid):
		"""
		@SETTER
		@params: cid = Centroid Id 
		"""
		self.cid = cid
		
	def get_id(self):
		"""
		@GETTER
		@return: cid = Centroid Id 
		"""
		return self.cid
		
	def set_center(self, center):
		"""
		@SETTER
		@params: center = Centroid Center 
		"""	
		self.center = center
		
	def get_center(self):
		"""
		@SETTER
		@params: cid = Centroid Id 
		"""
		return self.center
		
	def add_point(self, point):
		"""
		@Helper method to add point to a cluster
		@params: point = Point to add to the cluster
		"""
		# print "Add point called"
		self.points.append(point)
	
	def remove_point(self, point):
		"""
		@Helper method to remove a point from cluster
		@params: point = Point to remove from the cluster
		"""		
		self.points.remove(point)
		
	def update_centroid(self):
		"""
		@Helper method to recompute the center
		@params: 
		@effect: 
		"""	
		# self.center = 
		mean_coords = [0 for i in xrange( self.center.get_len() )]
		for pt in self.points:
			for c in xrange( pt.get_len() ):
				mean_coords[c] += pt.coords[c]
		for i in xrange( self.center.get_len() ):
			try:
				mean_coords[i] /= len( self.points )
			except ZeroDivisionError:
				return
		self.center = Point(mean_coords)
		
	def intra_distance(self):
		"""
		@Helper method to compute intra cluster mean distance
		@return: the average distance within the cluster
		"""	
		sums = 0.0
		for pt in self.points:
			
				sums += pt.distance(self.center)
		# avoid division by 0
		if len(self.points):
			return sums / len(self.points)
	
	def __str__(self):
		"""
		@Override: toString method
		@return: structured information on cluster
		"""	
		rtstring = "Cluster with id: " + str( self.get_id() ) + "\nCenter : " + str( self.center ) + "\nPoints"
		for pt in self.points:
			rtstring += "[ " + str( pt ) + " ] "
		return rtstring
	
	
	

class Point:
	"""
		Class Point: V 1.0
		
		Contains the definition of a point 
		Attributes:
			coords - the coordinates of a point
			cluster - the cluster ID it is in 
					(at start all are in -1)
		Methods:
			distance - computes distance to 
						another Point
			
	"""
	cluster = -1
	
	def __init__(self, coords= []):
		self.coords = coords
	
	def __str__(self):
		return "Point " + str(self.coords)
		
	def get_len(self):
		return len(self.coords)
	# euclidian
	def distance(self, point):
		summ = 0
		# print str(point) + "compared to " + str(self.coords)
		try :
			for i in xrange( point.get_len() ):
				summ += (self.coords[i] - point.coords[i])**2
			return summ ** 0.5
		except IndexError:
			print "The points don't have the same number of attributes"
			return None
	
###############################################################################
# FUNCTION
###############################################################################
def choose_cluster(point, clusters):
	"""
		Update the cluster for the given point
		Compute the distances and finds the 
		Cluster that is closest
		
		@effect: moves a Point from a Cluster
				if it is closer to its center
	"""
	distances =[]
	global flag
	global flag_count	
	for i in xrange( len(clusters) ):
		distances.append( point.distance( clusters[i].get_center() ) )
	
	minindex = distances.index ( min( distances ) )
	# print "Adding point .." + str(point) + " to centroid " + str(minindex)
	clusters[minindex].add_point( point )
#	for ct in centroids:
#		print " ## " + str( ct ) + "##"
	
	for ct in clusters:
		if (ct.get_id() == point.cluster) and (point in ct.points):
			ct.remove_point(point)
			break
	if point.cluster != clusters[minindex].get_id():
		flag = True	
		flag_count = 0
	point.cluster = clusters[minindex].get_id()

"""
    Get the K from the user, if user enters randomK, generate
    
    @param: argv - the list of command line arguments 
    
    @return: k - number of clusters for K-means
    
    @error: 0 - k is set to 0
"""
def get_k(argv):
	if len(argv) >= 2:
		# If not, we take a k between 2 and MaxK(predefined in codes) randomly:
		if str(argv[1]).lower() == 'randomk':
			k = random.randrange(2, MaxK)
			print 'Using random k =  ' + str(k)
			return k
		# If the k is given by the user:
		elif int(argv[1]) > 0:
			k = int(argv[1])
			print 'Using user k  = ' + str(k)
			return k
		else:
			return 1
	else:
		print "!ERROR!\n{User did not input correctly, k is 0!!}\n"
		return 0

def get_data(argv):
	if len(argv) >= 3:
		# If not, we take a k between 2 and MaxK(predefined in codes) randomly:
		if str(argv[2]).lower() == 'randomdata':
			io.write_data( io.generate_random_data(random.randrange( 2, MaxN ) , random.randrange( 2, MaxK )) , "input_random.csv")
			print 'Using random k =  ' + str(k)
			return "input_random.csv"
		else:
			return argv[2]
			
	else:
		print "!ERROR!\n{User did not input correctly, k is 0!!}\n"
		return 0

def list2set(aList):
	_set = set()
	for ll in aList:
		for el in ll:
			_set.add( el )
	return _set
###############################################################################
########################## TESTS ##############################################
###############################################################################
def kmeans():
    pass    

###############################################################################
######################## TESTS END ############################################
###############################################################################

###############################################################################
######################### Main ################################################
###############################################################################

# Be sure that user enters correct params to the CL
if len(sys.argv) < 3:
    print '''!ERROR!\n[Usage: python ''' + sys.argv[0] + ''' integer for K/'randomk'  InFile/'RandomData'  OutFile]\nPlase try again.\nExiting...'''
    exit(0)
# get K from either the input or generate it randomly
k = get_k(sys.argv)
# get the data from the file
print sys.argv[2]
data, labels = io.read_data( get_data( sys.argv ) )

# print len( list2set(data) ) 


points = []
for dt in data:
	pt1 = Point(dt)
	points.append( pt1 )
temp = Cluster(points[0], points[:50])

temp.update_centroid()

print " Center of first " + str( temp.center.coords)

# centers set
centers = set()
while len( centers ) < k:
	centers.add( random.choice( points ) )
# Pick out k random points to use as our initial centroids
# initial = random.sample(points, k)
#centers.add ( points[63])
#centers.add ( points[53])
#centers.add ( points[74] )

# list of centroids
clusters = []
counter = 0
for cent in centers:
	clusters.append( Cluster( cent ) )
	clusters[-1].set_id( counter ) 
	counter += 1
############################################
for i in xrange( MAX_ITERS ):
	flag = False
	
	for ctrd in clusters:
		# print the centroid and its intradistance
		print "Cluster no. " + str(ctrd.get_id())
		print ctrd.intra_distance()
		ctrd.update_centroid()
	# for each point , update the centroid
	for pt in points:
 		choose_cluster( pt, clusters )
 	# id no points change centroid, stop
	if not flag:
		flag_count += 1
		print "Iterations: " + str(i)
		if flag_count >= 5:
			break
	print ""
# now compute centroid for each point
#  for pt in points:
# 	choose_centroid( pt, centroids )

# pt1 = Point( data[7] )
# centroid.add_point( pt1 )

# print the number of points in each centroid
for ctrd in clusters:
	print "Cluster # " + str( ctrd.get_id() )
	print "Center " + str (ctrd.center.coords)
	#for pt in ctrd.points:
		#print pt.coords,
		#print " dist  " + str (pt.distance( centroids[0].center ) )+  " " +  str (pt.distance( centroids[1].center ) ) + " " + str (pt.distance( centroids[2].center ) )
	print len(  ctrd.points  )
# write points and their cluster ID to file 
if len(sys.argv) < 4:
	f = open("output.csv", "w")
else:
	f = open(sys.argv[3], "w")
f.write("# The coordinates of the points and the cluster they are in\n")
for pt in points:
	f.write( str( pt.coords ) + " | Cluster id: " + str( pt.cluster ) + "|\n") 
f.close()
# write centers and their cluster ID to file 
f = open("centers.csv", "w")
f.write("# The coordinates of the centers\n")
for ct in clusters:
	f.write( str( ct.center.coords ) + " | Cluster id: " + str( ct.get_id() ) + "|\n") 
f.close()

print "flag count at end " + str(flag_count)

