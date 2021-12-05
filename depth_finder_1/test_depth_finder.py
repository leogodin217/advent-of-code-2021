from depth_finder import get_input
from depth_finder import count_increases_accumulator
from depth_finder import count_increases_zipped
from depth_finder import count_increases_rolling_three
from depth_finder import get_rolling_windows
import sure


def test_get_input_provides_a_list():
    depths = get_input()
    depths.should.be.a(list)


def test_get_input_list_contains_ints():
    depths = get_input()
    for depth in depths:
        depth.should.be.a(int)


def test_count_increases_accumulator_returns_correct_increases():
    depths = [1, 2, 3, 4, 4, 5, 0, 1]
    count_increases_accumulator(depths).should.equal(5)


def test_increases_zipped_returns_correct_increases():
    depths = [1, 2, 3, 4, 4, 5, 0, 1]
    count_increases_zipped(depths).should.equal(5)


def test_increases_rolling_three_returns_correct_increase():
    # From the example
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    count_increases_rolling_three(depths).should.equal(5)


def test_get_rolling_windows_returns_correct_windows():
    depths = [1, 2, 3, 4, 5]
    expected_windows = [6, 9, 12]
    get_rolling_windows(depths).should.equal(expected_windows)
