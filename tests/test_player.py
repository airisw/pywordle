from pywordle.player import Player

def test_players_lives():
    player = Player()

    assert player.LIVES == 6

def test_player_lost_life():
    player = Player()
    player.lost_life()

    assert player.LIVES == 5

    player.lost_life()

    assert player.LIVES == 4