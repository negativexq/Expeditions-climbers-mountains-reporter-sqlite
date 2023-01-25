import json
import sqlite3

from climber import Climber
from mountain import Mountain
from expedition import Expedition


def fill_database(json_file: str, database: str):
    with open(json_file, "r") as f:
        data = json.load(f)
    for j in range(len(data)):
        all_data = data[j]
        conn = sqlite3.connect(database)
        c = conn.cursor()
        name_1 = data[j]["climbers"]
        for i in range(len(name_1)):
            c.execute(
                "INSERT OR IGNORE INTO climbers VALUES (?, ?, ?, ?, ?)",
                (
                    name_1[i]["id"],
                    name_1[i]["first_name"],
                    name_1[i]["last_name"],
                    name_1[i]["nationality"],
                    name_1[i]["date_of_birth"],
                ),
            )

        mount = data[j]["mountain"]
        c.execute(
            "INSERT OR IGNORE INTO mountains VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                all_data["id"],
                mount["name"],
                mount["countries"][0],
                mount["rank"],
                mount["height"],
                mount["prominence"],
                mount["range"],
            ),
        )

        c.execute(
            "INSERT OR IGNORE INTO expeditions VALUES  (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                all_data["id"],
                all_data["name"],
                all_data["id"],
                all_data["start"],
                all_data["date"],
                all_data["country"],
                all_data["duration"],
                all_data["success"],
            ),
        )

        for i in range(len(name_1)):
            c.execute(
                "INSERT OR IGNORE INTO expedition_climbers VALUES (?, ?)",
                (name_1[i]["id"], all_data["id"]),
            )

        conn.commit()
        conn.close()


def load_climbers(database: str):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM climbers")
    climbers = []

    for row in c.fetchall():
        climbers.append(Climber(row[0], row[1], row[2], row[3], row[4]))

    for climber in climbers:
        c.execute(
            "SELECT * FROM expedition_climbers WHERE climber_id = ?", (climber.id,)
        )
        for row in c.fetchall():
            c.execute("SELECT * FROM expeditions WHERE id = ?", (row[1],))
            for row in c.fetchall():
                climber.expeditions.append(
                    Expedition(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                    )
                )
    conn.close()
    return climbers


def load_mountains(database: str):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM mountains")
    mountains = []
    for row in c.fetchall():
        mountain = Mountain(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        c.execute("SELECT * FROM expeditions WHERE mountain_id = ?", (mountain.id,))
        for row in c.fetchall():
            mountain.set_expeditions(
                Expedition(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            )
            """append the climbers to expeditions"""
            c.execute(
                "SELECT * FROM expedition_climbers WHERE expedition_id = ?", (row[0],)
            )
            for row in c.fetchall():
                c.execute("SELECT * FROM climbers WHERE id = ?", (row[0],))
                for row in c.fetchall():
                    mountain.expeditions[-1].add_climber(
                        Climber(row[0], row[1], row[2], row[3], row[4])
                    )
        mountains.append(mountain)
    conn.close()
    return mountains


def load_expeditions(
    database: str,
):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM expeditions")
    expeditions = []
    for row in c.fetchall():
        expenditions = Expedition(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )
        expeditions.append(expenditions)
    # append the climbers to expeditions
    for expedition in expeditions:
        c.execute(
            "SELECT * FROM expedition_climbers WHERE expedition_id = ?",
            (expedition.id,),
        )
        for row in c.fetchall():
            c.execute("SELECT * FROM climbers WHERE id = ?", (row[0],))
            for row in c.fetchall():
                expedition.add_climber(Climber(row[0], row[1], row[2], row[3], row[4]))
    conn.close()
    return expeditions


def main():
    fill_database("expeditions.json", "climbersapp.db")


if __name__ == "__main__":
    main()
