# Movie Suggestion System

We want to create a movie suggestion system. The user will input any movies they have recently watched, along with a score they give them. They will also be given the option to input what genres they like. Our goal will then be to develop an AI that will sort through a dataset of movies finding similar movies which the user would be interested in. We will achieve this by implementing three searching algorithms for this project, a breadth-first search, which will give more general suggestions, a depth-first search, giving recommendations very similar to each other, and a heuristic search, which will be most tailored to the user.

# Running...

To be able to run the program for ther first time, please run
`win-dependencies`
on windows

# The Problem

The program will always start by prompting the user to enter information. They will have 3 options, input recent movies they have watched and how they felt about them, input genres they enjoy, or they can choose to input both.

When inputting their recent films, they will be prompted to input the name and how they personally rate the film. If the movie is not found in the dataset, they will also be prompted to answer follow up questions. These are, the genre and up to 5 leading actors.

When choosing genres, the user will input their favourite 3 genres and up to 10 other liked genres. They will also be prompted to input disliked genres and be able to blacklist genres.

If the user picks the both option it will combine these two, first asking about the films and then about the genres.

The results of these will be the output of a highly recommended movie. There will also be the option to sort by their favourite genres and actors.

The user will be able to say if they have already watched the highly recommended movie to show that the search worked, or they will be able to review it. A high review meaning it worked as intended.

We will track the recommendations cost by seeing how many movies they go through before finding one they want to watch.

We will also track the user preference cost which will track how often the system is suggesting irrelevant movies costing user dissatisfaction.

# Assignment Brief

Building on lecture materials and lab exercises, your task is to identify an interesting problem
that can be solved, at least in part, by three of the search strategies we have studied in the AI
part of the module. The choice of problem is unrestricted, but the size of the work must be
suitable for the available time (5 weeks) and group size (up to 5 people).
In choosing your problem and planning your work, keep in mind the four questions we have
discussed in class:

1. What is the AI problem that we want to solve?
2. Why it is an important problem to solve?
3. How can we solve it?
4. How can we solve it in a better way (faster, more robust, and efficient)?

You will need to produce a project proposal describing your problem and why it matters, the
dataset you will use, and what results you expect to get from the analysis. We will provide
feedback on this proposal in terms of scope and suitability of the project. Based on this feedback,
you should carry out any preparations of the data and infrastructure to solve your problem. You
should collect and interpret any results in terms of the problem definition, of the performance
of the chosen search strategies, and of their real-world meaning. Finally, you should critically
assess your work, identifying challenges, limitations, and opportunities for improvement. Pay
special attention to aspects of your approach that link the analysis to the algorithms involved
and their complexity (e.g. if you are forced to reduce the size of your dataset so that you can run
the analysis algorithms within your time and memory constraints).
You will report on your work in a 15-minute presentation to the lecturing team and the rest of
the class during Week 11. The presentation should focus on the problem and its relevance, and
the results and interpretation of your results, avoiding technical details. At the end of the project,
you will submit a written report in which you can describe in more detail your approach, the
strategies you used, your results and their interpretation, possible future enhancements, and
any relevant considerations linking your work to relevant algorithms and their complexity.
