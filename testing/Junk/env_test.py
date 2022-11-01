import gym

env = gym.make("CartPole-v1", render_mode="rgb_array")

observation = env.reset()

print(observation)
print(env.action_space)

done = False
while not done:
    observation, reward, done, info, temp = env.step(env.action_space.sample())
    print(env.action_space.sample())

    env.render()
