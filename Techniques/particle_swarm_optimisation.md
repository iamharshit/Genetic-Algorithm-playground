### AIM:
It is an optimisation technique i.e given a function we need to find the best possible solution.Brother of Genetic Algo.	

### Inspiration:
The algorithm is inspired from the way birds search for food in groups.

### Terminology:
* In Gen algo where the potential solutions are called "Organisms", here the potential solutions are called "Particles"(although it should have been called "Bird")

### In Layman's terms:
* A group of around 50 mettalurgists arrive in an unknown large plot of gurgaon to search for iron ore - technically speaking they want to find the best spot where if they start digging they'll find the maximum amount of iron.
* Each of them is equipped with an instrument - which tells the amount of iron present below the selected point.
* Here the mettalurgists come up with a strategy to find the best point on the plot - Each person randomly chooses a point on ground and finds the amount of iron beneath that point.
* Now, they finds the person among themselves who has the best value.In next iteration each person moves 15steps towards that person to come to a new point and again they uses the machine to  find the amount of iron beanth their point.Then they finds the person among themselves again and the process continues ......
* This is done untill they each of them comes to a single point or they reach a descent enough point or they starts sweating.
* Analogies:

    The Strategy = Particle Swarm Optimisation
 
    Mettalurgist = Particle
 
    Task = Optimum point
 
    Choosen Point = Candidate Solution
 
    Machine = Fitness function
 
    15 steps = Velocity
 
    Reach a descent enough point = minimum error criteria attained
 
    Starts sweating = Maximum iteration reached 
* Note: In actual instead of having a fixed velocity(here 15 steps) in PSO their is a formulae to calculate velocity of each particle.

### Pseudo-code :
```
For each particle
    Initialize particle
END

Do
    For each particle
        Calculate fitness value
        If the fitness value is better than the best fitness value (pBest) in history
            set current value as the new pBest
    End

    Choose the particle with the best fitness value of all the particles as the gBest
    For each particle
        Calculate particle velocity according equation 
        Update particle position according equation 
    End 
```

### References:
* Visualisation - [here](https://www.youtube.com/watch?v=_bzRHqmpwvo) & [here](https://www.youtube.com/watch?v=GMLEc5x_f30)	
* [Desi Lecture](https://www.youtube.com/watch?v=cIiwo9tMDZY)
* [Code in Matlab](https://www.researchgate.net/publication/296636431_Codes_in_MATLAB_for_Particle_Swarm_Optimization)

