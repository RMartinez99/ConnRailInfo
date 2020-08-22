import json
import sys

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
            show = Options()
            self.optionProcessor()
        elif choice == "3":
            print("Feature coming soon in Version 2")
            show = Options()
            self.optionProcessor()
        elif choice == "4":
            self.showTable()
        else:
            sys.exit(0)
        
    
    def createTable(self):
        print("Give me an entry number, please")
        entry = input("")
        while entry in self.timeTable:
            print("Error: Entry exists for today's schedule")
            entry = input("")
        company = input("Rail Company: ")
        trainNum = input("Train Number: ")
        arrTime = input("Expected Arrival: ")
        dest = input("Destination: ")
        trainString = f"Station: {self.station}, Company: {company}, #{trainNum}, Due: {arrTime}, Destination: {dest}"
        self.timeTable[entry] = trainString
        show = Options()
        self.optionProcessor()

    
    def showTable(self):
        print(self.timeTable)
        show = Options()
        self.optionProcessor()
    
    def modTimeTable(self):
        entry = input("Give me an entry number, please")
        while entry not in self.timeTable:
            print("Error: Entry not found. Try again")
            entry = input("")
        company = input("Rail Company: ")
        trainNum = input("Train Number: ")
        arrTime = input("Expected Arrival: ")
        dest = input("Destination: ")
        trainString = f"Station: {self.station}, Company: {company}, #{trainNum}, Due: {arrTime}, Destination: {dest}"
        self.timeTable[entry] = trainString
        show = Options()
        self.optionProcessor()

class Options:
    def __init__(self):
        self.showMenu()

    def showMenu(self):
       print(""" 
                    1. Create Timetable
                    2. Modify Timetable
                    3. Delete Timetable
                    4. Show Timetables
                    Any other key: Exit program
    
                """)

    