import json
import os
from validators import DataValidator

class DBConnection:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not DBConnection.instance:
            DBConnection.instance = super().__new__(cls)
        return DBConnection.instance

    def __init__(self, db=None):
        self.db_file = db or "../JSON/db.json"
        try:
            with open (self.db_file, "r") as infile:
                if os.stat(self.db_file).st_size <= 1:
                    with open (self.db_file, "w") as outfile:
                        outfile.write("[]") #initialize
                self.db_data = json.load(infile)
        except FileNotFoundError:
            os.system(f"echo [] > {self.db_file}") # HACK
            self.__init__(db)
            

    def insertData(self, data: dict):
        self.db_data.append(data)
        if DataValidator(data).isValid():
            self.commitData()

    def commitData(self):
        with open(self.db_file, "w") as file:
            json.dump(self.db_data, file, indent=4)
