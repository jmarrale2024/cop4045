"""Analyze daily weather observations for multiple stations."""

from datetime import datetime
import os
import sys
import tempfile
import unittest


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"
MIN_TEMPERATURE = -100.0
MAX_TEMPERATURE = 150.0


def read_observations(filename):
	"""Read observations and return (observations, errors)."""
	observations = {}
	errors = []
	seen = set()

	with open(filename, "r", encoding="utf-8") as input_file:
		for line_number, line in enumerate(input_file, start=1):
			fields = line.strip().split(",")
			if len(fields) != 3 or not fields[0].strip() or not fields[1].strip():
				errors.append((line_number, "malformed line"))
				continue

			station = fields[0].strip()
			date_text = fields[1].strip()
			temperature_text = fields[2].strip()

			try:
				date = datetime.strptime(date_text, DATE_FORMAT)
			except ValueError:
				errors.append((line_number, "invalid date"))
				continue

			try:
				temperature = float(temperature_text)
			except ValueError:
				errors.append((line_number, "invalid temperature"))
				continue

			if not MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
				errors.append((line_number, "temperature out of range"))
				continue

			observation_key = (station, date)
			if observation_key in seen:
				errors.append((line_number, "duplicate station/date"))
				continue

			seen.add(observation_key)
			observations.setdefault(station, []).append((date, temperature))

	for station in observations:
		observations[station].sort(key=lambda observation: observation[0])

	return observations, errors


def station_statistics(observations):
	"""Return (minimum, maximum, mean) temperatures for every station."""
	return {
		station: (
			min(temperature for _, temperature in station_observations),
			max(temperature for _, temperature in station_observations),
			sum(temperature for _, temperature in station_observations)
			/ len(station_observations),
		)
		for station, station_observations in observations.items()
	}


def station_outliers(observations):
	"""Return stations whose latest temperature exceeds their mean."""
	statistics = station_statistics(observations)
	return {
		station: (date, temperature, statistics[station][2])
		for station, station_observations in observations.items()
		for date, temperature in station_observations[-1:]
		if temperature > statistics[station][2]
	}


def write_statistics(filename, statistics):
	"""Write sorted station statistics with one decimal place."""
	with open(filename, "w", encoding="utf-8") as output_file:
		for station in sorted(statistics):
			minimum, maximum, mean = statistics[station]
			output_file.write(
				f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n"
			)


def main():
	"""Read command-line files, print results, and write statistics."""
	if len(sys.argv) != 3:
		print("Usage: python p5_Jacob_Marrale.py input_file output_file")
		return

	input_filename, output_filename = sys.argv[1:]
	try:
		observations, errors = read_observations(input_filename)
		statistics = station_statistics(observations)
		outliers = station_outliers(observations)
		write_statistics(output_filename, statistics)
	except OSError as error:
		print(f"File access error: {error}")
		return

	print("Statistics:")
	for station in sorted(statistics):
		minimum, maximum, mean = statistics[station]
		print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")

	print("Outliers:")
	for station in sorted(outliers):
		date, temperature, mean = outliers[station]
		print(f"{station}: {date.strftime(DATE_FORMAT)}, {temperature:.1f}, mean={mean:.1f}")

	if errors:
		print("Errors:")
		for line_number, message in errors:
			print(f"line {line_number}: {message}")


class WeatherStationTests(unittest.TestCase):
	"""Tests for weather observation analysis."""

	def write_input(self, contents):
		file_handle = tempfile.NamedTemporaryFile(
			mode="w", encoding="utf-8", delete=False
		)
		file_handle.write(contents)
		file_handle.close()
		self.addCleanup(os.unlink, file_handle.name)
		return file_handle.name

	def test_reads_several_stations_and_sorts_observations(self):
		filename = self.write_input(
			"StationB,09:28:09 AM 04/21/2026,70\n"
			"StationA,09:28:09 AM 04/20/2026,60\n"
			"StationB,09:28:09 AM 04/20/2026,65\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(errors, [])
		self.assertEqual(list(observations), ["StationB", "StationA"])
		self.assertLess(observations["StationB"][0][0], observations["StationB"][1][0])

	def test_accepts_negative_temperature(self):
		filename = self.write_input("North,09:28:09 AM 01/01/2026,-40.5\n")

		observations, errors = read_observations(filename)

		self.assertEqual(errors, [])
		self.assertEqual(observations["North"][0][1], -40.5)

	def test_rejects_duplicate_observation(self):
		filename = self.write_input(
			"Station,09:28:09 AM 04/20/2026,70\n"
			"Station,09:28:09 AM 04/20/2026,71\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(len(observations["Station"]), 1)
		self.assertEqual(errors, [(2, "duplicate station/date")])

	def test_rejects_invalid_ranges_and_malformed_lines(self):
		filename = self.write_input(
			"Station,09:28:09 AM 04/20/2026,150.1\n"
			"Station,09:28:09 AM 04/20/2026,-100.1\n"
			"missing fields\n"
		)

		observations, errors = read_observations(filename)

		self.assertEqual(observations, {})
		self.assertEqual(
			errors,
			[
				(1, "temperature out of range"),
				(2, "temperature out of range"),
				(3, "malformed line"),
			],
		)

	def test_calculates_statistics_and_outliers(self):
		filename = self.write_input(
			"Station,09:28:09 AM 04/20/2026,10\n"
			"Station,09:28:09 AM 04/21/2026,20\n"
			"Other,09:28:09 AM 04/20/2026,20\n"
		)
		observations, _ = read_observations(filename)

		self.assertEqual(station_statistics(observations)["Station"], (10.0, 20.0, 15.0))
		self.assertIn("Station", station_outliers(observations))
		self.assertNotIn("Other", station_outliers(observations))

	def test_writes_sorted_statistics_with_one_decimal(self):
		output_filename = os.path.join(tempfile.gettempdir(), "weather_statistics_test.txt")
		self.addCleanup(
			lambda: os.path.exists(output_filename) and os.unlink(output_filename)
		)
		write_statistics(
			output_filename,
			{"Zoo": (1, 2.345, 1.5), "Alpha": (-4.2, 9, 2.25)},
		)

		with open(output_filename, "r", encoding="utf-8") as output_file:
			result = output_file.read()
		self.assertEqual(result, "Alpha,-4.2,9.0,2.2\nZoo,1.0,2.3,1.5\n")

	def test_missing_file_raises_file_not_found(self):
		with self.assertRaises(FileNotFoundError):
			read_observations("file_that_does_not_exist.txt")


if __name__ == "__main__":
	main()
