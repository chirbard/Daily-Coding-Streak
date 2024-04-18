# PPO Agent playing BipedalWalker-v3 

- Model on Hugging Face: https://huggingface.co/chirbard/ppo-BipedalWalker-v3
- Based on Hugging Face Deep RL course: https://huggingface.co/learn/deep-rl-course/
- Gymnasium Environment: https://gymnasium.farama.org/environments/box2d/bipedal_walker/

## Hyperparameters
```
model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 1024,
    batch_size = 64,
    n_epochs = 4,
    gamma = 0.99,
    gae_lambda = 0.98,
    ent_coef = 0.01,
    verbose=1)
```
## Train Time
Trained for 3 000 000 timesteps. Training took 1 hour and 8 minutes on Nvidia RTX A2000 Laptop.

## Video
![replay gif](replay.gif)