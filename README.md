# reinforcement-learning-policy-evaluation
This repo contains a simulation of policy evaluation algorithm on a Stochastic Markov Decision Process. It is part of a the course COMPSCI 687: Reinforcement Learning. 
A given policy $\pi(s,a)$ is chosen and the performance of that policy is estimated by running the agent on the environement. 

We also randomly chose policies and test their performance. By searching in a sufficiently large set of policies, we can find an optimal policy. 


## Requirements
Need python on your machine to run this code. 

## 

To run the program, enter the following commands: 

$python simulation.py <policy_num> <gamma>

<policy_num> : Can be either 1 or 2. 
1 for Q1's stochastic policy. Runs the policy for 150000 episodes and prints the J-estimate at the last step
2 for Q2's random policies. Generates a random deterministic policy and averages the G for 100 times. This is done N times where N varies from 1 to 250. Selects the best policy along with the reward for N=250 and prints it in the end. 

<gamma> : real number between 0 and 1. 
The discount rate of the MDP


MDP.py consists of the MDP class.


The MDP configuration is stored in MDP.txt and the stochastic policy is stored in policy.txt which the program reads from to simulate. These can be updated as needed.

A run of Q1 was generated and the results were stored in Gs.txt. These were used to plot the graphs in "Plotting Results.ipynb" Jupyter Notebook. 
Similarly for Q2d, "Q2_stats.txt" were generated and used to plot the graphs. 

"runs.txt" contains a few hundred thousand runs of the 1st policy which one may look if interested.

