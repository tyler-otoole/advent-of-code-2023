# Read the input from a .txt file
def read_input(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

# Check if a single game is possible based on the cube limits
def is_game_possible(game_info, max_red, max_green, max_blue):
    # Split game_info into its subsets (separated by semicolons)
    subsets = game_info.split(';')
    
    # Check each subset to ensure it does not exceed the available cubes
    for subset in subsets:
        # Extract counts of red, green, and blue cubes from each subset
        cubes = subset.split(',')
        red_count = green_count = blue_count = 0
        
        # Process each cube count and color
        for cube in cubes:
            count, color = cube.strip().split(' ')
            count = int(count)
            if color == 'red':
                red_count += count
            elif color == 'green':
                green_count += count
            elif color == 'blue':
                blue_count += count
        
        # If any count exceeds the available cubes, the game is impossible
        if red_count > max_red or green_count > max_green or blue_count > max_blue:
            return False
    
    # If no subset exceeded the available cubes, the game is possible
    return True

# Main function to process the games and sum valid game IDs
def find_valid_games(file_path, max_red, max_green, max_blue):
    # Read the input data
    lines = read_input(file_path)
    
    # Initialize the sum of valid game IDs
    valid_game_sum = 0
    
    # Process each line of input
    for line in lines:
        # Each line is of the format: Game ID: cubes information
        game_info = line.strip().split(':')
        game_id = int(game_info[0].strip().split()[1])
        cubes_info = game_info[1].strip()
        
        # Check if the game is possible
        if is_game_possible(cubes_info, max_red, max_green, max_blue):
            valid_game_sum += game_id
    
    return valid_game_sum

# part 1 solution
file_path = 'data/input/day2.txt' # relative file path
max_red = 12
max_green = 13
max_blue = 14

result = find_valid_games(file_path, max_red, max_green, max_blue)
print(f"Sum of valid game IDs: {result}")


#### PART TWO ####


# Function to calculate the minimum cubes required for a game
def min_cubes_for_game(cubes_info):
    # Initialize minimum required cubes to 0
    min_red = min_green = min_blue = 0
    
    # Split the cubes_info into subsets of cubes
    subsets = cubes_info.split(';')
    
    # Process each subset to determine the max cubes needed for each color
    for subset in subsets:
        cubes = subset.split(',')
        red_count = green_count = blue_count = 0
        
        for cube in cubes:
            count, color = cube.strip().split(' ')
            count = int(count)
            
            if color == 'red':
                red_count = max(red_count, count)
            elif color == 'green':
                green_count = max(green_count, count)
            elif color == 'blue':
                blue_count = max(blue_count, count)
        
        # Update the minimum required cubes
        min_red = max(min_red, red_count)
        min_green = max(min_green, green_count)
        min_blue = max(min_blue, blue_count)
    
    # Return the minimum cubes required for red, green, and blue
    return min_red, min_green, min_blue

# Main function to process the games and sum the powers of the minimum cube sets
def sum_of_powers(file_path):
    # Read the input data
    lines = read_input(file_path)
    
    # Initialize the sum of powers
    total_power = 0
    
    # Process each line of input
    for line in lines:
        # Extract the game ID and cubes information
        game_info = line.strip().split(':')
        game_id = int(game_info[0].strip().split()[1])  # Extract game ID
        cubes_info = game_info[1].strip()  # Extract cubes information
        
        # Calculate the minimum cubes required for each color
        min_red, min_green, min_blue = min_cubes_for_game(cubes_info)
        
        # Calculate the power of the minimum set of cubes
        power = min_red * min_green * min_blue
        
        # Add the power to the total sum
        total_power += power
    
    return total_power

# part 2 solution
file_path = 'data/input/day2.txt' # relative file path
result = sum_of_powers(file_path)
print(f"Sum of powers: {result}")