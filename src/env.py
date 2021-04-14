import random

import gym



class Environment:
    """Initializing the internal state of the environment"""
    def __init__(self):
        self.steps_left=10
    """Below function returns the observation state of the environment to the Agent"""
    def get_observation(self) -> List [float]:
        return[0.0,0.0,0.0]
    """Below function is a query of the Agent to the environment on the possible set of actions
    In this case, the possible actions are 0 and 1
    """
    def get_actions(self) ->List [int]:
        return[0,1]
    """The below code is to signal the  end of an episode.
    A series of interactions between the Agent and the environment are divided into sequences called Episodes
    """
    def is_done(self) ->bool:
        return self.steps_left ==0
    """ Action class(below), is the central piece of the environment's functionality, and it does two things-
    One, It handles the actions from the Agent.
    Two, It returns the rewards from the Environment.
    In This example, the reward is a random number and the actions are[0,1]
    """
    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()

