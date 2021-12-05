
# 1583 depth increases
def get_input():
    '''
    Reads the input data into a list
    '''
    depths = []
    with open('input.txt', 'r') as f:
        depths = f.readlines()

    depth_ints = [int(depth) for depth in depths]
    return depth_ints


def count_increases_accumulator(depths):
    '''
    This version uses an iterator and accumulator to determine
    the number of times a depth increases

    Args:
        depths (list: int): A list of depth readings in order  

    Returns:
        int: Number of times the depth increases 
    '''

    # Iterate over the depths, while comapring the current depth
    # with the previous depth.
    num_increases = 0
    previous_depth = depths[0]  # First record will never be an increase
    for depth in depths:
        if depth > previous_depth:
            num_increases += 1
        previous_depth = depth

    return num_increases


def count_increases_zipped(depths):
    '''
    This version creates tuples of previous/next depths, then sums the boolean comparison to
    determine the number of times a depth increases. While this may possibly seem more Pythonic,
    it is difficult to read and performs slower than the accumulator version.

    Args:
        depths (list: int): A list of depth readings in order  

    Returns:
        int: Number of times the depth increases 
    '''

    # The first value can never increase, so we remove it
    current_depths = depths[1:]
    previous_depths = depths
    increases = [depth[0] > depth[1]
                 for depth in zip(current_depths, previous_depths)]

    return sum(increases)


def count_increases_rolling_three(depths):
    '''
    Measure the number of times depth increases using a 3-depth rolling window. This problem
    is the same as the first one once we get the rolling windows.

    Args:
        depths (list: int): A list of depth readings in order  

    Returns:
        int: Number of times the depth increases 
    '''

    rolling_windows = get_rolling_windows(depths)
    return count_increases_accumulator(rolling_windows)


def get_rolling_windows(depths):
    '''
    Creates a rolling window of sums of 3 from a list. In a real-world use case
    I would add an arg for window_size. Not needed here, but makes sense.

    Args:
        depths (list: int): List of depth readings in order 

    Returns:
        list: List of sums of a rolling 3 window
    '''

    windows = []

    # Iterate from the first item of the list to the 3rd from last
    for i in range(len(depths))[:-2]:
        start = i  # Start position in the list
        stop = i + 3  # First item in the list not included
        window = sum(depths[start:stop])
        windows.append(window)

    return windows


def get_answers():
    '''
    Prints answers for question 1 and question 2
    '''
    depths = get_input()
    depth_increases = count_increases_accumulator(depths)
    print(f'Day 1 - answer 1: {depth_increases}')
    rolling_three_increases = count_increases_rolling_three(depths)
    print(f'Day 1 - answer 2: {rolling_three_increases}')
