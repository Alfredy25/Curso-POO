from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    _id: Optional[int]
    _username: str
    _password: str
    _email: str

    def __str__(self):
        return f'id={self.id}, username={self.username}, password={self.password}, email={self.email}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


