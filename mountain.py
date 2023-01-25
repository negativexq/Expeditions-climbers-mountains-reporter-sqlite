class Mountain:
    def __init__(
        self,
        id: int,
        name: str,
        country: str,
        rank: int,
        height: int,
        prominence: int,
        range: str,
    ):
        self.id = id
        self.name = name
        self.country = country
        self.rank = rank
        self.height = height
        self.prominence = prominence
        self.range = range
        self.expeditions = []  # list to store Expedition objects for this mountain

    def set_expeditions(self, expedition):
        self.expeditions.append(expedition)

    def height_difference(self):
        return self.height - self.prominence

    def get_height(self):
        return self.height

    def get_expeditions(self):
        return self.expeditions

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
