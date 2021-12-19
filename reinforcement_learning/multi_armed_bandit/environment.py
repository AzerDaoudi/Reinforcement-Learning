from basic_environment import BasicEnvironment
import numpy as np 

class ArmedTestbed(BasicEnvironment):

    def __init__(self, num_arms = 10, seed = 1442):

        self.num_arms = num_arms
        self.mean_action_values = None
        self.started = False
        self.seed = seed
        self.optimal_value = None

    def start(self):

        if not self.started:
            np.random.seed(self.seed)
            self.started = True
            self.mean_action_values = 2*np.random.randn(self.num_arms)
            self.optimal_value = np.max(self.mean_action_values)

        else:
            raise Exception(f"The {self.num_arms}-armed Test bed has already started")
        
    
    def action_reward(self, action):

        return self.mean_action_values[action] + np.random.randn()

    
    def clean_env(self):
        self.started = False
        self.mean_action_values = None
        self.optimal_value = None



    

    


