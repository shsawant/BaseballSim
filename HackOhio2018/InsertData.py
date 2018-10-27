import mysql.connector
from pybaseball import statcast_batter
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
from pybaseball import statcast


mydb = mysql.connector.connect(
  host="localhost",
  password = "password",
  user="username",
  database="baseball"
)

#get players for both team
players = [("corey", "kluber"), ("yan", "gomes"), ("yonder", "alonso"), ("jose", "ramirez"), ("josh", "donaldson"), ("francisco", "lindor"), ("melky", "cabrera"),("jason", "kipnis"),("michael", "brantley"),("luis", "castillo"), ("tucker", "barnhart"), ("joey", "votto"), ("scooter", "gennett"), ("eugenio", "suarez"), ("mason", "williams"),("billy", "hamilton"),("preston","tucker"),("jose","peraza")]

mycursor = mydb.cursor()
#get player data
for player in players:
    id = playerid_lookup(player[1], player[0])
    print(len(id))
    if len(id) == 1:
        stats = statcast_batter('2018-3-29', '2018-10-02', id.key_mlbam.iloc[0])
        hr = 0
        bip = 0
        tot = 0
        for event in stats.events:
            tot = tot+1
            if event == 'home_run':
                hr = hr + 1
            if type(event) != float and event != "strikeout" and event != "walk" and event != "home_run":
                bip = bip + 1
        sql = "INSERT INTO batters (NAME, HR, BIP) VALUES (%s, %s, %s)"
        val = (f'{player[0]} {player[1]}', hr/tot, bip/tot)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print(f'{player[1]}, {player[0]}')


#some players have multiple ids, for these we ignore
