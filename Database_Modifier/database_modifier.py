import sqlite3
from datetime import datetime
from Data_Modifiers.json_modifier import DataParser
from Model.userinfo import User


# Pulling the date and time to name the table
def returnDatetime() -> str:
    current_time = datetime.utcnow()
    str_current_time = str(current_time.date()).replace('-', '') + str(current_time.hour) + str(
        current_time.minute) + str(current_time.second)
    return str_current_time


class DbModifier:

    def __init__(self, dbname: str) -> None:
        self.dbname = dbname
        self.tableName = self.tableName()
        self.dbConnection = self.connect(dbname)

    # Connection phase
    def connect(self, dbname: str) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(self.dbname)
            # c = conn.cursor()
            # c.fetchall()
            print(f"Connected to database {self.dbname} successfully")
            return conn
        except sqlite3.Error as error:
            print("Failed to connect with sqlite3 database", error)

    # Closing the connection
    def closeConnection(self, conn: sqlite3.Connection):
        conn.close()

    # Uses data and time info to name the table
    def tableName(self):
        tableid = datetime.now().strftime('%Y_%m_%d_%H%M%S')
        tableName = "data_" + tableid
        return tableName

    # Creates the table
    def createTable(self):
        curr = self.dbConnection
        columns = """email, username, fullname, emailuserlk, usernamelk, 
             yearofBirth, birthMonth, birthDay, country, ap"""
        tableSql = """CREATE TABLE IF NOT EXISTS %s (%s)""" % (self.tableName, columns)
        curr.execute(tableSql)

    # For bulk insertions
    def insertUserList(self, userlist):
        for user in userlist:
            self.insertUser(user)

    # Main insertion function
    def insertUser(self, user: User):
        try:
            insertingQuery = f"""
            INSERT INTO {self.tableName} 
            (email, username, fullname, emailuserlk, usernamelk, yearofBirth,
            birthMonth, birthDay, country, ap)
            VALUES (?,?,?,?,?,?,?,?,?,?)"""

            cr = self.dbConnection.cursor()
            cr.execute(insertingQuery, (
                user.email, user.username, user.fullName, user.emailUsrLk, user.userNameLk, user.yearofBirth,
                user.birthMonth,
                user.birthDay, user.country, user.ap))
            self.dbConnection.commit()

        except:
            print("Insertion failed.")

        finally:
            self.dbConnection.close()
