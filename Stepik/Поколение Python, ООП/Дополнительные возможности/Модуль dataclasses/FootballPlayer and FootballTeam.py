from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, init=False, repr=False, compare=False)

    def add_players(self, *novices):
        for player in novices:
            self.players.append(player)


player = FootballPlayer("Kylian", "Mbappe", 180000000)

print(player)
print(player.name)
print(player.surname)
print(player.value)
print()


player1 = FootballPlayer("Jude", "Bellingham", 120000000)
player2 = FootballPlayer("Vinicius", "Junior", 120000000)
player3 = FootballPlayer("Kylian", "Mbappe", 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)
print()


team = FootballTeam("PSG")

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer("Kylian", "Mbappe", 180000000))
print(team.players)
print()


team1 = FootballTeam("PSG")
team2 = FootballTeam("PSG")
team3 = FootballTeam("Arsenal")

player1 = FootballPlayer("Jude", "Bellingham", 120000000)
player2 = FootballPlayer("Vinicius", "Junior", 110000000)
player3 = FootballPlayer("Kylian", "Mbappe", 180000000)

team1.add_players(player1)
team2.add_players(player2)
team3.add_players(player3)

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)
