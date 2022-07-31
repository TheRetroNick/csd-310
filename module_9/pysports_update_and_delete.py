# Nick Schmid
# Assignment 9.3
# Pysports Update and Delete

from re import template
from tkinter.tix import Select
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

#
#
### This is the INSERT 

# Set the cursor to point to the data in database
    cursor = db.cursor()

# Set the new code to INSERT the new player
    inserted = "INSERT INTO player (first_name, last_name, team_id)\
        VALUES('Smeagol', 'Shire Folk', 1)"

# Execute the Join code
    cursor.execute (inserted)

    result = cursor.fetchall()

# Set the new code to join the tables
    joined = "SELECT p.player_id, p.first_name, p.last_name, t.team_name\
    FROM player AS p\
    INNER JOIN team AS t\
        ON p.team_id = t.team_id"

# Execute the Join code
    cursor.execute (joined)

    result = cursor.fetchall()

# Print the result    
    print(" --DISPLAYING PLAYERS AFTER INSERT-- ")
    for player in result:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
    input("\n\n Press any key to continue...")

#
#
### This is the UPDATE 

# Set the cursor to point to the data in database
    cursor = db.cursor()

# Set the new code to UPDATE the player
    updated = "UPDATE player\
        SET team_id = 2,\
            first_name = 'Gollum',\
            last_name = 'Ring Stealer'\
        WHERE first_name = 'Smeagol'"

# Execute the Join code
    cursor.execute (updated)

    result = cursor.fetchall()

# Set the new code to join the tables
    joined = "SELECT p.player_id, p.first_name, p.last_name, t.team_name\
    FROM player AS p\
    INNER JOIN team AS t\
        ON p.team_id = t.team_id"

# Execute the Join code
    cursor.execute (joined)

    result = cursor.fetchall()

# Print the result    
    print(" --DISPLAYING PLAYERS AFTER UPDATE-- ")
    for player in result:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
    input("\n\n Press any key to continue...")

#
#
### This is the DELETE 

# Set the cursor to point to the data in database
    cursor = db.cursor()

# Set the new code to DELETE the player
    deleted = "DELETE FROM player\
        WHERE first_name = 'Smeagol'"
        #'Smeagol' in this case only deletes the old Smeagol file, 
        # but it will leave a lot of 'Gollum' player files if run repeatedly.


# Execute the Join code
    cursor.execute (deleted)

    result = cursor.fetchall()

# Set the new code to join the tables
    joined = "SELECT p.player_id, p.first_name, p.last_name, t.team_name\
    FROM player AS p\
    INNER JOIN team AS t\
        ON p.team_id = t.team_id"

# Execute the Join code
    cursor.execute (joined)

    result = cursor.fetchall()

# Print the result    
    print(" --DISPLAYING PLAYERS AFTER DELETE-- ")
    for player in result:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
    input("\n\n Press any key to continue...")

###
#
#

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
