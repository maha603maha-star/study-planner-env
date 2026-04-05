from env import MyStudyPlannerEnv
import random

def run():
    env = MyStudyPlannerEnv(level="medium")
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = random.choice(env.action_space)
        obs, reward, done, _ = env.step(action)
        total_reward += reward

    return f"Final Score: {total_reward}"

print(run())