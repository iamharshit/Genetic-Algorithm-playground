import googlemaps #for getting distances
import itertools #for PnC
import pandas as pd 
import numpy as np
from deap import creator #for Gen-algo
from deap import tools
from deap import base
from deap import algorithms 
import random
import csv

gmaps = googlemaps.Client(key='AIzaSyC8eX8ttiPZSwQiYw1vsIVdw5IuXthTIh4')

citys = ['New Delhi', 'Hyderabad', 'Itanagar', 'Dispur', 'Patna', 'Raipur', 'Panaji', 'Gandhinagar', 'Chandigarh', 'Shimla', 'Srinagar', 'Ranchi', 'Bengaluru', '	Thiruvananthapuram', 'Bhopal', 'Mumbai', 'Imphal', 'Shillong', 'Aizwal', 'Kohima', 'Bhubaneshwar', 'Jaipur', 'Gangtok', 'Chennai', 'Agartala', 'Lucknow', 'Dehradun', 'Kolkata']

city1='New Delhi'
city2='Mumbai'

durations = {}
distances = {}

#Computing Distances
for (city1,city2) in itertools.combinations(citys,2):
	try:
		route = gmaps.distance_matrix(origins=[city1],destinations=[city2], mode='driving',language='English',units='metric')
	
		#dist in meters and dur in secs
		dist = route['rows'][0]['elements'][0]['distance']['value']	
		##dur = duration = route['rows'][0]['elements'][0]['duration']['value']
		print dist	
		distances[frozenset([city1, city2]) ] = dist
		##durations[frozenset([city1, city2]) ] = dur
	
	except Exception as e:
		print 'Unable to find distance between '+city1+' '+city2

#Storing Distances in .csv file for future reference
with open('city-distances.csv','w') as f:
	fwriter = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)	
	fwriter.writerow(['city1', 'city2', 'distance'] )
	
	for (city1,city2) in distances.keys():
		fwriter.writerow([city1, city2, str(distances[frozenset([city1,city2])] )])	
		
#Gen algo

#creates a new class inheriting from the base class
#-1.0 for minimisation of money and +1.0 for maximisation of cities visited
creator.create('FitnessMulti', base.Fitness, weights=(-1.0,1.0))

#The individual has the fitness attribute which specifies its fitness value
creator.create('Individual', list, fitness=creator.FitnessMulti)

#Toolbox is container of tools of all sorts
toolbox = base.Toolbox()
#registering the method under the toolbox with the alias name
#random.sample does random sampling from `citys` list
toolbox.register('select_citys', random.sample, citys, random.randint(2,20) )

#For iterating through all the samples in the previous stage
#Each individual is a fully planned trip
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.select_citys)

#the method population specifies the no. of times the method toolbox.individual would be called
#Storing results from every repeat constructs population
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

def eval_trip(individual):
	'''
		Returns total citys visited and total distance travelled
	'''
	total_dist = 0
	
	#Changing container and Making trip as round trip
	individual = list(individual)
	individual += individual[0]

	for i in range(1, len(individual)):
		city1, city2 = individual[i-1], individual[i]
		dist =  distances[frozenset(city1, city2)]
		total_dist += dist

	return len(individual), total_dist

def selection_operator(individuals, k):
	'''
		Selects road trip for next generation from current generation favoring trips with lower total distance and more cities visited.
		K denotes how many selection needs to be done
	'''
	return tools.selNSGA2(i, int(k/5.))*5 

def mutation_operator(individual):
    '''
		Mutates one road trip for reaching global minima.
		Applies a random change to one road trip:        
            - Insert: Adds one new city to the road trip
            - Delete: Removes one city from the road trip
            - Point: Replaces one city with another different one
            - Swap: Swaps the places of two city in the road trip
    '''
    possible_mutations = ['swap']
    
    if len(individual) < len(all_waypoints):
        possible_mutations.append('insert')
        possible_mutations.append('point')
    if len(individual) > 2:
        possible_mutations.append('delete')
    
    mutation_type = random.sample(possible_mutations, 1)[0]
    
    # Insert mutation
    if mutation_type == 'insert':
        waypoint_to_add = individual[0]
        while waypoint_to_add in individual:
            waypoint_to_add = random.sample(all_waypoints, 1)[0]
            
        index_to_insert = random.randint(0, len(individual) - 1)
        individual.insert(index_to_insert, waypoint_to_add)

    # Delete mutation
    elif mutation_type == 'delete':
        index_to_delete = random.randint(0, len(individual) - 1)
        del individual[index_to_delete]
    
    # Point mutation
    elif mutation_type == 'point':
        waypoint_to_add = individual[0]
        while waypoint_to_add in individual:
            waypoint_to_add = random.sample(all_waypoints, 1)[0]
        
        index_to_replace = random.randint(0, len(individual) - 1)
        individual[index_to_replace] = waypoint_to_add
        
    # Swap mutation
    elif mutation_type == 'swap':
        index1 = random.randint(0, len(individual) - 1)
        index2 = index1
        while index2 == index1:
            index2 = random.randint(0, len(individual) - 1)
            
        individual[index1], individual[index2] = individual[index2], individual[index1]
    
    return individual

#registering the above functions as toolbox methods with standard names
toolbox.register('evaluate', eval_trip)
toolbox.register('mutate', mutation_operator)
toolbox.register('select', selection_operator)

#randomly initialising population of 100
populaton_ = toolbox.population(n=1000)
#selecting pareto optimal population as Hall of Fame
hof = tools.ParetoFront(similar=pareto_eq)

#Statistics part
stats = tools.Statistics(lambda ind: (int(ind.fitness.values[0]), round(ind.fitness.values[1], 2)))
stats.register('Minimum', np.min, axis=0)
stats.register('Maximum', np.max, axis=0)
# This stores a copy of the Pareto front for every generation of the genetic algorithm
stats.register('ParetoFront', lambda x: copy.deepcopy(hof))

#Specifying the total generations and Using "Simple Evolutionary Algorithm" as our gen-algo 
total_gens = 5000
pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0., mutpb=1.0, ngen = total_gens, stats=stats, halloffame=hof, verbose=False)

#printing the selected places
print hof


