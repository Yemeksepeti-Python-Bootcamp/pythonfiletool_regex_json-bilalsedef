import re


class regex_check():
    def __init__(self, email, username, fullname, dob):
        self.email = email
        self.username = username.lower()
        self.fullname = fullname.lower()
        self.dob = list(dob.split("-"))

    def isValid(self):
        # Checking validations according to the constraints
        results = [0, 0]
        if self.username in list(re.findall(r'(.+)@(.+)\.(.+)', self.email))[0][0]:
            results[0] = 1
        else:
            if len([i for i in list(list(re.findall(r'(.+)@(.+)\.(.+)', self.email))[0][0]) if
                    i in self.username]) >= 3:
                results[0] = 1
            else:
                results[0] = 0
        # Checking if name or surname is in the username, only one of them is enough
        t = 0
        for i in list(str(self.fullname).split()):
            if i in self.username:
                results[1] = 1
                t += 1
            else:
                if t == 1:
                    results[1] = 1
                else:
                    results[1] = 0
        return results

    # Pulling year, month and day info from the full date
    def dob(self):
        year = self.dob[0]
        month = self.dob[1]
        day = self.dob[2]
        full_dob = [year, month, day]
        return full_dob
