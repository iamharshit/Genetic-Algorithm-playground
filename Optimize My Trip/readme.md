## Optimise Trip

Being a student myself there are many times we face problem of Visiting the best places nearby with minimal amount of expenditure.
I tried to solve this multi-objective optimisation problem using Genetic Algorithm where we maximze the number of state capitals visited and simultaneously minimize the total cost incured.Instead of exhaustively looking at every possible solution, genetic algorithms start with a handful of random solutions and continually tinkers with these solutions — always trying something slightly different from the current solutions and keeping the best ones — until they can’t find a better solution any more.Although Gen algo may not give the best solution but it gives resonably good solutions.
The solutions assumes that there is no traffic(ofcourse,not possible in India :) ) and cost of travelling is directly propotional to distance travelled.


### Why Genetic Algo?
Rather then going for brute-force which then would be an NP-Hard problem exactly the way as standard Travelling Salesman problem hence we go for evolutionary algorithm.
Although the standard Gen algo approach have 3 steps Reproduction-> CrossOver-> Mutation, Here no crossover is done because crossover would be meaningless here.

### Basic Usage
* Decide on which places you wanna visit and subsitute them in list named `Citys`.
* Get your Google Maps API key as explained [here](https://github.com/googlemaps/google-maps-services-python#api-keys) and insert it in optimize_trips.py file.
* Run `optimize_trip.py`

### References
* [Deap Simple Tutorial](https://thesesergio.wordpress.com/2013/05/31/deap-a-self-made-tutorial-12/)

