# Name: Harmeet Singh



# ------------------------------------------------------------
# Define a List storing all the matches needed to be played
# (MatchList class stores a list of all matches between every team)
# ------------------------------------------------------------
#   For eg.: For 3 teams, map represents the below array
#   [(1,2), (1,3), (2,3), (2,1), (3,1), (3,2)]
# ------------------------------------------------------------
class MatchList:
    # Constructor
    def __init__(self, size):
        self.size = size
        
        match_size = (size * (size-1))
        offset = int((size * (size-1)) / 2)

        self.map = [(None,None)] * match_size

        i = 0
        for j in range(1, size):
            for k in range(j+1, size+1):
                self.map[i] = (j, k)
                self.map[i+offset] = (k, j)
                i += 1
    
    # Function to check if two matches have atleast one team in common
    def is_consequent(self, i, j):
        if self.map[i][0] == self.map[j][0] or self.map[i][0] == self.map[j][1] or self.map[i][1] == self.map[j][0] or self.map[i][1] == self.map[j][1]:
            return True
        else:
            return False
    
    # Function to print the map
    def print_map(self):
        for i in range(len(self.map)):
            print(f"{i}: ({self.map[i][0]}, {self.map[i][1]})", end=" ")
        print()


# ------------------------------------------------------------
# Define a general List class
# ------------------------------------------------------------
# We use this class for two purposes: 
#   1. To store the list of matches that are played on a particular day
#   2. To store the list of matches that are remaining to be played overall (remaining_matches)
# ------------------------------------------------------------
class List:
    def __init__(self, size, val):
        self.size = size
        self.list = [val] * size
    
    def find_next_match(self):
        for i in range(self.size):
            if self.list[i] == 1:
                self.list[i] = 0
                return i
        return -1

    def print_list(self):
        for i in range(self.size):
            print(self.list[i], end=" ")
        print()


# ------------------------------------------------------------
# Define a Graph class to store the matches as nodes and edges between matches that are consequent
# (Consequent matches means matches that have atleast one team in common)
# ------------------------------------------------------------
#   For eg.: For 3 teams, the graph represents the below adjacency matrix
#   0 1 1
#   1 0 1
#   1 1 0
# ------------------------------------------------------------
class Graph:
    def __init__(self, nodes_size, match_map):
        self.size = nodes_size
        self.adjacency_list = [[0 for i in range(nodes_size)] for j in range(nodes_size)]

    def create_edges_between_consequent__matches(self, match_map):
        for i in range(self.size):
            for j in range(self.size):
                if match_map.is_consequent(i, j) == True:
                    # print('1', end=" ")
                    self.adjacency_list[i][j] = 1
                else:
                    # print('0', end=" ")
                    self.adjacency_list[i][j] = 0
        
    def set_col(self, row):
        for i in range(self.size):
            self.adjacency_list[i][row] = 1

    def print_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjacency_list[i][j], end=" ")
            print()

# ------------------------------------------------------------
# Function to check if a match is already present in the list of matches played on a particular day
# or is consequent to a match already present in the list of matches played on a particular day
# ------------------------------------------------------------
def OccuringInList(match_index, idx, temp, match_num):
    for i in range(idx):
        if match_index.is_consequent(temp.list[i],match_num):
            return True
    return False

# ------------------------------------------------------------
# Function to find the tournament sequence using the greedy algorithm
# ------------------------------------------------------------
def GreedyAlgorithm(g, match_size, match_index):
    # Define the list of remaining matches and tournament sequence
    remaining_match_count = match_size
    tournament_sequence = []
    remaining_matches = List(match_size, 1)

    # While there are matches remaining to be played in the tournament
    while(remaining_match_count > 0):
        # Define a list for the matches played on a particular day
        cur_day_matches = []

        #Define a list to store the matches that have been played on a particular day
        temp = List(match_size, -1)
        idx = 0

        # Find the next match to be played on that day and append it to the list of matches played on that day
        cur_match = remaining_matches.find_next_match()
        cur_day_matches.append(match_index.map[cur_match])

        # Decrease the number of remaining matches
        remaining_match_count -= 1

        # Add the match to the list of matches played on that day
        temp.list[idx] = cur_match
        idx += 1

        # Set the column of the match to 1 (so that the match is not played again)
        g.set_col(cur_match)

        # Find the next matches that can be played on that day
        for i in range(match_size):
            
            # If the match is not played yet and it is not already present in the list of matches played on that day
            # (or consequent to a match already present in the list of matches played on that day)
            if g.adjacency_list[cur_match][i] == 0 and not OccuringInList(match_index, idx, temp, i):
                # Add the match to the list of matches played on that day
                cur_day_matches.append(match_index.map[i])
                temp.list[idx] = i
                idx += 1
                remaining_matches.list[i] = 0
                remaining_match_count -= 1
                g.set_col(i)
        
        # Append the list of matches played on that day to the tournament sequence
        tournament_sequence.append(cur_day_matches)
    
    # Return the tournament sequence
    return tournament_sequence


# ------------------------------------------------------------
# Main function
# ------------------------------------------------------------
if __name__ == '__main__':
    # Take number of teams playing the matches as input
    n = int(input("Enter the number of Teams: "))

    if n < 2:
        print("Atleast 2 teams are required to play a tournament")
        exit()
    
    # Calculate the number of matches to be played
    match_size = n * (n-1)

    # Create the match index map :- Create a list of all matches between every team
    match_index = MatchList(n)
    # match_index.print_map()
    # print()

    # Create the graph of matches (each match is a node in the graph)
    g = Graph(match_size, match_index)
    
    # Create nodes between matches that are consequent (matches that have atleast one team in common)
    g.create_edges_between_consequent__matches(match_index)
    # g.print_graph()
    # print()

    # Find the tournament sequence using the greedy algorithm
    tournament_seq = GreedyAlgorithm(g, match_size, match_index)

    # Print the tournament sequence
    print("\nTournament Sequence:  ")
    for i in range(len(tournament_seq)):
        for j in range(len(tournament_seq[i])):
            print(tournament_seq[i][j], end="; ")
        if i != len(tournament_seq)-1:
            print('\n')
