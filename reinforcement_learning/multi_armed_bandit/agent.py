import numpy as np 
from basic_agent import BasicAgent

class Agent(BasicAgent):

    def __init__(self, num_actions, selection_strategy, alpha = None):

        self.num_actions = num_actions
        self.selection_strategy = selection_strategy
        self.step_size = alpha
        self.q_values = np.zeros(num_actions)
        self.action_count = np.zeros(num_actions)
        self.last_action = None
        self.time_step_t = 0
        self.started = False

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






        







    
