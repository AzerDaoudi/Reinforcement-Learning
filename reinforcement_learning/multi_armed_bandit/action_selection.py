import numpy as np 
from basic_action_selection import ActionSelection

class EpsilonGreedy(ActionSelection):

    def __init__(self, epsilon = 0.1):
        self.epsilon = epsilon
        
    def __repr__(self):
        return f"Epsilon greedy action selection with epsilon = {self.epsilon}"
    
    def __setattr__(self, key, value):

        if key == "epsilon":
            if not(value >= 0 and value <= 1 ):
                raise AttributeError(f"'Epsilon' must be in [0,1], epsilon = {value}")
           
    def select(self, agent_info):

        q_values = agent_info["q_values"]
        if np.random.random() <=  self.epsilon:
            return np.random.choice(agent_info["num_actions"])
        else: 
            return np.argmax(q_values)


class UCB(ActionSelection):

    def __init__(self, c = 2):

        self.c = c
    def __repr__(self):
        return f"Upper-Confidence-Bound action selection with c = {self.c}"

    def select(self, agent_info):

        q_values = agent_info["q_values"]
        action_count = agent_info["action_count"]
        time_steps = agent_info["time_step_t"]

        if 0 not in action_count:
            return np.argmax(q_values + self.c * np.sqrt(np.log(time_steps/action_count)))
        else:
            return np.random.choice(np.where(action_count == 0)[0])



class Stochastic(ActionSelection):
    pass



        

    




