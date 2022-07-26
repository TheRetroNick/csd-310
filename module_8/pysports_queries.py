# Nick Schmid
# Assignment 8.2
# MySQL Connection test

import mysql.connector
from mysql.connector import errorcode


# database config object
config = {
    "user": "root",
    "password": "retroVirtual7854!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

# Connection and print results
try:
    db = mysql.connector.connect(**config)
    print(db)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

# Team Records are the first output
    print()
    print(" --DISPLAYING TEAM RECORDS-- ")

#Set the cursor to point to the data in database
    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()

# Use a line for each output, space at the end
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()
    
# Repeat for the player data    
    print (" --DISPLAYING PLAYER RECORDS-- ")
    acursor = db.cursor()

    acursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players = acursor.fetchall()

    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()

# In case the connection is bad
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
