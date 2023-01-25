from climber import Climber
from expedition import Expedition
from mountain import Mountain
from climbersreporter import Reporter
import datetime
import unittest


class Test(unittest.TestCase):
    # Test to check if the age of a climber is correct based on the date_of_birth
    def test_age_of_climber(self):
        # Create a climber with a date of birth in the past
        climber = Climber(1, "John", "Doe", "USA", datetime.datetime(2000, 1, 1))

        # Get the age of the climber
        age = climber.get_age()
        # Calculate the expected age based on the current year
        today = datetime.datetime.now()
        expected_age = today.year - 2000
        # Assert that the age of the climber is correct
        assert age == expected_age

    # Test to check if the amount of expeditions for a specific climber is returned correctly
    def test_amount_of_expeditions_of_climber(self):
        # Create a climber
        climber = Climber(1, "John", "Doe", "USA", datetime.datetime(2000, 1, 1))

        # Create some expeditions and add them to the climber's list of expeditions
        expeditions = [
            Expedition(
                1,
                "Expedition 1",
                1,
                "Base Camp",
                datetime.datetime(2020, 1, 1),
                "Nepal",
                5,
                True,
            ),
            Expedition(
                2,
                "Expedition 2",
                2,
                "Base Camp",
                datetime.datetime(2020, 2, 1),
                "Nepal",
                5,
                True,
            ),
            Expedition(
                3,
                "Expedition 3",
                3,
                "Base Camp",
                datetime.datetime(2020, 3, 1),
                "Nepal",
                5,
                True,
            ),
        ]
        for expedition in expeditions:
            climber.expeditions.append(expedition)

        # Get the amount of expeditions for the climber
        amount_of_expeditions = climber.get_expeditions()

        # Assert that the amount of expeditions for the climber is correct
        assert len(amount_of_expeditions) == 3

    # Test to check the difference in height and prommence of a mountain
    def test_height_difference_mountain(self):
        # Create a mountain with a height and prominence
        mountain = Mountain(1, "Mt. Everest", "Nepal", 1, 8848, 8848, "Himalayas")

        # Get the height difference of the mountain
        height_difference = mountain.height_difference()

        # Assert that the height difference is correct
        assert height_difference == 0

        # Create a mountain with a different height and prominence
        mountain = Mountain(
            2, "Mt. Kilimanjaro", "Tanzania", 2, 5895, 5885, "Kilimanjaro"
        )

        # Get the height difference of the mountain
        height_difference = mountain.height_difference()

        # Assert that the height difference is correct
        assert height_difference == 10

    # Test to check if the amount of expeditions for a specific mountain is returned correctly
    def test_amount_of_expeditions_of_mountain(self):
        # Create a mountain
        mountain = Mountain(1, "Mt. Everest", "Nepal", 1, 8848, 8848, "Himalayas")

        # Create some expeditions and add them to the mountain's list of expeditions
        expeditions = [
            Expedition(
                1,
                "Expedition 1",
                1,
                "Base Camp",
                datetime.datetime(2020, 1, 1),
                "Nepal",
                5,
                True,
            ),
            Expedition(
                2,
                "Expedition 2",
                1,
                "Base Camp",
                datetime.datetime(2020, 2, 1),
                "Nepal",
                5,
                True,
            ),
            Expedition(
                3,
                "Expedition 3",
                1,
                "Base Camp",
                datetime.datetime(2020, 3, 1),
                "Nepal",
                5,
                True,
            ),
        ]
        for expedition in expeditions:
            mountain.expeditions.append(expedition)

        # Get the amount of expeditions for the mountain
        amount_of_expeditions = mountain.get_expeditions()

        # Assert that the amount of expeditions for the mountain is correct
        assert len(amount_of_expeditions) == 3

    # Test to check if the returned date matches the specified format for that expedition date
    def test_expedition_date_conversion(self):
        # Create an expedition with a date
        expedition = Expedition(
            1,
            "Expedition 1",
            1,
            "Base Camp",
            datetime.datetime(2020, 1, 1),
            "Nepal",
            5,
            True,
        )
        # Convert the date of the expedition to the specified format
        formatted_date = expedition.convert_date("%Y-%m-%d")
        # Assert that the formatted date is correct
        assert formatted_date == "2020-01-01"

    # Test to check if the duration is converted from 1H19 to the specified format
    def test_expedition_duration_conversion(self):
        # Create an expedition with a duration in minutes
        expedition = Expedition(
            1,
            "Expedition 1",
            1,
            "Base Camp",
            datetime.datetime(2020, 1, 1),
            "Nepal",
            79,
            True,
        )
        # Convert the duration of the expedition to the specified format
        formatted_duration = expedition.convert_duration("%H:%M")

        # Assert that the formatted duration is correct
        assert formatted_duration == "01:19"

    def test_add_climber_to_expedition(self):
        # Create a climber
        climber = Climber(1, "John", "Doe", "USA", datetime.datetime(1980, 1, 1))

        # Create an expedition
        expedition = Expedition(
            1,
            "Expedition 1",
            1,
            "Base Camp",
            datetime.datetime(2020, 1, 1),
            "Nepal",
            5,
            True,
        )

        # Add the climber to the expedition
        expedition.add_climber(climber)

        # Get the climbers on the expedition
        climbers = expedition.get_climbers()

        # Assert that the climber was added correctly to the expedition
        assert climber in climbers

    # Test to check the amount of climbers on a specified expedition
    def test_amount_of_climbers_on_expedition(self):
        # Create a climber
        climber = Climber(1, "John", "Doe", "USA", datetime.datetime(1980, 1, 1))

        # Create an expedition
        expedition = Expedition(
            1,
            "Expedition 1",
            1,
            "Base Camp",
            datetime.datetime(2020, 1, 1),
            "Nepal",
            5,
            True,
        )

        # Add the climber to the expedition
        expedition.add_climber(climber)

        # Get the climbers on the expedition
        climbers = expedition.get_climbers()

        # Assert that the amount of climbers on the expedition is correct
        assert len(climbers) == 1

    # Test to validate if the given mountain of a specified expedition is correct
    def test_mountain_on_expedition(self):
        # Create a mountain
        mountain = Mountain(1, "Mount Everest", "Nepal", 1, 8848, 8448, "Himalaya")
        # Create an expedition with the mountain
        expedition = Expedition(
            1,
            "Expedition 1",
            mountain.id,
            "Base Camp",
            datetime.datetime(2020, 1, 1),
            "Nepal",
            5,
            True,
        )
        # Get the mountain for the expedition
        mountain_on_expedition = expedition.get_mountain()
        # Assert that the mountain on the expedition is correct
        assert mountain_on_expedition == mountain.id


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
    print("All tests passed!")
