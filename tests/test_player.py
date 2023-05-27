import pytest
from pywordle.player import Player

def test_constructor():
    player = Player()

    assert player.ATTEMPTS == 0

def test_player_lost_attempt():
    player = Player()
    player.lost_attempt()

    assert player.ATTEMPTS == 1

    player.lost_attempt()

    assert player.ATTEMPTS == 2