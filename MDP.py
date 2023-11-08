import numpy as np
import random

POLICY1 = 1         # Policy 1 is for Q2 a, b, c
POLICY2 = 2         # Policy 2 is the random deterministic policy for Q2 d.


class MDP:
    """
    Class for the Markov Decision Process.
    The MDP configurations are provided through input_mdp and input_policy text files.
    """
    
    def __init__(self, input_mdp, input_policy) -> None:
        # Reading MDP inputs
        with open(input_mdp) as fp:
            lines = fp.readlines()
            self.states = lines[0].split()          # States are in 0th line
            # States contain ['s1', 's2', ... ,'s7']
            self.actions = lines[1].split()         # Actions are in 1st line
            # Actions contain ['a1', 'a2']
            self.end_states = lines[2].split()      # End States are in 2nd line
            # End state contains the final states. ['s6', 's7'] in this example

            # Initializing initial Ps, Transition Ps, and Policy to zero
            self.initial_p = np.zeros(len(self.states))
            self.transition_matrix = np.zeros((len(self.states), len(self.actions), len(self.states)))
            self.rewards = np.zeros((len(self.states), len(self.actions))) 
            self.policy = np.zeros((len(self.states), len(self.actions)))

            # Initializing Random Policy
            self.random_policy = np.zeros((len(self.states), len(self.actions)))
            self.RandomizeTheRandomPolicy()     # Randomizes the policy

            for line in lines:
                parts = line.strip().split()

                # Initial probabilitis
                if len(parts) == 5 and 'd0' in parts[0]:
                    s = self.states.index(parts[1])
                    p = parts[4]
                    self.initial_p[s] = p
                
                # Transition Matrix
                if len(parts) == 9 and 'p' in parts[0]:
                    s1 = self.states.index(parts[1])
                    a = self.actions.index(parts[3])
                    s2 = self.states.index(parts[5])
                    p = parts[8]
                    self.transition_matrix[s1][a][s2] = p
                
                # Rewards
                if len(parts) == 7 and 'R' in parts[0]:
                    s = self.states.index(parts[1])
                    a = self.actions.index(parts[3])
                    r = float(parts[6])
                    self.rewards[s][a] = r

        # Checking if sum of Ps of all actions is 1 in transition matrix
        self.ValidateMDP()  

           
        # Reading Policy
        with open(input_policy) as fp:
            lines = fp.readlines()
            for line in lines:
                parts = line.strip().split()
                s = self.states.index(parts[0])
                a = self.actions.index(parts[1])
                p = parts[2]
                self.policy[s][a] = p
        return
    

    def ValidateMDP(self):
        p_sum = [
            sum(self.transition_matrix[self.states.index(s)][self.actions.index(a)] )==1
            for s in self.states for a in self.actions if s not in self.end_states
            ]
        if not all(p_sum):
            raise "Wrong Transition Matrix in MDP with non 1 outgoing probabilities"       
        return


    def GenerateStartState(self):
        return random.choices(self.states, self.initial_p)[0]
    

    def GenerateAction(self, s, policy_option = POLICY1):
        s_index = self.states.index(s)

        # Select policy option
        if policy_option == POLICY1:
            return random.choices(self.actions, self.policy[s_index])[0]
        elif policy_option == POLICY2:              
            return random.choices(self.actions, self.random_policy[s_index])[0]
    

    def GenerateNextState(self, s, a):
        s_index = self.states.index(s)
        a_index = self.actions.index(a)
        return random.choices(self.states, self.transition_matrix[s_index][a_index])[0]


    def GenerateReward(self, s, a):
        s_index = self.states.index(s)
        a_index = self.actions.index(a)
        return self.rewards[s_index][a_index]


    def RandomizeTheRandomPolicy(self):
        self.random_policy = np.zeros((len(self.states), len(self.actions))) # Reset the random policy
        for s in self.states: # Iterate through all the states
            # Choose the random action out of all the actions
            a_chosen = random.choices(self.actions)[0]
            s_index = self.states.index(s)
            a_chosen_index = self.actions.index(a_chosen)
            self.random_policy[s_index][a_chosen_index] = 1.
    

def main():
    mdp = MDP('MDP.txt', "policy.txt")
    # print(mdp.GenerateStartState())
    # print(mdp.states)
    # print(mdp.actions)
    # print(mdp.transition_matrix)
    # print(mdp.initial_p)
    # print(mdp.policy)
    print(mdp.policy[1])
    print(mdp.transition_matrix[1][1])
    a = mdp.GenerateAction("s2")
    print(a)
    s = mdp.GenerateNextState("s2", a)
    print(s)
    r = mdp.GenerateReward("s2", a)
    print(r)


if __name__ == "__main__":
    main()