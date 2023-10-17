# Algorithm for Scheduling Tournaments

This Python script implements an algorithm for tournament scheduling for a specified number of teams. It employs a greedy algorithm to determine the tournament's match order.


## Usage Instruction

1. Ensure that Python 3 is installed on your computer.
2. Clone this repository onto your local system.
3. Open a command prompt or terminal.
4. Navigate to the directory for the project.
5. Execute the script with the following command:
   > python tournament_scheduler.py
6. Provide the total number of teams.
7. The tournament schedule will be printed for the given number of teams.

## Compoment Overview

- 'MatchList': Class for generating a list of all inter-team contests.
- 'List': General list class used to manage matches for a day and remaining matches.
- 'Graph': Class used to represent matches as nodes and edges between successive matches.
- 'OccurringInList': Function for determining whether a match is included in the roster of matches for a given day.
- 'GreedyAlgorithm': Implementation of the tournament scheduling algorithm.
- 'main': The program's entry point.


## Contact Information

Please [contact me](mailto:luckyharrysingh@gmail.com) if you have any queries or comments.
