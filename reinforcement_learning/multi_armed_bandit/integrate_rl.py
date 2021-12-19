import numpy as np 
import matplotlib.pyplot as plt 
class IntegrateRL:
    """
    class represents the integration of a list of agents with their environment.
    """
    def __init__(self, agents, environment, num_runs = 100, num_steps = 1000):

        self.agents = agents
        self.env = environment
        self.num_runs = num_runs
        self.num_steps = num_steps
        self.rewards = np.zeros((len(agents),num_steps))

    def interact(self):

        self.env.start()
        for i, agent in enumerate(self.agents):
            for run in range(self.num_runs):
                action = agent.start()
                for step in range(self.num_steps):
                    reward = self.env.action_reward(action)
                    action =  agent.update(reward)
                    self.rewards[i][step] += reward
            
                agent.clean_agent()
            self.rewards[i] = self.rewards[i]/self.num_runs

        self.env.clean_env()

    def plot_rewards(self):
        pass


            
                    
        
