"""tests"""
import pytest
from board import Board


@pytest.mark.parametrize("border_size,num_cells", [(10, 100), (0, 0), (3, 9)])
def test_board_size(border_size: int, num_cells: int):
    """checks border size"""
    board = Board(border_size=border_size)
    assert board.num_cells == num_cells
