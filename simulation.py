import sys
import json
import MDP
from MDP import MDP

POLICY1 = 1         # Policy 1 is for Q2 a, b, c
POLICY2 = 2         # Policy 2 is the random deterministic policy for Q2 d.


def runEpisode(mdp:MDP, gamma:float, chosen_policy) -> float:
    s = mdp.GenerateStartState()                                    # Generate the intial states based on d0
    G = 0.
    discount = 1.
    # run = s + " "        # Uncomment to print the episode
    while(s not in mdp.end_states):                                 # Exits when end states are reached
        a = mdp.GenerateAction(s=s, policy_option=chosen_policy)    # Generates action for selected policy
        s_next = mdp.GenerateNextState(s=s, a=a)                    # Generates next state based on transition matrix
        r = mdp.GenerateReward(s=s, a=a)                            # Generates reward based on reward function
        # run = run + a + " " + str(r) + " " + s_next + " "
        G += discount*r                                             # Adding discounted reward to Run's reward G
        discount = discount*gamma                                   # Readying discount for next step
        s = s_next                                                  # Readying s for next step
    # print(run)
    return G                                                        # Total discounted reward for the run is returned


def simulation_1(gamma = 0.9):
    # If policy 1 was chosen:

    mdp = MDP('MDP.txt', "policy.txt")
    n_runs = 150000
    Gs = []

    for i_episode in range(n_runs):
        print(f"Run number: {i_episode}") if i_episode % 10000 == 0 else None
        r = runEpisode(mdp, gamma, POLICY1)
        Gs.append(r)

    # Uncomment if you want to see all run's rewards.
    # with open(file="Gs.txt", mode="w") as f:
    #     for g in Gs: 
    #         f.write(str(g)+'\n')
    print(sum(Gs)/len(Gs))
    return
    

def simulation_2(gamma = 0.9):
    # If policy 2 was chosen:
    mdp = MDP('MDP.txt', "policy.txt")
    n_runs = 100                                # Number of runs per random policy
    # N = 250                                   # Number of random policies

    # f = open(file="Q2_stats.txt", mode="w")
    for N in range(1, 251, 10):
        # Setting best performance smaller than the Least reward possible in this MDP
        best_perf = -99999 
        best_policy = None
        for i_random_policy in range(N):
            mdp.RandomizeTheRandomPolicy()      # Randomized the current random policy
            # print(f"Running {i_random_policy}th random policy")
            # Running the episodes for this random policy
            sum_Gs = 0
            for i_episode in range(n_runs):
                r = runEpisode(mdp, gamma, POLICY2)
                sum_Gs = sum_Gs + r
            J = sum_Gs/n_runs                   # Averaging all the Gs over the n_runs of current policy
            if J > best_perf:                   
                best_perf = J                   # Updating best_perf if r is better than current best policy
                best_policy = mdp.random_policy
        # print(best_policy)
        print(N, best_perf)
        # f.write(str(N) + " " + str(best_perf) + "\n")
    print("Best Policy: ")
    print(best_policy)
    print(f"Best J: {best_perf}")
    # f.close()


    # print(best_policy)


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("No arguments passed, Run $python simulation.py <policy_num> <gamma>")
        print("<policy_num> : '1' = Given Policy, '2' = Random Deterministic Policy")
        print("<gamma> : Discount rate, real num between 0 and 1")
        print("Running the policy 1 with gamma = 0.9")
        simulation_1()
    elif(len(sys.argv) == 2):
        print("No <gamma> argument, running with gamma = 0.9")
        if(sys.argv[1] == '1'):
            simulation_1()
        elif(sys.argv[1] == '2'):
            simulation_2()
        else:
            print("Wrong usage. Enter <policy_num> either 1 or 2")
    elif(len(sys.argv) == 3):
        if float(sys.argv[2]) > 1 or float(sys.argv[2]) < 0:
            print("arg 2:<gamma> must be between 0 and 1")
        else:
            if(sys.argv[1] == '1'):
                simulation_1(float(sys.argv[2]))
            elif(sys.argv[1] == '2'):
                simulation_2(float(sys.argv[2]))
            else:
                print("Wrong usage. Enter <policy_num> either 1 or 2")
    else:
        print("Wrong usage! \nRun $python simulation.py 1 for given policy, 2 for random deterministic policy")

