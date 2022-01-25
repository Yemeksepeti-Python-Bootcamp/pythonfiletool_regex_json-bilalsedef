import json
from os import sep
from Model.userinfo import User
from Data_Modifiers.regex_modifiers import regex_check


class DataParser:
    def __init__(self, filename):
        self.filename = filename

    def getjson(self):
        # Reading json file content
        with open(self.filename) as json_file:
            data = json.load(json_file)
            return data

    def jsontolist(self):
        # Converting json contents to list items
        converted_user_data = list()
        aList = self.getjson()
        for i in range(len(aList)):
            email = aList[i]["email"]
            username = aList[i]["username"]
            fullname = aList[i]["profile"]["name"]
            dob = aList[i]["profile"]["dob"]
            checker = regex_check(email, username, fullname, dob)
            emailuserlk = checker.isValid()[0]
            usernamelk = checker.isValid()[1]
            yearofBirth = int(checker.dob[0])
            birthMonth = int(checker.dob[1])
            birthDay = int(checker.dob[2])
            country = aList[i]["profile"]["address"][-1]
            save_user = User(email, username, fullname, yearofBirth, emailuserlk, usernamelk, birthMonth, birthDay, country)
            converted_user_data.append(save_user)
        return converted_user_data
