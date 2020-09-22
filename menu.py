import sys
from makeTimeTable import TimeTableMachine
import sqlite3
import json

#Version 4.0 Beta


class Menu:
  def __init__(self):
    sqliteConnection = sqlite3.connect('Stations.sqlite3')
    cursor = sqliteConnection.cursor()
    cursor.execute("select * from Stations")
    stations_L = cursor.fetchall()
    self.stations = dict(stations_L)
    self.showMenu()
    
  
  def showMenu(self):
    print("Timetable Maker v4.0 Beta")
    code = input("Please enter a station code for a New Haven Line/CTRail terminal station.\n")
    while code not in self.stations:
        print("Sorry, but an error occurred. This occurs for one of 4 reasons:\nThe station is not a major station,\nA misentry with a station code,\nThe station doesn't exist,\nOr is not on the New Haven, Shore Line East, or Hartford Lines.\n\nReenter again.")
        code = input("")
    print(f"Welcome to {self.stations[code]}. Please choose an option below.")

    self.timeTable = TimeTableMachine(self.stations[code])
    
    print(""" 
                    1. Create Timetable Entry
                    2. Modify Timetable Entry
                    3. Delete Timetable Entry
                    4. Show Timetable Entries
                    5. Save data to database
                    Any other key: Exit program and save data as JSON
    
                """)
    self.timeTable.optionProcessor()

