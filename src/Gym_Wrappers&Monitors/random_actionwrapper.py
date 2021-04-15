import gym
from typing import TypeVar
import random


Action = TypeVar("Action")

class RandomActionWrapper(gym.ActionWrapper):
    """We initialize the wrapper by calling a parent's __init__ method and also define epsilon; the probability to choose a random value"""
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon
    def Action(self, action:Action) -> Action:
        """
        This is the method that we need to override from the parent's class to tweak the actions.
        We sample a random action with the probability of epsilon instead of the action that we receive from the agent
        """
        if random.random() < self.epsilon:
            print("Random!!")
            return self.env.action_space.sample()
        return Action
    """
    Now, we will create a normal CartPole and pass it to our wrapper constructor.
    Now we will use the wrapper as our normal Env instance instead of the CartPole
    If you want, you can play with the epsilon parameter on the wrapper's creation
    and verify that randomness improves the agent's score on average.
    """
if __name__=="__main__":
    env = RandomActionWrapper(gym.make("CartPole-v0"))

    obs = env.reset()
    total_rewards=0.0
    while True:
        obs, reward, done, _ =env.step(0)
        total_rewards += reward
        if done:
            break
    print("Reward got: %.2f" % total_rewards)

"""
MONITOR

Another class that you should be aware of is Monitor . It is implemented like
Wrapper and can write information about your agent's performance in a file, with
an optional video recording of your agent in action.
"""


