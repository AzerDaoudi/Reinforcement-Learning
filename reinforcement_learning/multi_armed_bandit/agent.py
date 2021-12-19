import numpy as np 
from basic_agent import BasicAgent

class Agent(BasicAgent):

    def __init__(self, num_actions, selection_strategy, initial_value = 0, alpha = None):

        self.num_actions = num_actions
        self.selection_strategy = selection_strategy
        self.step_size = alpha
        self.q_values = initial_value * np.ones(num_actions)
        self.action_count = np.zeros(num_actions)
        self.last_action = None
        self.time_step_t = 0
        self.started = False
        self.initial_value = initial_value
    
    def __setattr__(self, key, value):

        if key == "step_size" and value is not None:
            if not(value > 0 and value <= 1 ):
                raise AttributeError(f"The step size 'alpha' must be in (0,1], alpha = {value}")
            

        

    def start(self):

        if not self.started:

            self.started = True
            self.last_action = self.selection_strategy.select(self.agent_info())
            self.time_step_t += 1
            self.action_count[self.last_action] += 1

            return self.last_action
        else:
            raise Exception("The Agent has already started")

    def update(self, reward_signal):

        if self.step_size is None:
            self.q_values[self.last_action] += (reward_signal - self.q_values[self.last_action])/self.action_count[self.last_action]
        else:
            self.q_values[self.last_action] += self.step_size * (reward_signal - self.q_values[self.last_action])

        self.last_action = self.selection_strategy.select(self.agent_info())

        self.time_step_t += 1
        self.action_count[self.last_action] += 1
        
        return self.last_action


    def agent_info(self):
        return vars(self)

    def clean_agent(self):

        self.q_values = self.initial_value * np.ones(self.num_actions)
        self.action_count = np.zeros(self.num_actions)
        self.last_action = None
        self.time_step_t = 0
        self.started = False






        







    
