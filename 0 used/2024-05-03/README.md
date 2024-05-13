# PPO Agent Worm

- Model on Hugging Face: https://huggingface.co/chirbard/ppo-Worm
- Based on Hugging Face Deep RL course: https://huggingface.co/learn/deep-rl-course/
- See it play on hugging face (choose chirbard/ppo-Worm): https://huggingface.co/spaces/unity/ML-Agents-Worm 

## Hyperparameters
```
behaviors:
  Worm:
    trainer_type: ppo
    hyperparameters:
      batch_size: 2024
      buffer_size: 20240
      learning_rate: 0.0003
      beta: 0.005
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 3
      learning_rate_schedule: linear
    network_settings:
      normalize: true
      hidden_units: 512
      num_layers: 3
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.9995
        strength: 1.0
    keep_checkpoints: 5
    max_steps: 5000000
    time_horizon: 1000
    summary_freq: 30000
```

## Video
![replay gif](replay.gif)