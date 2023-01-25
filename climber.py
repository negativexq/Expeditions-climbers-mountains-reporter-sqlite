import datetime


class Climber:
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        nationality: str,
        date_of_birth: datetime.datetime,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.expeditions = []

    def __repr__(self) -> str:
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                [
                    f"{key}={value!r}"
                    for key, value in self.__dict__.items()
                    if key != "expeditions"
                ]
            ),
        )

    def get_age(self):
        today = datetime.datetime.now()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (
            today.month == self.date_of_birth.month and today.day < self.date_of_birth.day
        ):
            age -= 1
        return age

    def get_expeditions(self):
        return self.expeditions
