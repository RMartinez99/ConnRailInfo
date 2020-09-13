import sys
from makeTimeTable import TimeTableMachine

#build 12
major_stations = {"NYG": "Grand Central",
"NYP" : "New York Penn Station",
"125" : "Harlem - 125th Street", 
"153" : "Yankees - E. 153rd Street", 
"FRD" : "Fordham", 
"NRO" : "New Rochelle", 
"PCX" : "Port Chester",
"GCH" : "Greenwich",
"STM" : "Stamford", 
"NCN" : "New Canaan", 
"SNW" : "South Norwalk",
"DBY" : "Danbury",
"BRP" : "Bridgeport",
"WBR" : "Waterbury",
"NHV" : "New Haven Union Station",
"STS" : "New Haven - State St.",
"OSB" : "Old Saybrook",
"NLC" : "New London",
"HFD" : "Hartford",
"SPG" : "Springfield"}

class Menu:
  def __init__(self, major_stations):
    self.stations = major_stations
    self.showMenu()
    
  
  def showMenu(self):
    print("Timetable Maker v3.1 Beta")
    code = input("Please enter a station code for a MAJOR New Haven Line/CTRail station.\n")
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
                    5. Read Timetable File
                    Any other key: Exit program
    
                """)
    self.timeTable.optionProcessor()

