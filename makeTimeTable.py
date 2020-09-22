import json
import sys
#Version 4.0 Beta
class TimeTableMachine():
    def __init__(self, station):
        self.station = station
        self.timeTable = {}

    def optionProcessor(self):
        choice = input("")
        
        if choice == "1":
            self.createTable()
        elif choice == "2":
            self.modTimeTable()
        elif choice == "3":
            self.delTimeTable()
        elif choice == "4":
            self.showTable()
        elif choice == "5":
            if self.timeTable == {}:
                print("Sorry, I cannot put empty data into database. It makes no sense to do so.")
            else:
                pass
        else:
            if self.timeTable == {}:
                sys.exit(0)
            else:
                print(f"Saving data for station {self.station}.")
                
                with open(f'{self.station}.json', 'w') as w:
                    json.dump(self.timeTable, w, sort_keys=True, indent = 3)

    
    def createTable(self):
        print("Give me an entry number, please")
        entry = input("")
        while entry in self.timeTable:
            print("Error: Entry exists for today's schedule. Please try another number.\n")
            entry = input("")
        company = input("Rail Company: ")
        trainNum = input("Train Number: ")
        arrTime = input("Expected Arrival: ")
        dest = input("Destination: ")
        trainString = f"Company: {company}, #{trainNum}, Due: {arrTime}, Destination: {dest}"
        self.timeTable[entry] = trainString
        show = Options()
        self.optionProcessor()

    
    def showTable(self):
        print(self.timeTable)
        show = Options()
        self.optionProcessor()
    
    def modTimeTable(self):
        entry = input("Give me an entry number, please.\n")
        while entry not in self.timeTable:
            print("Error: Entry not found. Try another entry")
            entry = input("")
        company = input("Rail Company: ")
        trainNum = input("Train Number: ")
        arrTime = input("Expected Arrival: ")
        dest = input("Destination: ")
        trainString = f"Company: {company}, #{trainNum}, Due: {arrTime}, Destination: {dest}"
        self.timeTable[entry] = trainString
        show = Options()
        self.optionProcessor()
    
    def delTimeTable(self):
        entry = input("Tell me what entry you want to delete.\n")
        while entry not in self.timeTable:
            print("Error: Could not delete. Entry not found. Enter a valid entry.")
            entry = input("")
        self.timeTable.pop(entry)
        show = Options()
        self.optionProcessor()

class Options:
    def __init__(self):
        self.showMenu()

    def showMenu(self):
       print(""" 
                    1. Create Timetable Entry
                    2. Modify Timetable Entry
                    3. Delete Timetable Entry
                    4. Show Timetable Entries
                    5. Save Entries to Database
                    Any other key: Exit program and save data to JSON
    
                """)

    