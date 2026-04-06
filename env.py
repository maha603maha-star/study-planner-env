import random

class MyStudyPlannerEnv:
    def __init__(self):
        self.action_space = [0, 1, 2, 3]
        self.reset()

    def reset(self):
        self.tasks = [3, 2, 2, 1]
        self.time_left = 10
        self.done = False
        return self._get_obs()

    def _get_obs(self):
        return [self.time_left] + self.tasks

    def step(self, action):
        if self.done:
            return self._get_obs(), 0, True, {}

        reward = 0

        if action < len(self.tasks):
            if self.tasks[action] > 0:
                self.tasks[action] -= 1
                reward += 5
            else:
                reward -= 2

        self.time_left -= 1
        reward -= 1

        if sum(self.tasks) == 0:
            reward += 20
            self.done = True

        if self.time_left <= 0:
            self.done = True

        return self._get_obs(), reward, self.done, {}
