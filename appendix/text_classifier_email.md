## Check for Understanding: Neural Network Fundamentals
###### I shared copies of the following example email to check for understanding on neural network basics. I asked students to discuss what they read, pointing on successes and flaws in the described design. In particular, I wanted to make sure the understood bias in input data, the role of preprocessing, backpropagation, appropriate bounds on the size of hidden layers, and training vs. testing. I also wanted them to discuss whether such a program _should_ be built and if it is, how we should interpret its results. In each section, the discussion made its way there naturally. This worked well as a discussion and each section resolved a few lingering ambiguities; annotating this individually would make a good homework assignment and would have given me a more granular read on individual students' gaps in understanding.
---
Hi there!

I’ve been working on using artificial intelligence to build a text classifier and I am hoping to hear your thoughts.

I want to build a program that predicts whether or not any high school student will get accepted to their first choice college based on their essays. The data I plan to use are one essay from each of the Milton Academy valedictorians and salutatorians from the past 50 years.

I am planning to train a basic feedforward neural network with one hidden layer and using a sigmoid function for backpropagation. To be honest, I am not 100% sure what backpropagation is or why I should use a sigmoid function – can you explain that quickly? I just saw online that it was a good idea. I am going to maintain a vocabulary with every word from every essay so that I don’t lose any information, so I expect the input layer to contain about 60,000 nodes. I want to keep associated info together so each row will represent one full essay. The output layer will be one binary node representing whether or not a student was accepted to their first choice college. I plan to use four nodes in the hidden layer.

To test how well my model is trained, I will feed two random essays from the training set through and see what they output. If they both output the correct decision (ie, the student was or was not accepted to their first choice school), then I will consider the model a success.

I am really hoping this works, because I want to sell this to college admissions offices. I think they will pay a lot for it since it will decrease how much time they need to spend time reading essays since they can just send the essay through my program to decide whether a student should get in or not!

Please let me know what I am doing right and what I should consider changing. Thanks for your time, and I look forward to your response!

