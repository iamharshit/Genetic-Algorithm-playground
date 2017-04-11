## Human vs Robot 

This is project from the usual talk on "will Robots kill humans?".I try to simulate those conditions using Simple Prey-Predator algorithm.Here the human is the prey and Robots is predator.

### Rules for simulation

Both creatures live in 20*20 grid of cells.One creatue occupy cell at a time.Each creature perform some action every time step.
<b>Human Behaviour</b> 
* Human randomly move up/down/left/right.But if the neighboring cells are occupied then ant doesn't move.
* If a human survives for 3 timesteps then it produces an offspring in the randomly choosen adjacent cell that is empty.The same continues.

<b>Robot Behaviour</b>
* Robot moves to an adjacent cell coontaining an human and kills him.If no human present then it moves randomly to a randomly choosen adjacent empty cell.
* If an Robot lives for 8 time steps then it manufactures another Robot.
* If an Robot has not killed human for more then 3 timesteps then it is considered as defected and it performs self execution.

### Status
The project is currently under the working phase.
