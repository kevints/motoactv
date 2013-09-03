import datetime
from motoactv import Motoactv
from unittest import TestCase
from unittest.mock import MagicMock

PAST_WORKOUTS_DATA = b"""
{
    "overviewMetrics": [
        "DURATION",
        "DISTANCE",
        "AVGPACE",
        "CALORIEBURN"
    ],
    "pastWorkoutActivityList": [
        "1"
    ],
    "pastWorkouts": [
        {
            "AVGCALBURN": 14.25,
            "AVGPACE": 555.12,
            "AVGSPEED": 6.49,
            "AVG_STEPRATE": 156.92,
            "CALORIEBURN": 570.24,
            "COUNT": 6305.0,
            "DISTANCE": 4.33,
            "DURATION": 2401.0,
            "HEARTRATEAVERAGE": 0.0,
            "HEARTRATEMAX": 0.0,
            "HEARTRATE_PEAK": 0.0,
            "MAX_ELEVATION": 176.96,
            "MAX_PACE": 0.22,
            "MAX_SPEED": 10.05,
            "MIN_ELEVATION": 0.32,
            "MIN_HEARTRATE": 0.0,
            "MIN_PACE": 0.0,
            "MIN_SPEED": 0.0,
            "Manual": false,
            "SPEED": 0.0,
            "WALK_DISTANCE": 0.0,
            "activity": "1",
            "endTime": 1378076851538,
            "is_modified_AVGCALBURN": false,
            "is_modified_AVGPACE": false,
            "is_modified_AVGSPEED": false,
            "is_modified_AVG_STEPRATE": false,
            "is_modified_CALORIEBURN": false,
            "is_modified_COUNT": false,
            "is_modified_DISTANCE": false,
            "is_modified_DURATION": false,
            "is_modified_HEARTRATEAVERAGE": false,
            "is_modified_HEARTRATEMAX": false,
            "is_modified_HEARTRATE_PEAK": false,
            "is_modified_MAX_ELEVATION": false,
            "is_modified_MAX_PACE": false,
            "is_modified_MAX_SPEED": false,
            "is_modified_MIN_ELEVATION": false,
            "is_modified_MIN_HEARTRATE": false,
            "is_modified_MIN_PACE": false,
            "is_modified_MIN_SPEED": false,
            "is_modified_SPEED": false,
            "is_modified_WALK_DISTANCE": false,
            "startTime": 1378074378342,
            "tableViewMetrics": [
                "DURATION",
                "WALK_DISTANCE",
                "CALORIEBURN",
                "DISTANCE"
            ],
            "tileMetrics": [
                "DURATION",
                "DISTANCE",
                "CALORIEBURN"
            ],
            "workoutActivityId": "A9OAOTHVToSwUzKvJta1rA==",
            "workoutSummaryId": "g+ncW9U0TKy84+CSpoOBXA=="
        },
        {
            "AVGCALBURN": 14.36,
            "AVGPACE": 559.73,
            "AVGSPEED": 6.43,
            "AVG_STEPRATE": 157.64,
            "CALORIEBURN": 391.84,
            "COUNT": 4314.0,
            "DISTANCE": 2.92,
            "DURATION": 1637.0,
            "HEARTRATEAVERAGE": 0.0,
            "HEARTRATEMAX": 0.0,
            "HEARTRATE_PEAK": 0.0,
            "MAX_ELEVATION": 82.02,
            "MAX_PACE": 0.22,
            "MAX_SPEED": 10.04,
            "MIN_ELEVATION": 0.05,
            "MIN_HEARTRATE": 0.0,
            "MIN_PACE": 0.0,
            "MIN_SPEED": 0.0,
            "Manual": false,
            "SPEED": 0.0,
            "WALK_DISTANCE": 0.0,
            "activity": "1",
            "endTime": 1377805443991,
            "is_modified_AVGCALBURN": false,
            "is_modified_AVGPACE": false,
            "is_modified_AVGSPEED": false,
            "is_modified_AVG_STEPRATE": false,
            "is_modified_CALORIEBURN": false,
            "is_modified_COUNT": false,
            "is_modified_DISTANCE": false,
            "is_modified_DURATION": false,
            "is_modified_HEARTRATEAVERAGE": false,
            "is_modified_HEARTRATEMAX": false,
            "is_modified_HEARTRATE_PEAK": false,
            "is_modified_MAX_ELEVATION": false,
            "is_modified_MAX_PACE": false,
            "is_modified_MAX_SPEED": false,
            "is_modified_MIN_ELEVATION": false,
            "is_modified_MIN_HEARTRATE": false,
            "is_modified_MIN_PACE": false,
            "is_modified_MIN_SPEED": false,
            "is_modified_SPEED": false,
            "is_modified_WALK_DISTANCE": false,
            "startTime": 1377803765256,
            "tableViewMetrics": [
                "DURATION",
                "WALK_DISTANCE",
                "CALORIEBURN",
                "DISTANCE"
            ],
            "tileMetrics": [
                "DURATION",
                "DISTANCE",
                "CALORIEBURN"
            ],
            "workoutActivityId": "fInDh685Sqi9VCKb+szz5g==",
            "workoutSummaryId": "PqReL4yiRJGkLH+oVsRG4Q=="
        },
        {
            "AVGCALBURN": 14.75,
            "AVGPACE": 548.44,
            "AVGSPEED": 6.56,
            "AVG_STEPRATE": 156.42,
            "CALORIEBURN": 722.71,
            "COUNT": 7697.0,
            "DISTANCE": 5.36,
            "DURATION": 2940.0,
            "HEARTRATEAVERAGE": 0.0,
            "HEARTRATEMAX": 0.0,
            "HEARTRATE_PEAK": 0.0,
            "MAX_ELEVATION": 179.09,
            "MAX_PACE": 0.19,
            "MAX_SPEED": 11.85,
            "MIN_ELEVATION": 0.68,
            "MIN_HEARTRATE": 0.0,
            "MIN_PACE": 0.0,
            "MIN_SPEED": 0.0,
            "Manual": false,
            "SPEED": 0.0,
            "WALK_DISTANCE": 0.0,
            "activity": "1",
            "endTime": 1377655133163,
            "is_modified_AVGCALBURN": false,
            "is_modified_AVGPACE": false,
            "is_modified_AVGSPEED": false,
            "is_modified_AVG_STEPRATE": false,
            "is_modified_CALORIEBURN": false,
            "is_modified_COUNT": false,
            "is_modified_DISTANCE": false,
            "is_modified_DURATION": false,
            "is_modified_HEARTRATEAVERAGE": false,
            "is_modified_HEARTRATEMAX": false,
            "is_modified_HEARTRATE_PEAK": false,
            "is_modified_MAX_ELEVATION": false,
            "is_modified_MAX_PACE": false,
            "is_modified_MAX_SPEED": false,
            "is_modified_MIN_ELEVATION": false,
            "is_modified_MIN_HEARTRATE": false,
            "is_modified_MIN_PACE": false,
            "is_modified_MIN_SPEED": false,
            "is_modified_SPEED": false,
            "is_modified_WALK_DISTANCE": false,
            "startTime": 1377652187513,
            "tableViewMetrics": [
                "DURATION",
                "WALK_DISTANCE",
                "CALORIEBURN",
                "DISTANCE"
            ],
            "tileMetrics": [
                "DURATION",
                "DISTANCE",
                "CALORIEBURN"
            ],
            "workoutActivityId": "97Mg5ol6T4edkKJt9Fkh/w==",
            "workoutSummaryId": "7EciNIHtS+ya9t6gaW4tMw=="
        }
    ],
    "recentWorkoutUserPreferences": {
        "endDate": 0,
        "metricType": null,
        "userEmail": null
    },
    "summary": {
        "AVGPACE": 554.43,
        "DISTANCE": 12.61,
        "DURATION": 6978.0
    }
}
"""


END_DATE = datetime.datetime(2013, 9, 2, 15, 50, 29, 637945)
START_DATE = END_DATE - datetime.timedelta(weeks=1)


class MotoactvTest(TestCase):
  def setUp(self):
    self.urlopener = MagicMock()

    self.motoactv = Motoactv(username="fake@fake.com", password="fake", urlopener=self.urlopener)

  def test_login(self):
    response = MagicMock()
    self.urlopener.open.return_value = response
    response.read.return_value = b'{}'

    self.motoactv.login()

    self.assertTrue(self.urlopener.open.called)
    self.assertTrue(response.read.called)


  def test_past_workouts(self):
    self.test_login()

    response = MagicMock()
    self.urlopener.open.return_value = response
    response.read.return_value = PAST_WORKOUTS_DATA
    
    self.motoactv.past_workouts(START_DATE, END_DATE)

    self.assertTrue(self.urlopener.open.called)
    self.assertTrue(response.read.called)
