# Expeditions-climbers-mountains-reporter-sqlite

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
