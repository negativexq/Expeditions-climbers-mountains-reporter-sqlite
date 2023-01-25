import datetime
from climber import Climber


class Expedition:
    def __init__(
        self,
        id: int,
        name: str,
        mountain_id: int,
        start: str,
        date: datetime,
        country: str,
        duration: int,
        success: bool,
    ):
        self.id = id
        self.name = name
        self.mountain_id = mountain_id
        self.start = start
        self.date = date
        self.country = country
        self.duration = duration
        self.success = success
        self.climbers = []

    def add_climber(self, climber: Climber):
        self.climbers.append(climber)

    def get_climbers(self):
        return self.climbers

    def get_mountain(self):
        # search for mountain with mountain_id in the mountain table
        return self.mountain_id

    def convert_date(self, to_format: str) -> str:
        return self.date.strftime(to_format)

    def convert_duration(self, to_format: str) -> str:
        total_seconds = (
            self.duration * 60
        )  # duration is in minutes, so convert to seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02d}:{minutes:02d}"

    def __repr__(self) -> str:
        """dont show climbers"""
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                [
                    f"{key}={value!r}"
                    for key, value in self.__dict__.items()
                    if key != "climbers"
                ]
            ),
        )
