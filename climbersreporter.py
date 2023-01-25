from mountain import Mountain
from expedition import Expedition
from climber import Climber
from datetime import datetime
import csv
import sqlite3


class Reporter:
    # How many climbers are there? -> int
    def total_amount_of_climbers(self) -> int:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM climbers")
        climbers = []
        for row in c.fetchall():
            climbers.append(Climber(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return len(climbers)

    # What is the highest mountain? -> Mountain
    def highest_mountain(self) -> Mountain:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM mountains")
        mountains = []
        for row in c.fetchall():
            mountains.append(
                Mountain(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for mountain in mountains:
            for expedition in expeditions:
                if mountain.id == expedition.mountain_id:
                    mountain.expeditions.append(expedition)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        return max(mountains, key=lambda x: x.height)

    # What is the longest and shortest expedition? ->
    def longest_and_shortest_expedition(self) -> tuple[Expedition, Expedition]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers to the expedition
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        return (
            max(expeditions, key=lambda x: x.duration),
            min(expeditions, key=lambda x: x.duration),
        )

    # Which expeditons have the most climbers -> tuple[Expedition, ...]
    def expedition_with_most_climbers(self) -> tuple[Expedition, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row[1])
        max_expedition = max(expedition_climbers, key=expedition_climbers.count)
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers to expeditions
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        return tuple(filter(lambda x: x.id == max_expedition, expeditions))

    # Which climbers have made the most expeditions -> tuple[Climber, ...]
    def climbers_with_most_expeditions(
        self, only_succesful: bool = False
    ) -> tuple[Climber, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row[0])
        max_climber = max(expedition_climbers, key=expedition_climbers.count)
        c.execute("SELECT * FROM climbers")
        climbers = []
        for row in c.fetchall():
            climbers.append(Climber(row[0], row[1], row[2], row[3], row[4]))
        # append the expeditions to climbers
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        expedition_climbers = []
        c.execute("SELECT * FROM expedition_climbers")
        for row in c.fetchall():
            expedition_climbers.append(row)
        for climber in climbers:
            for expedition in expeditions:
                for climber_expedition in expedition_climbers:
                    if (
                        climber.id == climber_expedition[0] and expedition.id == climber_expedition[1]
                    ):
                        climber.expeditions.append(expedition)
        if only_succesful:
            for climber in climbers:
                climber.expeditions = tuple(
                    filter(lambda x: x.success, climber.expeditions)
                )
        conn.close()
        return tuple(filter(lambda x: x.id == max_climber, climbers))

    # Which mountain has the most expeditions -> Mountain
    def mountains_with_most_expeditions(self) -> tuple[Mountain, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        c.execute("SELECT * FROM mountains")
        mountains = []
        for row in c.fetchall():
            mountains.append(
                Mountain(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )
        for mountain in mountains:
            for expedition in expeditions:
                if mountain.id == expedition.mountain_id:
                    mountain.expeditions.append(expedition)
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        max_expedition = max(mountains, key=lambda x: len(x.expeditions))
        return tuple(filter(lambda x: x.id == max_expedition.id, mountains))

    # Which expedition was the first successful expedition? -> Expedition
    def get_first_successful_expedition(self) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        return min(
            filter(lambda x: x.success, expeditions),
            key=lambda x: x.date,
        )

    def get_first_expedition(self, only_succesful: bool = False) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        if only_succesful:
            expeditions = tuple(filter(lambda x: x.success, expeditions))
        conn.close()
        return min(expeditions, key=lambda x: x.date)

    # Which succesful expedition is the latetst? -> Expedition
    def get_latest_successful_expedition(self) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        # return the latest expedition that was successful
        return max(
            filter(lambda x: x.success, expeditions),
            key=lambda x: x.date,
        )

    def get_latest_expedition(self, only_succesful: bool = False) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        return max(expeditions, key=lambda x: x.date)

    # Which climbers have climbed mountain Z between period X and Y? -> tuple[Climber, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Climbers Mountain Z between X and Y.csv`
    # otherwise it should just return the value as tuple(Climber, ...)
    # CSV example:
    #   Id, first_name, last_name, nationality, date_of_birth
    def get_climbers_that_climbed_mountain_between(
        self, mountain: Mountain, start: datetime, end: datetime, to_csv: bool = False
    ) -> tuple[Climber, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM expeditions")
        expeditions = []
        for row in c.fetchall():
            expeditions.append(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
        # append the climbers
        c.execute("SELECT * FROM expedition_climbers")
        expedition_climbers = []
        for row in c.fetchall():
            expedition_climbers.append(row)
        for expedition in expeditions:
            for climber in expedition_climbers:
                if expedition.id == climber[1]:
                    expedition.climbers.append(climber[0])
        conn.close()
        climbers = []
        for expedition in expeditions:
            if (
                mountain.id in expedition.mountains and expedition.date >= start and expedition.date <= end
            ):
                for climber in expedition.climbers:
                    climbers.append(climber)
        if to_csv:
            with open(
                "Climbers Mountain Z between X and Y.csv", "w", newline=""
            ) as csvfile:
                fieldnames = [
                    "Id",
                    "first_name",
                    "last_name",
                    "nationality",
                    "date_of_birth",
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for climber in climbers:
                    writer.writerow(
                        {
                            "Id": climber.id,
                            "first_name": climber.first_name,
                            "last_name": climber.last_name,
                            "nationality": climber.date_of_birth,
                            "date_of_birth": climber.date_of_birth,
                        }
                    )
        return tuple(climbers)

    # Which mountains are located in country X? ->tuple[Mountain, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Mountains in country X.csv`
    # otherwise it should just return the value as tuple(Mountain, ...)
    # CSV example:
    #   Id, name, country, rank, height, prominence, range
    def get_mountains_in_country(
        self, country: str, to_csv: bool = False
    ) -> tuple[Mountain, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM mountains")
        mountains = []
        for row in c.fetchall():
            mountains.append(
                Mountain(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )
        conn.close()
        mountains_in_country = tuple(filter(lambda x: x.country == country, mountains))
        if to_csv:
            with open(f"Mountains in country {country}.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["id", "name", "country", "rank", "height", "prominence", "range"]
                )
                for mountain in mountains_in_country:
                    writer.writerow(
                        [
                            mountain.id,
                            mountain.name,
                            mountain.country,
                            mountain.rank,
                            mountain.height,
                            mountain.prominence,
                            mountain.range,
                        ]
                    )
            return None
        return mountains_in_country

    # Which climbers are from country X? -> tuple[Climber, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Climbers in country X.csv`
    # otherwise it should just return the value as tuple(Climber, ...)
    # CSV example:
    #   Id, first_name, last_name, nationality, date_of_birth
    def get_climbers_from_country(
        self, country: str, to_csv: bool = False
    ) -> tuple[Climber, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT * FROM climbers")
        climbers = []
        for row in c.fetchall():
            climbers.append(Climber(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        climbers_from_country = tuple(
            filter(lambda x: x.nationality == country, climbers)
        )
        if to_csv:
            with open(f"Climbers in country {country}.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["id", "first_name", "last_name", "nationality", "date_of_birth"]
                )
                for climber in climbers_from_country:
                    writer.writerow(
                        [
                            climber.id,
                            climber.first_name,
                            climber.last_name,
                            climber.nationality,
                            climber.date_of_birth,
                        ]
                    )
            return None
        return climbers_from_country
