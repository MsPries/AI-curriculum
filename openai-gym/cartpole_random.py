'''
A model-free solver for the CartPole environment in the OpenAI Gym.

Every episode, the player chooses chooses four random weights and chooses
to move left or right based on the product of multiplying those weights
with the observation. The player receives a score for the episode and keeps
track of the weights from the episode which received the highest score.

This example serves as a scaffolding for approaching a gym environment.

Written by Emily Pries based on Kevin Frans' post at http://kvfrans.com/simple-algoritms-for-solving-cartpole/
'''

import gym
import numpy as np

class CartPoleSolver():
	# Solver initialization
	def __init__(self, monitor=False):
		# Make the gym environment
		self.env = gym.make('CartPole-v1')

		# Set environment variables
		self.MAX_SCORE = 500 # The best score possible for this environment is 500

		# Store videos of the episodes in the "cartpole-random" directory - default is no video
		if monitor:
			self.env = gym.wrappers.Monitor(self.env, './cartpole-random', force=True)

	def choose_action(self, observation, params):
		# Cart pole lets us move left (action = 0) or right (action = 1)
		# This moves left if observation x params < 0, otherwise move right
		return 0 if np.matmul(observation, params) < 0 else 1

	def episode(self, params):
		# Reset the environment
		observation = self.env.reset()
		score = 0

		# Repeatedly choose an action, apply the action, and update the score
		for i in range(5000):
			action = self.choose_action(observation, params)
			observation, reward, done, info = self.env.step(action)
			score += reward
			if done: # The episode has ended
				break
		return score

	def run(self, linear_random=False):
		best_score = 0
		best_params = None

		# Start new episodes to find the best set of params
		for j in range(100000):
			# Randomly assign four weights and run an episode
			params = np.random.rand(4) * 2 - 1
			score = self.episode(params)

			# Keep track of the best scoring params
			if score > best_score:
				best_score = score
				best_params = params
				print("Episode {}: {}".format(j, best_score))

			if score == self.MAX_SCORE: # We can't find a better score, so stop
				break
		print("Best score was from Episode {}: {}".format(j, best_score))

if __name__ == '__main__':
    player = CartPoleSolver()
    player.run()
