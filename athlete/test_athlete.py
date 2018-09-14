import unittest
from athlete import *


class AthleteTests(unittest.TestCase):

	def setUp(self):
		self.athlete_1 = Athlete()

	def test_total_distance_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.athlete_1.total_distance, 0)

	def test_total_time_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.athlete_1.total_time, 0)

	def test_validate_time_if_validate_time_raise_an_exception(self):
		with self.assertRaises(Exception):
			self.athlete_2 = Athlete(0, 10)
			self.athlete_2.validate_time()

class RunnerTests(unittest.TestCase):

	def setUp(self):
		self.runner_1 = Runner()
		self.runner_2 = Runner(10,10)

	def test_total_distance_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.runner_1.total_distance, 0)

	def test_total_time_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.runner_1.total_time, 0)

	def test_validate_time_if_validate_time_raise_an_exception(self):
		with self.assertRaises(Exception):
			self.runner_3 = Runner(0, 10)
			self.runner_3.validate_time()

	def test_speed_speed_as_getter(self):
		raised = False
		try:
			self.runner_1.speed
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_speed_speed_as_setter(self):
		raised = False
		try:
			self.runner_1.speed = 0
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_time_total_time_as_getter(self):
		raised = False
		try:
			self.runner_1.total_time
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")
	#2da parte
	def test_total_time_total_time_as_setter(self):
		raised = False
		try:
			self.runner_1.total_time = 20
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_speed_record_if_speed_record_exists(self):
		raised = False
		try:
			self.runner_1.speed_record()
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_distance_total_distance_as_getter(self):
		raised = False
		try:
			self.runner_1.total_distance
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_distance_total_distance_as_setter(self):
		raised = False
		try:
			self.runner_1.total_distance = 10
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_run_returns_a_string_with_total_distance_total_time_and_speed_when_distance_0_and_time_0(self):
		self.assertEqual(self.runner_1.run(), "I'm a Runner and Ran 0 meters, time: 0 seconds, speed: 0 m/s")

	def test_run_returns_a_string_with_total_distance_total_time_and_speed_when_distance_greater_than_0_and_time_greater_than_0(self):
		self.assertEqual(self.runner_2.run(), "I'm a Runner and Ran 10 meters, time: 10 seconds, speed: 1.0 m/s")

	def test_new_workout_if_new_workout_increments_total_distance_and_total_time(self):
		raised = False
		try:
			self.runner_1.new_workout(20, 7)
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")
		self.assertEqual(self.runner_1.run(), "I'm a Runner and Ran 20 meters, time: 7 seconds, speed: 2.86 m/s")

class SwimmerTests(unittest.TestCase):

	def setUp(self):
		self.swimmer_1 = Swimmer(50, 5)

	def test_swim_returns_a_string_with_total_distance_total_time_and_speed_when_distance_50_and_time_5(self):
		self.assertEqual(self.swimmer_1.swim(), "I'm a Swimmer and Swim 50 meters, time: 5 seconds, speed: 10.0 m/s")

#crear Cyclist class *************

class CyclistTest(unittest.TestCase):

	def setUp(self):
		self.cyclist_1 = Cyclist(75, 5)

	def test_roll_a_bicla_returns_a_string_with_total_distance_total_time_and_speed_when_distance_75_and_time_5(self):
		self.assertEqual(self.cyclist_1.roll_a_bicla(), "I'm a Cyclist and Roll 75 meters, time: 5 seconds, speed: 15.0 m/s")


if __name__=="__main__":
    unittest.main()
