class Status:
    def __init__(self, data):
        self.online: bool = data.get("online")
        self.players: StatusPlayers = StatusPlayers(data)


class StatusPlayers:
    def __init__(self, data):
        self.online = data.get("onlinePlayers", 0)
        self.max = data.get("maxPlayers", 0)
