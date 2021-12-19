from abc import ABCMeta, abstractmethod

class BasicAgent:

    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        pass 
    @abstractmethod
    def start(self):
        """
        A method called to start agent
        """
    @abstractmethod
    def update(self, reward_signal):
        """
        A method to update the action values from the  environment's reward
        """
    @abstractmethod
    def agent_info(self):
        """
        A method returns a dictionary that contains the agent information/state
        """
