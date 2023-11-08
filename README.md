# reinforcement-learning-policy-evaluation
This repo contains a simulation of policy evaluation algorithm on a Stochastic Markov Decision Process. It was part of a course assignemnt from the course COMPSCI 687: Reinforcement Learning at the University of Massachusetts, Amherst in Fall 2023.

A given policy $\pi(s,a)$ is chosen and the performance of that policy is estimated by running the agent on the environement. 

We also randomly chose policies and test their performance. By searching in a sufficiently large set of policies, we can find an optimal policy. 


## Requirements
Need python on your machine to run this code. 

## How to run the program
To run the program, enter the following commands: 

`python simulation.py <policy_num> <gamma>`

`<policy_num>` : Can be either 1 or 2. 

1 for Q1's stochastic policy. Runs the policy for 150000 episodes and prints the J-estimate at the last step

2 for Q2's random policies. Generates a random deterministic policy and averages the $G$ for 100 times to estimate the $J$ of the policy $\pi$. This is done N times where N varies from 1 to 250. Selects the best policy along with the reward for N=250 and prints it in the end. 

`<gamma>` : real number between 0 and 1. 
The discount rate of the MDP

## File Structure

MDP.py consists of the MDP class.

The MDP configuration is stored in [MDP.txt](/MDP.txt) and the stochastic policy is stored in policy.txt which the program reads from to simulate. These can be updated as needed.
MDP

### MDP.txt structure
Line 1: All states

Line 2: All possible actions

Line 3: Ending states

Lines containing d_0: Initial Probability $d_0$(s) = Pr [ $S_0$ = $s$ ]

Lines containing p:     Transition Probability $p(s,a,s')$ = Pr[ $S_{t+1}$  = $s'$ | $S_t$ = $s$ , $A_t$ = $a$]

Lines containing R: Reward  Funtion $R(s,a)$ is Reward generated at state $s$ when action $a$ was taken. 

The following MDP was chosen as the environment in which the policy was evaluated. 

![image](https://github.com/ojasraundale/reinforcement-learning-policy-evaluation/blob/main/HW1_MDP.jpg)



## Misc/Results
A run of Q1 was generated and the results were stored in Gs.txt. These were used to plot the graphs in "[Plotting Results.ipynb](/Plotting Results.ipynb)" Jupyter Notebook. 
Similarly for Q2d, "[Q2_stats.txt](/Q2_stats.txt)" were generated and used to plot the graphs. 

The following plot shows how J-estimate stabililized as number of runs $N$ is increased.
![image](https://github.com/ojasraundale/reinforcement-learning-policy-evaluation/blob/main/plots/2b_new.png)

"[runs.txt](/runs.txt)" contains a few hundred thousand runs of the 1st policy which one may look if interested.

