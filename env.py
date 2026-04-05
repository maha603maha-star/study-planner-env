import random

class MyStudyPlannerEnv:
    def __init__(self, level="easy"):
        self.level = level
        self.reset()

    def reset(self):
        if self.level == "easy":
            self.subjects = {"Math": 2, "OS": 1}
        elif self.level == "medium":
            self.subjects = {"Math": 3, "OS": 2, "DBMS": 2, "AI": 1}
        else:
            self.subjects = {"Math": 4, "OS": 3, "DBMS": 3, "AI": 2, "CN": 2}

        self.priority = {sub: random.randint(1, 3) for sub in self.subjects}
        self.action_space = list(self.subjects.keys())
        self.time_left = 10
        self.done = False

        return self._get_obs()

    def _get_obs(self):
        return {
            "subjects": self.subjects.copy(),
            "priority": self.priority,
            "time_left": self.time_left
        }

    def step(self, action):
        if self.done:
            return self._get_obs(), 0, True, {}

        reward = 0

        if action in self.subjects:
            if self.subjects[action] > 0:
                self.subjects[action] -= 1
                reward += 5 + self.priority[action]
            else:
                reward -= 2

        self.time_left -= 1
        reward -= 1

        if all(v == 0 for v in self.subjects.values()):
            reward += 20 + self.time_left
            self.done = True

        if self.time_left <= 0:
            self.done = True

        return self._get_obs(), reward, self.done, {}