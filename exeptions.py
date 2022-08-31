class CompanyExistException(Exception):

    def __init__(self, company):
        self.message = f"We are sorry, but '{company}' already exists"
        super().__init__(self.message)


class NoSuchUserException(Exception):
    def __init__(self):
        self.message = f"Sorry,but such user isn't exists, try again"
        super().__init__(self.message)


class UserAlreadyExistsExeption(Exception):
    def __init__(self, login):
        self.message = f"Sorry, but user with login '{login}' already exists"
        super().__init__(self.message)


class EmptyScrollExeption(Exception):

    def __init__(self):
        self.message = "empty scroll"
        super().__init__(self.message)
