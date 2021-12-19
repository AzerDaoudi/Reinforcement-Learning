from abc import ABCMeta, abstractmethod

class ActionSelection:
    """
    Implements the action selection method for the agent  
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass 
    
    @abstractmethod
    def __repr__(self):
        pass
        

    @abstractmethod
    def select(self,agent_info):
        """
        A method to select an action from a given agent information
        """