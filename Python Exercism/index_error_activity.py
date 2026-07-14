def process_player_record(player_id):
    #player_id < len(player_record) and player_id > -1
    try:
        player_record = get_player_record(player_id)
        return player_record
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
