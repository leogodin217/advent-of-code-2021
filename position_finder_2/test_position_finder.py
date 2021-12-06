from position_finder import get_input
from position_finder import get_position_change
from position_finder import get_movements
import sure


def test_get_input():
    movements = get_input()
    movements.should.be.a(list)


def test_get_movements_handles_forward_movements():
    movements = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]
    get_movements(movements, 'horizontal').should.equal([5, 8, 2])


def test_get_movements_handles_vertical_movements():
    movements = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]
    get_movements(movements, 'virtical').should.equal([5, -3, 8])


def test_get_position_change_gets_correct_change():
    position_changes = [1, -1, 2, -3]
    get_position_change(position_changes).should.equal(-1)
