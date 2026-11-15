''' 
AIM= Python implementation of the iterative policy evaluation and update. 

REL. THEORY=
Iterative Policy Evaluation is a reinforcement learning technique used to calculate the value of states under a given policy. It repeatedly updates state values using the Bellman expectation equation until the values converge. Policy improvement selects better actions based on the calculated values. These steps form the foundation of policy iteration in reinforcement learning.



CODE=                                     '''

import numpy as np

# Define GridWorld environment
rows = 4
cols = 4
states = rows * cols
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Initialize value function
V = np.zeros(states)

# Set parameters
gamma = 0.9
theta = 0.001
reward = -1

# Define transition function
def get_next_state(state, action):
    row = state // cols
    col = state % cols

    if action == 'UP':
        row = max(0, row - 1)
    elif action == 'DOWN':
        row = min(rows - 1, row + 1)
    elif action == 'LEFT':
        col = max(0, col - 1)
    elif action == 'RIGHT':
        col = min(cols - 1, col + 1)

    return row * cols + col

# Initialize random policy
policy = np.random.randint(0, 4, states)

# Iterative Policy Evaluation
def policy_evaluation():
    global V

    while True:
        delta = 0

        for state in range(states):
            if state == 0 or state == states - 1:
                continue

            old_value = V[state]
            action = actions[policy[state]]
            next_state = get_next_state(state, action)

            V[state] = reward + gamma * V[next_state]
            delta = max(delta, abs(old_value - V[state]))

        if delta < theta:
            break

# Policy Improvement
def policy_improvement():
    policy_stable = True

    for state in range(states):
        if state == 0 or state == states - 1:
            continue

        old_action = policy[state]
        values = []

        for action in actions:
            next_state = get_next_state(state, action)
            values.append(reward + gamma * V[next_state])

        policy[state] = np.argmax(values)

        if old_action != policy[state]:
            policy_stable = False

    return policy_stable

# Policy Iteration
iteration = 0

while True:
    iteration += 1

    policy_evaluation()

    if policy_improvement():
        break

# Display results
print("Policy Iteration Completed")
print("\nOptimal Value Function:")
print(V.reshape(rows, cols))

print("\nOptimal Policy:")

symbols = ['↑', '↓', '←', '→']

for state in range(states):
    if state == 0:
        print('S', end='  ')
    elif state == states - 1:
        print('G', end='  ')
    else:
        print(symbols[policy[state]], end='  ')

    if (state + 1) % cols == 0:
        print()

print("\nTotal Iterations:", iteration)

'''
LO=
1. Understood policy evaluation and improvement.
2. Calculated state values iteratively.
3. Implemented policy iteration for GridWorld.
'''