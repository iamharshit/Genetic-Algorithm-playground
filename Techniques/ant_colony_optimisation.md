### AIM:
An optimisation technique

### Inspiration:
The way ant expore their enviornment for food.The magic is "Ant are blind" still they efficiently moves in the enviornment.

### Strategy:
Ant solve that problem by- At first, the ants wander randomly. When an ant finds a source of food, it walks back to the colony leaving "markers" (pheromones) that show the path has food. When other ants come across the markers, they are likely to follow the path with a certain probability. If they do, they then populate the path with their own markers as they bring the food back. As more ants find the path, it gets stronger until there are a couple streams of ants traveling to various food sources near the colony.

Because the ants drop pheromones every time they bring food, shorter paths are more likely to be stronger, hence optimizing the "solution."

![img](http://www.projects.science.uu.nl/urbanbiology/antfig5.png)


GARBAGE NOTE: Ant communicate through touching each other,producing work specific smell and other ant recieving that smell, marking a path with chemical signal. They decide their movement pattern based on individual interaction.

### Pseudo-Code:
```
Best Solution = GenerateRandomSolution()

Do
    For each Ant
       Candidate solution = ConstructSolution(BestSolution, My problem)
       If Candidate solution is better then Best solution
       		set Best solution as Candidate solution
    End

```
Note: The probabilistic step-wise construction of solution makes use of both history (pheromone) and problem-specific heuristic information to incrementally construct a solution piece-by-piece.

### Application:

* Exploring a enviornment in shortest amount of time - Travelling Salesman problem or Robot exploring an enviornment eg. The Curosity rover on Mars.
* Scheduling Computing Tasks

### References:

* Introductory Vedios on how ant behaves - [here](https://www.youtube.com/watch?v=vG-QZOTc5_Q) & [here](https://www.youtube.com/watch?v=7s16f2fmkEw)
* [Code](www.cleveralgorithms.com/nature-inspired/swarm/ant_colony_system.html)
