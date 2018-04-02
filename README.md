# AI-curriculum

#### Introduction
This repo contains the curriculum as it was taught for Applied Math and Artificial Intelligence '17-'18. This class was offered as a project based class for high school seniors with and without a background in calculus. I have structured the materials here as a resource for other educators, however it may be of interest to students of all stripes. Normally, the class met twice per week for 45 minutes and offered 45 minutes of homework per class meeting. I ordered the projects based on how I taught them, however, you will notice it is an imperfect progression. I have included some facilitation notes knowing YMMV.

Use this README as an overview for the various projects offered. Where appropriate, further resources are available in the sub-directories of this repo. 

#### Table of Contents
- [Getting Started with Python](#getting-started-with-python)
- Q-Learning for Pathfinding
- Introduction to Neural Networks
- Text Classification
- Handwriting Recognition (MNIST)
- OpenAI Gym Video Game Agents
- Style Transfer
- Final Projects
- Appendix A: Check for Understanding: Escape the Room
- Appendix B: Check for Understanding: Neural Network Fundamentals
- Appendix C: Brainstorm Materials

#### Getting Started with Python
The students had not learned Python in a prior class, however some were familiar with it on their own. Most students had taken two years (2x/week) of classes taught in Java. I wanted them to get comfortable learning on their own, so in class I did the following:
- Most of environment set up (Python 3.5.x and Sublime Text)
- Demo of how to save and run a Python file (and talked about the difference between Python as an interpreted language and Java as a compiled language)
- Overview of command line

Then, their homework for the next two nights (an hour and a half) was to work their way through this list:
1. **Contribute to [this class-wide doc](https://docs.google.com/document/d/1NM1VvV0Txrq8BfaZutzzKT3rGzSic5fY6BXO2HSQJho/edit?usp=sharing)** to get their feet wet in beginning thinking through how the concepts behind programming languages are similar, even if the syntax looks different.
2. **Read and annotate World.py and Learner.py**, researching and taking notes on syntax they were unfamiliar with. These were the files we were using first, so I wanted them to feel comfortable reading unfamiliar code as well as get comfortable prioritizing the most pressing things they don't know. Seeing how much you don't know and proceeding anyway is one of the biggest skills I wanted to develop in these students.
3. **Practice writing Python snippets** using a site like [Coding Bat](http://www.codingbat.com) (which focuses on syntax) or [Project Euler](http://www.projecteuler.net) (which focuses on problem solving).
4. **Translate an existing Java program into Python.** It is important students who are new to Python choose a project without major dependencies. Students who felt more comfortable in Python started looking into Python libraries.
5. **Modify Learner.py and World.py as you choose.** Suggestions (in loose increasing order of Python familiarity): change the color of the target and death pit, change the score penalty per step, make the program run more slowly, increase the size of the board, increase the number of squares on the board, add a new obstacle, change the starting point/target/death pit, modify the program to find the optimal path in fewer runs...
6. **Practice using the command line** to navigate between directories.

You will notice that doing all of these would take more than an hour and a half - this is intentional. All of these are valuable practice, so students choose the portions most interesting to them and bring the lessons into class to share with other students.

After the text classification project, several students shared that they would have liked to spend more time on this part. I wanted to get them hooked on doing something cool to "trick" them into learning on their own, but they were already motivated enough that we could have dedicated more time to this together. In particular, the students would have been able to move more quickly with more comfort on the command line. Next time, I might make a Capture the Flag type game where students need to navigate between directories to get clues and find a result in class.
