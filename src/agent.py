
import random
from env import Environment

class Agent:
    def __init__(self):
        """We initialize a counter that will keep the total reward during the episode"""
        self.total_rewards = 0.0

    def step(self, env: Environment):
        """
        The step function takes in Environmemt as an argument and performs the following:
        1. Observes the environment
        2. Makes a decision about the action to take based on the observations
        3. Submits the reward to the environment
        4. Gets the reward for the current step
        """
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_rewards += reward

    """For our Example, the agent ignores the observations in the decision making process on which
       action to take, Instead it chooses an action randomly
    """

    """
    Finally, we will create a glue code that will merge the two classes and the run
    """


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
        print("Total reward got: %.4f" % agent.total_rewards)




