# AI-curriculum

### Introduction
This repo contains the curriculum as it was taught for Applied Math and Artificial Intelligence '17-'18. You can see example projects in the class gallery [here](https://mspries.github.io/).

This class was offered as a project based class for high school seniors with and without a background in calculus. I have structured the materials here as a resource for other educators, however it may be of interest to students of all stripes. Normally, the class met twice per week for 45 minutes and offered 45 minutes of homework per class meeting. I ordered the projects based on how I taught them, however, you will notice it is an imperfect progression. I have included some facilitation notes knowing YMMV.

Use this README as an overview for the various projects offered. Where appropriate, further resources are available in the sub-directories of this repo. 

### Table of Contents
- [Getting Started with Python](#getting-started-with-python)
- [Q-Learning for Pathfinding](#q-learning-for-pathfinding)
- [Introduction to Neural Networks](#introduction-to-neural-networks)
- [Text Classification](#text-classification)
- Handwriting Recognition (MNIST)
- [OpenAI Gym Video Game Agents](#openai-gym-video-game-agents)
- Style Transfer
- Final Projects
- [Appendix A - Escape the Room](#appendix-a---escape-the-room)
- [Appendix B - Neural Network Email](#appendix-b---neural-network-email)
- Appendix C: Brainstorm Materials
- [Appendix D - GitHub Set Up Instructions](#appendix-d---github-set-up-instructions)

### Getting Started with Python
The students had not learned Python in a prior class, however some were familiar with it on their own. Most students had taken two years (2x/week) of classes taught in Java. I wanted them to get comfortable learning on their own, so in class I did the following:
- Most of environment set up (Python 3.5.x and Sublime Text)
- Demo of how to save and run a Python file (and talked about the difference between Python as an interpreted language and Java as a compiled language)
- Overview of command line

Then, their homework for the next two nights (an hour and a half) was to work their way through this list:
1. **Contribute to [this class-wide doc](https://docs.google.com/document/d/1NM1VvV0Txrq8BfaZutzzKT3rGzSic5fY6BXO2HSQJho/edit?usp=sharing)** to get their feet wet in beginning thinking through how the concepts behind programming languages are similar, even if the syntax looks different.
2. **Read and annotate [World.py](https://github.com/emilypries/q_learning_demo/blob/master/World.py) and [Learner.py](https://github.com/emilypries/q_learning_demo/blob/master/Learner.py)**, researching and taking notes on syntax they were unfamiliar with. These were the files we were using first, so I wanted them to feel comfortable reading unfamiliar code as well as get comfortable prioritizing the most pressing things they don't know. Seeing how much you don't know and proceeding anyway is one of the biggest skills I wanted to develop in these students.
3. **Practice writing Python snippets** using a site like [Coding Bat](http://www.codingbat.com) (which focuses on syntax) or [Project Euler](http://www.projecteuler.net) (which focuses on problem solving).
4. **Translate an existing Java program into Python.** It is important students who are new to Python choose a project without major dependencies. Students who felt more comfortable in Python started looking into Python libraries.
5. **Modify [World.py](https://github.com/emilypries/q_learning_demo/blob/master/World.py) and [Learner.py](https://github.com/emilypries/q_learning_demo/blob/master/Learner.py) as you choose.** Suggestions (in loose increasing order of Python familiarity): change the color of the target and death pit, change the score penalty per step, make the program run more slowly, increase the size of the board, increase the number of squares on the board, add a new obstacle, change the starting point/target/death pit, modify the program to find the optimal path in fewer runs...
6. **Practice using the command line** to navigate between directories.

You will notice that doing all of these would take more than an hour and a half - this is intentional. All of these are valuable practice, so students choose the portions most interesting to them and bring the lessons into class to share with other students.

After the text classification project, several students shared that they would have liked to spend more time on this part. I wanted to get them hooked on doing something cool to "trick" them into learning on their own, but they were already motivated enough that we could have dedicated more time to this together. In particular, the students would have been able to move more quickly with more comfort on the command line. Next time, I might make a Capture the Flag type game where students need to navigate between directories to get clues and find a result in class.

### Q-Learning for Pathfinding
Q-Learning is a reinforcement learning technique. For this project, we used [this program](https://github.com/emilypries/q_learning_demo) from Siraj Raval [video on Q-Learning in video games](https://www.youtube.com/watch?v=A5eihauRQvo). The students got more comfortable with Python by reading, annotating, then modifying these programs. For facilitator reference, in one 45 minute class, we did a close reading of Learner.py together through line 25. For homework, they continued the close reading and then in the next class we teased out [how Q-Learning works](https://en.wikipedia.org/wiki/Q-learning). 

### Introduction to Neural Networks
I used [MarI/O](https://www.youtube.com/watch?v=qv6UVOQ0F44) as a hook for approaching neural networks, as it offers great visuals along with a concise explanation of what makes this technique interesting. For homework, the students read through [Trask's tutorial](https://iamtrask.github.io/2015/07/12/basic-python-network/) to start thinking about creating their own basic neural networks. In class together, we drew out a basic neural network and talked through calculating the dot product. Then, the students worked on making their own network for determining XOR based on the tutorial. In class, we resolved Python issues, as this was their first time writing Python, as well as talked about the sigmoid function. [This is one resource](http://www.bogotobogo.com/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php) that gave students some clarity around the sigmoid function. 

For building their XOR networks, I gave them code for a working example as well as structure for writing their own - you can find this code [here](https://github.com/emilypries/xor-neural-network). This gave them the confidence to dive into the blank part of code and gave them an easy resource for debugging on their own. This seemed to be the right amount of support to allow them to focus on the concepts while developing their Python skills.

Additionally, this tutorial used numpy, so the students installed pip and started getting comfortable installing packages on their own computers. [Here](https://github.com/MsPries/AI-curriculum/blob/master/appedix/pip.md) are the instructions I gave them.

### Text Classification
Text classification was the theme of the students' first major group project. They were challenged to try to answer a central question using some set of text. The project rubric is available [here](https://docs.google.com/document/d/1YauZ3bCHO7yNwlQh0lxH_-nULNi3PowZ9s_KPQM0Pdc/edit?usp=sharing).

We started by looking at the bag of words technique together. The students worked through [this tutorial](https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6) over two homeworks and two class periods. Then, they moved into [this Kaggle competition](https://www.kaggle.com/c/word2vec-nlp-tutorial#part-1-for-beginners-bag-of-words) looking at IMDB reviews and the associated ratings. This Kaggle competition was great as a resource because it built directly off of the tiny bag of words tutorial and laid out some challenges associated with using this technique for this application. There are numerous tutorials directly connected to the IMDB Kaggle competition and ones that plugged directly into iPython notebooks were most helpful.

As it was the first group project, we spent some time looking at collaboration tools. I gave them a guide for using GitHub and an [overview](https://docs.google.com/document/d/1NnFg3SMnAP2Cw_WqTTWZfBs053kCc_4-lNQMYbGAy80/edit?usp=sharing) of some existing systems. At the start of each class, we had a stand up meeting where each group gave a concise update on their progress and had the opportunity to formally ask for help. The students stayed somewhat involved with other students' projects, so the formal ask for help option was less needed. I gave them [instructions](#appendix-d---github-set-up-instructions) for setting up GitHub but spent the next class going over how it works; next time I will just explain how it works for the sake of time.


### OpenAI Gym Video Game Agents
For the student's semester exam project, they were challenged to explore AI programs to complete challenges or compete in the [OpenAI Gym](https://gym.openai.com/). You can find the student prompt [here](https://github.com/MsPries/AI-curriculum/blob/master/openai-gym/prompt.md).

To introduce the project, we explore a solver for the ["cartpole" environment](https://gym.openai.com/envs/CartPole-v0/). This introduced the idea of interacting with a simulated environment and gave them scaffolding code to build off of. I gave them a [random player](https://github.com/MsPries/AI-curriculum/blob/master/openai-gym/cartpole_random.py) that tries random parameters and keeps track of the most successful set as well a [random player that scales linearly](https://github.com/MsPries/AI-curriculum/blob/master/openai-gym/cartpole_linear.py). In class, we looked at graphs and had students visualize the success score vs parameter choices in 2, 3, and 4 dimensions. This was a helpful way to see the role of gradient descent interacting with a cost function. From there, they delved into their projects for the next ~3 weeks.

### Appendix A - Escape the Room
This "escape the room" style activity checked for understanding for concepts of the first few explorations. The overhead to create it was more than standard but it is easily modified to be reusable and the excitement around collaborative problem-solving was incredible.

You can find the live version of the activity [here](https://mspries.github.io/escape/escape.html) and a complete write up [here](https://github.com/MsPries/AI-curriculum/blob/master/appendix/escape_the_room.md).

### Appendix B - Neural Network Email
I used an example email with a proposed design for a college acceptance text classifier using neural networks to check for understanding on neural network fundamentals. We also discussed the ethics behind building such a program. It worked well as a classroom discussion, however if I were concerned about getting a more granular understanding of individual student mastery, I would have assigned annotating this email as a homework assignment.

You can find the example email [here](https://github.com/MsPries/AI-curriculum/blob/master/appendix/text_classifier_email.md).


### Appendix D - GitHub Set Up Instructions
I gave the students [these instructions](https://docs.google.com/document/d/1gzKgVDmiwaBqljEHdeqNw-NFH-A_cEJwEU-7L-fDJ_A/edit?usp=sharing) to help them get set up on GitHub
