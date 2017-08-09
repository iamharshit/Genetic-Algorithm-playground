### AIM:
To find the optimum solution from large search space.

### Terminology:
Candidate solutions are called "Agents".We say that agents are moved in the search space from one position to another.

### Pseudo-code:
```
For each Agent
    Initialize Agent with position
END

Do
	 For each Agent
		 Compute New Position using a formulae
		 if Fitness(new position) is better then Fitness(old position)
			 Update Agent's Position
    End

```

### References:
* [DE package/library](http://www1.icsi.berkeley.edu/~storn/code.html) and [Code](https://en.wikipedia.org/wiki/Differential_evolution)
* [Original Reaseach Paper](http://jaguar.biologie.hu-berlin.de/~wolfram/pages/seminar_theoretische_biologie_2007/literatur/schaber/Storn1997JGlobOpt11.pdf)
