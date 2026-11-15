import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from collections import deque

# Create CartPole environment
env = gym.make("CartPole-v1")

# Define neural network
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_size, 24),
            nn.ReLU(),
            nn.Linear(24, 24),
            nn.ReLU(),
            nn.Linear(24, action_size)
        )

    def forward(self, x):
        return self.network(x)

# Initialize parameters
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

model = DQN(state_size, action_size)
target_model = DQN(state_size, action_size)
target_model.load_state_dict(model.state_dict())

optimizer = optim.Adam(model.parameters(), lr=0.001)
memory = deque(maxlen=10000)

gamma = 0.99
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
batch_size = 64
episodes = 300

# Select action using epsilon-greedy policy
def select_action(state):
    if random.random() < epsilon:
        return env.action_space.sample()

    state = torch.FloatTensor(state).unsqueeze(0)
    with torch.no_grad():
        return model(state).argmax().item()

# Train DQN using replay memory
def train_model():
    if len(memory) < batch_size:
        return

    batch = random.sample(memory, batch_size)

    states, actions, rewards, next_states, dones = zip(*batch)

    states = torch.FloatTensor(np.array(states))
    actions = torch.LongTensor(actions).unsqueeze(1)
    rewards = torch.FloatTensor(rewards)
    next_states = torch.FloatTensor(np.array(next_states))
    dones = torch.FloatTensor(dones)

    current_q = model(states).gather(1, actions).squeeze()

    with torch.no_grad():
        next_q = target_model(next_states).max(1)[0]
        target_q = rewards + gamma * next_q * (1 - dones)

    loss = nn.MSELoss()(current_q, target_q)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Training loop
for episode in range(episodes):
    state, info = env.reset()
    total_reward = 0

    for step in range(500):
        action = select_action(state)

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        memory.append((
            state, action, reward, next_state, done
        ))

        state = next_state
        total_reward += reward

        train_model()

        if done:
            break

    epsilon = max(epsilon_min, epsilon * epsilon_decay)

    # Update target network
    if episode % 10 == 0:
        target_model.load_state_dict(model.state_dict())

    print("Episode:", episode + 1, "Reward:", total_reward)

env.close()

# Test trained agent
test_env = gym.make("CartPole-v1", render_mode="human")

state, info = test_env.reset()
done = False

while not done:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)

    with torch.no_grad():
        action = model(state_tensor).argmax().item()

    state, reward, terminated, truncated, info = test_env.step(action)
    done = terminated or truncated

test_env.close()

print("DQN Training and Testing Completed!")