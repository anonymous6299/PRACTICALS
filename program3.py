import gymnasium as gym
import numpy as np
import random
import time

# Create FrozenLake environment
env = gym.make("FrozenLake-v1", is_slippery=False)

# Initialize Q-table
state_size = env.observation_space.n
action_size = env.action_space.n
Q = np.zeros((state_size, action_size))

# Set hyperparameters
learning_rate = 0.8
discount_factor = 0.95
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000
max_steps = 100

# Train the Q-learning agent
for episode in range(episodes):
    state, info = env.reset()
    done = False

    for step in range(max_steps):

        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        # Perform action
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Update Q-table
        Q[state, action] += learning_rate * (
            reward + discount_factor * np.max(Q[next_state, :]) * (not done)
            - Q[state, action]
        )

        state = next_state

        if done:
            break

    # Reduce exploration rate
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Training completed!")
print("\nTrained Q-Table:")
print(Q)

# Watch the trained agent play
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")

state, info = env.reset()
done = False

print("\nTrained Agent Playing the Game:")

while not done:
    action = np.argmax(Q[state, :])
    state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    time.sleep(0.5)

if reward == 1:
    print("Agent successfully reached the goal!")
else:
    print("Agent failed to reach the goal.")

env.close()