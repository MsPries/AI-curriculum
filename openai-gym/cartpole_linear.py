'''
A model-free solver for the CartPole environment in the OpenAI Gym.

The player chooses four random weights and chooses to move left or right
based on the product of multiplying those weights with the observation.
The player recieves a score for the episode and if the player has improved
since the last episode, it keeps the weights. Otherwise, the weights are
randomly modified by adding random changes that are scaled to become
increasingly larger the more episodes pass before an improvement occurs.

The increasing scalar serves to expedite learning if the weights start
in a very ineffective random configuration. To test without the scalar
increase, run the player with the linear_random=False kwarg.

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
		self.ORIGINAL_RANDOMNESS = 0.05 # Amount of noise
		self.RANDOMNESS_INCREASE = 0.001 # Amount to increase randomness scalar

		self.randomness = self.ORIGINAL_RANDOMNESS

		# Store videos of the episodes in the "cartpole-linear" directory - default is no video
		if monitor:
			self.env = gym.wrappers.Monitor(self.env, './cartpole-linear', force=True)
		print("init")

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

	def run(self, linear_random=True):
		best_score = 0
		# Start with four random weights
		params = np.random.rand(4) * 2 - 1

		# Start new episodes, modifying the weights based on the results
		for j in range(100000):
			# Modify the existing weights introducing scaled noise
			next_params = params + (np.random.rand(4) * 2 - 1)*self.randomness
			score = self.episode(next_params) # Run the episode with the new params

			if score > best_score: # If these params seem better than the last ones, keep
				best_score = score
				params = next_params
				self.randomness = self.ORIGINAL_RANDOMNESS # Reset randomness amount
				print("Episode {}: {}".format(j, best_score))
			# If the most recent episode wasn't an improvement and we are linearly scaling the amount of noise, do so
			elif linear_random:
				self.randomness += self.RANDOMNESS_INCREASE

			if score == self.MAX_SCORE: # We can't find a better score, so stop
				break
		print("Best score was from Episode {}: {}".format(j, best_score))

if __name__ == '__main__':
    player = CartPoleSolver()
    player.run()
