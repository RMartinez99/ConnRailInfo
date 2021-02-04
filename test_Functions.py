import sqlite3
import json
import unittest
# import sys
class BasicTestCase(unittest.TestCase):
    def test_sqlite(self):
        sqliteConnection = sqlite3.connect('Stations.sqlite3')
        cursor = sqliteConnection.cursor()
        cursor.execute("select * from Stations")
        stations_L = cursor.fetchall()
        stations = dict(stations_L)
        print("PASS")

    def test_json(self):
        timeTable = {}
        station = "Stamford"
        entry = "1"
        company = "Amtrak"
        trainNum = "66"
        arrTime = "3:30 AM"
        dest = "Boston, MA"
        trainString = f"Company: {company}, #{trainNum}, Due: {arrTime}, Destination: {dest}"
        timeTable[entry] = trainString
        if timeTable == {}:
            print("FAIL")
    
        else:
            with open(f'{station}.json', 'w') as w:
                json.dump(timeTable, w, sort_keys=True, indent = 3)

if __name__ == '__main__':
    unittest.main()
    
