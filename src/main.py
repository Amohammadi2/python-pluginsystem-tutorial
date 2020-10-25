from jsonDB import DBConnection
import os

class Program:

    def main(self):
        self.db = DBConnection(f"../JSON/{input('enter your class name: ')}.json")

        try:
            while True:
                self.db.insertData(self.getInput())
        except KeyboardInterrupt:
            print ("opening json file ...")
            os.system(f"{'notepad' if os.name=='nt' else 'nano'} {self.db.db_file}")

    def getInput(self):
        return {
            "first-name": input("enter your first name: "),
            "last-name": input("enter your last name: "),
            "grade": int(input("which grade are you at? (enter a number) : "))
        }

if __name__ == "__main__": Program().main()