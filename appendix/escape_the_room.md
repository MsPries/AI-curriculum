### Escape the Room

This Wizard of Oz-themed check for understanding is a collaborative activity that challenged each class to "escape the room" by solving a timed series of puzzles based on the prior material.

It was shared as a webpage, available [here](https://mspries.github.io/escape/escape.html). The source code is available via GitHub [here](https://github.com/MsPries/mspries.github.io/tree/master/escape). Thanks to [@jhil](https://github.com/jhil) for donating his time to help with the design!

The flow for this activity is as follows:
1. Solving each of first three puzzles gave the students a number as a clue
2. For each student that defended an answer to the fourth puzzle, they received a letter or letters that, when ordered correctly, spelled out a location in my office where I hid a box locked with a combination lock
3. The combination lock's code was the three numbers from the first three puzzles
4. Inside the box, the students found a series of questions with answers falling in columns A or B, as well as a [Microbit](http://microbit.org/) microcontroller (I use these with my 7th grade classes). The students needed to find the right answers and then plug in and input the correct series of A's and B's to get the final password on the Microbit
5. They entered this password on the webpage and won the game!

When they won, the students were instructed to Chromecast a new window and follow a link. This link played a Youtube video that was a school-wide inside joke. After having a good laugh, I also brought them snacks.

Student reviews of the activity:

**"This class is actually lit."** - Anonymous Senior

**"Did Ms. Pries just troll us?"** - Anonymous Senior

More information on each of the puzzles as well as facilitation notes follows. Refer to the [webpage](https://mspries.github.io/escape/escape.html) for full problem descriptions.

### The Puzzles
1. [Dorothy - Pathfinding](#dorothy---pathfinding)
2. [Lion - Handwriting Recognition](#lion---handwriting-recognition)
3. Scarecrow - XOR Neural Network
4. [Tin Man - AI Ethics](#tin-man---ai-ethics)
5. Pop Quiz

### 1. Dorothy - Pathfinding

This puzzle built off their work with [Q-Learning for pathfinding](https://github.com/emilypries/q_learning_demo) by directing them to [this repo](https://github.com/MsPries/YellowBrickRoad) to "follow the yellow brick road."

![maze-image](https://mspries.github.io/escape/img/road.png)

This program challenges the student to navigate their orange player to the golden goal square a certain number of times in a row, each time taking no more than a certain number of steps. Compared to the version they had seen before, this puzzle extends the board and introduces more obstacles, so that in order to finish the game before time ran out, the students would need to tailor the code.

There are many possible improvements, and I anticipated students following up on our prior conversations about paralellization and parameter optimization and modifying the learning rate across multiple instances of the program or multiple computers and getting the clue from whichever instance finished first.

I also like to encourage students to think "out of the box," so they asked if they could write a way to manually navigate using the keyboard. Anticipating this, the "up" "down" "left", and "right" actions were misaligned for the player, giving them some challenge. I accepted that solution, particularly since I appreciate the opportunity to encourage them to show skepticism when someone appears to "throw AI" at a problem that doesn't need it.

When solved, the program printed a clue to the command line.

### 2. Lion - Handwriting Recognition

This puzzle built off their prior work with handwriting recognition and challenged students to convert an image of handwritten digits into digital characters.

![handwritten-digits](https://raw.githubusercontent.com/MsPries/TensorFlow-MNIST/master/secret_code.png)

I gave starter code for interacting with image [here](https://github.com/MsPries/TensorFlow-MNIST/), including an individual character and smaller test case to try out their ideas.

To solve it, students needed to see the image of digits as a grid of pixels. From there, they iterated through the image, isolating blocks of pixels and identifying individual digits using the pretrained "brain."

This puzzle was intended to prompt questions about the scale at which switching from human labor to computer labor made sense as well as to check that they understood the difference between training a new neural network and using an existing one. They also needed to practice reading PIL (Python Image Library) documentation in order to crop the image in the ways they needed. Implementing this logic proved more challenging for the students in each section than tying into the MNIST network.

Once they got a string of digit characters, the students entered that string on the webpage and received a clue.

### 4. Tin Man - AI Ethics

This "puzzle" was a little different. Students read [an article](http://www.slate.com/articles/technology/bitwise/2014/07/roko_s_basilisk_the_most_terrifying_thought_experiment_of_all_time.html) about Roko's Basilisk, a thought experiment around the development of malevolent superintelligence. They then had to commit to either working towards creating this superintelligent being or refusing to do so, at the risk of eternal punishment should our reality prove to be a simulation itself. Either choice was acceptable, but students were required to defend their position.

This puzzle was frustrating for a few students who expected a "right" answer. It also messed with the minds of a few students (in a good way). A few students voted and gave a logical explanation, but made it clear that they thought the premise was ridiculous.

In my smaller section, I had the students read the article ahead of time and come and discuss as a class. In my larger section, I gave no extra context. When students broke into small groups to work on different puzzles (without reading the problem statements ahead of time, as the students self-reflected!), the group that worked on this "puzzle" played the role of explaining the thought experiment. They took a while to read and I think they may have felt as though the missed out on some of the coding-based problem solving.
