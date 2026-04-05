import random
from env import MyStudyPlannerEnv

env = MyStudyPlannerEnv(level="medium")

for episode in range(5):
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = random.choice(env.action_space)
        obs, reward, done, _ = env.step(action)
        total_reward += reward

    print("Episode:", episode, "Score:", total_reward)