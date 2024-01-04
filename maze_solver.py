import random
from queue import Queue
# Define constants for maze elements

# <---- COLOR CODES ---->
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
END_COLOR = "\033[0m" 

# <---- MAZE ELEMENTS ---->
WALL = f'{RED}▓{END_COLOR}'
OPEN_SPACE = f'{BLUE}◌{END_COLOR}'
START = 'S'
END = 'E'
PATH = f'{GREEN}◍{END_COLOR}'

# <---- MAZE GENERATION ---->
def generate_maze(n, wall_percentage):
    maze = [[OPEN_SPACE] * n for _ in range(n)]
    # Add walls
    num_walls = int(n * n * wall_percentage / 100)
    for _ in range(num_walls):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = WALL
    # Set start and end points
    maze[0][0] = START
    maze[n - 1][n - 1] = END
    return maze
  
def print_maze(maze):
    for row in maze:
        print(" ".join(row))
        
def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        current, path = queue.get()
        if current == end:
            return path
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, path + [neighbor]))
    return None
  
def get_neighbors(maze, current):
    row, col = current
    neighbors = []
    # Check up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != WALL:
            neighbors.append((new_row, new_col))
    return neighbors
  
def mark_path(maze, path):
    for row, col in path:
        if maze[row][col] != START and maze[row][col] != END:
            maze[row][col] = PATH
            
def main():
    try:
        while True:
            n = int(input("Enter the size of the maze (n x n): "))
            wall_percentage = int(input("Enter the percentage of walls (<= 25%): "))
            
            if wall_percentage > 25:
                print("Please enter a value between 0 to 25.")
                continue  # Restart the loop
            
            maze = generate_maze(n, wall_percentage)
            print("\nGenerated Maze:")
            print_maze(maze)
            
            option = input(f"{CYAN}\nChoose an option: P (Generate path and Print), G (Generate another puzzle), E (Exit): {END_COLOR}").upper()
            
            if option == 'P':
                path = find_path(maze)
                if path:
                    mark_path(maze, path)
                    print("\nPath Found:")
                    print_maze(maze)
                    
                    ask_option = input(f"{CYAN}\nChoose an option: G (Generate another puzzle), E (Exit): {END_COLOR}").upper()
                    if ask_option == 'G':
                        continue  # Restart the loop for generating another puzzle
                    elif ask_option == 'E':
                        print("Exiting the game.")
                        break  # Exit the loop and end the program
                    else:
                        print("Invalid option. Exiting the game.")
                        break  # Exit the loop and end the program
                    
                else:
                    print("\nNo Path Found.")
            elif option == 'G':
                continue  # Restart the loop for generating another puzzle
            elif option == 'E':
                print("Exiting the game.")
                
                break  # Exit the loop and end the program
            else:
                print("Invalid option. Please enter P, G, or E.")
    except KeyboardInterrupt:
        print("\nExiting the game.")            
if __name__ == "__main__":
    main()

