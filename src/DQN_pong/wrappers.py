import cv2
import gym
import gym.spaces
import numpy as np
import collections

class Firereset(gym.wrappers):
    def __init__(self,env=None):
        super(Firereset, self).__init__(env)
        assert env.unwrapped.get_action_meanings()[1] == 'FIRE'
        assert len(env.unwrapped.get_action_meanings()) >= 3

    def step(self,Action):
        return self.env.step(Action)

    def reset(self):
        self.env.reset()
        obs, _, done, _ = self.env.step(1)
        if done:
            self.env.reset()
        obs, _, done, _ = self.env.step(2)
        if done:
            self.env.reset()
        return obs

class MaxAndSkipEnv(gym.wrappers):
    def __init__(self, env=None, skip=4):
        super(MaxAndSkipEnv, env, self).__init__(env)
        self.obs_buffer =collections.deque(maxlen=2)
        self._skip = skip

    def step(self, Action):
        total_rewards=0.0
        done = None
        for _ in range(self._skip):
            obs,reward, done, info = self.env.step(Action)
            self.obs_buffer.append(obs)
            total_rewards += reward
            if done:
                break
            max_frame = np.max(np.stack(self._obs_buffer), axis=0)
            return max_frame, total_rewards, done, info


class Bufferwrapper(gym.ObservationWrapper):
    def __init__(self, env, n_steps=4, dtype=np.float64):
        super(Bufferwrapper, self).__init__(env)
        self.dytpe = dtype
        old_space= env.observation_space

        self.observation_space = gym.spaces.Box(
            old_space.low.repeat(n_steps, axis=0),
            old_space.high.repeat(n_steps, axis=0), dtype=dtype)
