## EvoNN

In Evolutionary Neural Network we have a population of neural networks with different set of hyper-parameters and we use genetic algorithms to choose the best between those.

### Describing Bestness

The bestness is defined by maitaining a trade-off between the "Training Error" and "Complexity" given fixed no. of iterations.We know as complexity decreases the training error would increase.So we would get a Pareto-front something like below.

![pareto front img](http://www.mdpi.com/energies/energies-09-00982/article_deploy/html/images/energies-09-00982-g002.png)

From that we need to use the "Akaike" information criterian to choose select one point.

### What Hyper-parameters?

The core structure of all the neural-net is same which:

![neural net img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Colored_neural_network.svg/300px-Colored_neural_network.svg.png)

i.e with only 3 layers, also it is not necessary that 2 cinsective layers are necessarily fully-connected.Additinal layers are absent to avoid over-fitting.

Hyper-parameters here basically are:
* Different number of nodes in the hidden layer.
* Since it is not fully connected neural net, hence configuration of edges between 2 layers are different.

### Selecting best hyperparameters
A population of these neural nets are optimised using genetic algorithms specifically i.e Selection-> Cross-over-> Mutation is done, we use Ant-colony optimisation technique to choose the best hyperparameters.
