class User:
    def __init__(self, email="None", username="None", fullname="None", yearofBirth="NA", emailuserlk=1,
                 usernamelk=1, birthMonth=0, birthDay=0, country="empty", ap=1):
        self.email = email
        self.username = username
        self.fullName = fullname
        self.emailUsrLk = emailuserlk
        self.userNameLk = usernamelk
        self.yearofBirth = yearofBirth
        self.birthMonth = birthMonth
        self.birthDay = birthDay
        self.country = country
        self.ap = ap
