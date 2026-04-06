from fastapi import FastAPI
from env import MyStudyPlannerEnv

app = FastAPI()

env = MyStudyPlannerEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: int):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }
