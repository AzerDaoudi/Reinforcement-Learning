from abc import ABCMeta, abstractmethod

class BasicEnvironment:
    """
    Implements the the Environment for the agent
    """

    __metaclass__ = ABCMeta
    @abstractmethod
    def start(self):
        """
        A method called to start the environment
        """

    @abstractmethod
    def action_reward(self, action):
        """
        Environment Method, that return the reward when an action taken by the agent
        """
    @abstractmethod
    def clean_env(self):
        """
        Method for reset the environment to initial values
        """
