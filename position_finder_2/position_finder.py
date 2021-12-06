

def get_input():
    moves = []
    with open('input.txt', 'r') as f:
        moves = f.readlines()
    return moves


def get_position_change(movements):
    '''
    Determines your position after a series of moves. 

    Args:
        movements (list: int): List of position changes either posative or negative 
    Returns int - The final position 
    '''
    return sum(movements)


def get_movements(movements, move_type):
    '''
    Parses positions in the form of type and amount to posative and negative integers

    Args:
        movements (list: str): [forward int, down int, up int] 
        move_type (str): Type of moves we want [horizontal, vertical]
    '''
    move_amounts = []

    # Separate the moves
    moves = [move.split() for move in movements]
    horizontal_moves = list(filter(lambda x: x[0] == 'forward', moves))
    vertical_moves = list(filter(lambda x: x[0] != 'forward', moves))

    if move_type == 'horizontal':
        move_amounts = [int(move[1]) for move in horizontal_moves]
    else:
        for move in vertical_moves:
            move_amounts.append(
                int(move[1]) if move[0] == 'down' else int(move[1]) * -1
            )

    return move_amounts


def get_position_aim(movements):
    moves = [move.split() for move in move_data]
    moves = [(move[0], int(move[1])) for move in moves]
    current_aim = 0
    current_depth = 0
    current_forward = 0

    for move in moves:
        if move[0] == 'down':
            current_aim += move[1]
        elif move[0] == 'up':
            current_aim -= move[1]
        else:
            current_forward += move[1]
            current_depth += current_aim * move[1]

    return (current_depth, current_forward, current_aim)


if __name__ == '__main__':
    move_data = get_input()
    vertical_moves = get_movements(move_data, 'vertical')
    vertical_change = get_position_change(vertical_moves)
    horizontal_moves = get_movements(move_data, 'horizontal')
    horizontal_change = get_position_change(horizontal_moves)
    print(f'Answer 1: {vertical_change * horizontal_change}')
    print(f'Veritcal change: {vertical_change}')
    print(f'Horizontal change: {horizontal_change}')

    current_depth, current_forward, current_aim = get_position_aim(move_data)
    print(f'Answer 2: {current_depth * current_forward}')
    print(f'Current depth: {current_depth}')
    print(f'Current forward : {current_forward}')
    print(f'Current aim: {current_aim}')
