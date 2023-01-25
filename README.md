# Expeditions-climbers-mountains-reporter-sqlite

This project utilizes the classes Mountain, Expedition, and Climber to access and report on data from a SQLite database named "climbersapp.db". The Reporter class contains several methods that query the database and return information about the climbers, mountains, and expeditions.

## Installation
To run the project, you will need to have Python and SQLite installed on your machine.
1. Clone the repository
2. Create the SQLite database named "climbersapp.db" and import the necessary tables and data

## Climber
The `Climber` class has the following attributes:
- `id`: int
- `first_name`: str
- `last_name`: str
- `nationality`: str
- `date_of_birth`: datetime.datetime
- `expeditions`: list of Expedition objects

It also has the following methods:
- `__repr__`: returns a string representation of the object, excluding the `expeditions` attribute
- `get_age`: returns the age of the climber based on their date of birth
- `get_expeditions`: returns the list of expeditions the climber has been a part of

## Expedition
The `Expedition` class has the following attributes:
- `id`: int
- `name`: str
- `mountain_id`: int
- `start`: str
- `date`: datetime
- `country`: str
- `duration`: int (in minutes)
- `success`: bool
- `climbers`: list of Climber objects

It also has the following methods:
- `add_climber`: adds a `Climber` object to the `climbers` list
- `get_climbers`: returns the list of climbers on the expedition
- `get_mountain`: returns the `mountain_id` of the expedition
- `convert_date`: converts and returns the `date` attribute in the specified format
- `convert_duration`: converts and returns the `duration` attribute in the specified format (hh:mm)
- `__repr__`: returns a string representation of the object, excluding the `climbers` attribute

## Mountain
The `Mountain` class has the following attributes:
- `id`: int
- `name`: str
- `country`: str
- `rank`: int
- `height`: int (in meters)
- `prominence`: int (in meters)

It also has the following methods:
- `set_expeditions`: adds an `Expedition` object to the `expeditions` list
- `height_difference`: returns the difference between the mountain's `height` and `prominence`
- `get_height`: returns the `height` of the mountain
- `get_expedition`: returns the list of `expeditions` for the mountain
- `__repr__`: returns a string representation of the object.

## Reporter Methods
The `Reporter` class contains the following methods:
- `total_amount_of_climbers()`: returns the total number of `climbers` in the database.
- `highest_mountain()`: returns the highest `mountain` in the database.
- `longest_and_shortest_expedition()`: returns a tuple containing the longest and shortest `expeditions` in the database.
- `expedition_with_most_climbers()`: returns a tuple containing the expeditions that have the most `climbers`.
- `get_first_expedition(only_succesful: bool = False)`: returns the first `expedition` in the database. The optional parameter only_succesful allows you to filter the `expeditions` by success.
- `get_latest_successful_expedition()`: returns the latest successful `expedition` in the database.
- `get_latest_expedition(only_succesful: bool = False)`: returns the latest `expedition` in the database. The optional parameter only_succesful allows you to filter the `expeditions` by success.
- `get_climbers_that_climbed_mountain_between(mountain: Mountain, start: datetime, end: datetime, to_csv: bool = False)`: returns a tuple of `climbers` that climbed a specific `mountain` between a given start and end date. This method also has an optional parameter `to_csv` which, when set to `true`, generates a CSV file containing the information of the `climbers`.
- `get_climbers_from_country(country: str, to_csv: bool = False)`: returns a tuple of `climbers` from a specific country. The optional parameter `to_csv` allows you to generate a CSV file with the information of the climbers when set to `True`.
- `get_mountains_in_country(country: str, to_csv: bool = False)`: returns a tuple of `mountains` from a specific country. The optional parameter `to_csv` allows you to generate a CSV file with the information of the mountains when set to `True`.

Note that the methods are using specific database schema, also the csv generation should be handled in a separate function.

