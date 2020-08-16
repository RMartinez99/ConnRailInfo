import json
import sys
from menu import AltMenu

class TimeTableMachine():
    def __init__(self, station):
        self.station = station
        self.timeTable = {}

    def optionProcessor(self):
        choice = input("")
        
        if choice == "1":
            self.createTable()
        elif choice == "2":
            print("feature coming in a later version")
        elif choice == "3":
            print("feature coming soon in a later version")
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
        self.showMenu = AltMenu()
        self.optionProcessor()

    
    def showTable(self):
        print(self.timeTable)
        self.showMenu = AltMenu()
        self.optionProcessor()

    